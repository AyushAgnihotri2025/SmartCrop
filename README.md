[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FAyushAgnihotri2025%2FSmartCrop%2F&count_bg=%2379C83D&title_bg=%23555555&icon=overleaf.svg&icon_color=%23E7E7E7&title=SmartCrop:+Intelligent+Crop+Recommendation&edge_flat=false)](https://github.com/AyushAgnihotri2025/Crop-Recommender)

# SmartCrop: Intelligent Crop Recommendation

## Theme: AgroTech

<p align="center">
   <img width="50%" src="https://user-images.githubusercontent.com/106915790/232244703-f44b3a75-1565-41ab-aab1-5fe4cb745383.jpg" />
</p>

The agriculture industry is one of the most significant contributors to the global economy, providing food, jobs, and income for millions of people. However, the sector has been facing numerous challenges that limit its productivity and profitability. One of the most significant challenges is inadequate knowledge of crop selection and management practices, leading to suboptimal yields and reduced profitability.

Crop recommendation using machine learning is a technological solution that seeks to address this challenge. The solution aims to leverage the power of machine learning algorithms to analyze and interpret data on various crops' requirements and growth conditions. With this data, the solution can make personalized recommendations to farmers on the crops that are best suited for their specific conditions, such as soil type, climate, and topography.

The solution works by collecting and analyzing data from various sources, such as satellite imagery, weather patterns, soil samples, and crop growth models. The data is fed into machine learning algorithms that can learn from the data and predict the best crops to grow in a particular location. The solution can also provide recommendations on the optimal planting time, seed variety, and irrigation practices to achieve maximum yield.

Several machine learning algorithms can be used to implement this solution, including decision trees, neural networks, support vector machines, and random forests. These algorithms can be trained using historical data on crop yields, soil and weather conditions, and other relevant parameters to make accurate predictions.

One of the critical benefits of this solution is that it enables farmers to make data-driven decisions on crop selection and management practices. With personalized recommendations based on their specific conditions, farmers can optimize their yields and maximize profitability. The solution can also help reduce the environmental impact of agriculture by promoting sustainable farming practices that reduce waste and improve soil health.

This application will assist farmers in increasing agricultural productivity, preventing soil degradation in cultivated land, reducing chemical use in crop production, and maximizing water resource efficiency.

There are various technologies used in implementing crop recommendation using machine learning, such as remote sensing, geographic information systems (GIS), and cloud computing. Remote sensing technologies, such as satellite imagery, can provide valuable data on crop growth patterns, soil moisture levels, and other environmental factors. GIS technology can help in mapping soil types, land use, and other geographical features that affect crop growth. Cloud computing technologies can be used to store and process vast amounts of data, making it accessible to farmers in real-time.

In conclusion, crop recommendation using machine learning is a powerful solution that can revolutionize the agriculture industry. By leveraging the power of machine learning algorithms and advanced technologies, the solution can provide personalized recommendations to farmers on the best crops to grow in their specific conditions. This can help optimize yields, improve profitability, and promote sustainable farming practices.

# [Use of Google Cloud Services and AMD Instance]()
SmartCrop is hosted on the Google Cloud platform, which provides a robust and scalable infrastructure for data storage and processing. To ensure fast and efficient processing of large datasets, SmartCrop utilizes AMD instances on Google Cloud. AMD instances provide high-performance computing capabilities, allowing SmartCrop to process vast amounts of data in real-time. With SmartCrop on Google Cloud with AMD instances, farmers can make data-driven decisions on crop selection and management practices, leading to optimized yields and improved profitability.

# [Dataset]()
This dataset was build by augmenting datasets of rainfall, climate and fertilizer data available for India.

### [Attributes information:]()

* **N** - Ratio of Nitrogen content in soil
* **P** - Ratio of Phosphorous content in soil
* **K** - Ratio of Potassium content in soil
* **Temperature** -  temperature in degree Celsius
* **Humidity** - relative humidity in %
* **ph** - ph value of the soil
* **Rainfall** - rainfall in mm 

### [Experiment Results:]()
* **Data Analysis**
    * All columns contain outliers except for N.
 * **Performance Evaluation**
    * Splitting the dataset by 80 % for training set and 20 % validation set.
 * **Training and Validation**
    * GausianNB gets a higher accuracy score than other classification models.
    * GaussianNB ( 99 % accuracy score )
 * **Performance Results**
    * Training Score: 99.5%
    * Validation Score: 99.3%

# Demo
**Live Demo:** http://34.82.65.249:6620/ or https://smartcrop.mrayush.me

**Video Demo:**


https://user-images.githubusercontent.com/106915790/232326623-c265ab62-9497-485d-9aee-741309536b0b.mp4


# References
* https://www.prolim.com/crop-recommendation-system-using-machine-learning-for-digital-farming/
* https://www.irjet.net/archives/V4/i12/IRJET-V4I12179.pdf
* https://ieeexplore.ieee.org/document/8768790
* http://sersc.org/journals/index.php/IJAST/article/view/30399
* https://www.researchgate.net/publication/345247916_Crop_Plantation_Recommendation_using_Feature_Extraction_and_Machine_Learning_Techniques
* https://towardsdatascience.com/farmeasy-crop-recommendation-portal-for-farmers-48a8809b421c
* https://www.kaggle.com/atharvaingle/crop-recommendation-dataset
* http://agri.ckcest.cn/ass/8185d605-6c4d-4d8a-b280-c867c2304d42.pdf
