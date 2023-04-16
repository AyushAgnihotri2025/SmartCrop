import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
import warnings

warnings.filterwarnings("ignore", message="Trying to unpickle estimator")

st.set_page_config(page_title="SmartCrop", page_icon="https://cdn.jsdelivr.net/gh/twitter/twemoji@master/assets/72x72/1f33f.png", layout='centered', initial_sidebar_state="collapsed")

def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:center;"> SmartCrop: Intelligent Crop Recommendation 🌱 </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    col = st.columns(1)[0]

    with col:
        st.subheader(" Find out the most suitable crop to grow in your farm 👨‍🌾")
        N = st.number_input("Nitrogen", 1,10000)
        P = st.number_input("Phosporus", 1,10000)
        K = st.number_input("Potassium", 1,10000)
        temp = st.number_input("Temperature",0.0,100000.0)
        humidity = st.number_input("Humidity in %", 0.0,100000.0)
        ph = st.number_input("Ph", 0.0,100000.0)
        rainfall = st.number_input("Rainfall in mm",0.0,100000.0)

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1,-1)
        
        if st.button('Predict'):

            loaded_model = load_model('model.pkl')
            prediction = loaded_model.predict(single_pred)
            col.write('''
		    ## Results 🔍 
		    ''')
            col.success(f"{prediction.item().title()} are recommended by the A.I for your farm.")
    #code for html ☘️ 🌾 🌳 👨‍🌾  🍃
    hide_menu_style = """
    <style>
    .block-container {padding: 2rem 1rem 3rem;}
    #MainMenu {visibility: hidden;}
    </style>
    """

hide_menu_style = """
        <style>
        .block-container {padding: 2rem 1rem 3rem;}
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
	main()