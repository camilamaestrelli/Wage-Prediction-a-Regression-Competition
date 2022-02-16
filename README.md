# Wage Prediction: A Regression Competition

***
This DS project is a result of the 7th [FLAI](https://www.flai.com.br/) Machine Learning Competition. 
The aim of the contest was to build a model that predicts wage with the smallest mean absolute error. 

This model won 1st place in the Competition.

For a better understanding, this was divided in 3 parts: Data Analysis, Machine Learning Algorithm and Deploy. The last one was not part of the competition but a way to practise the last DS step.

Note: Although the code cells are in english, the explanation and result interpretations (markdown cells) are in portuguese.

---

1. Exploratory Data Analysis: [EDA]()

At this stage, the goal was to understand the datasets.


2. ML: [Algorithm]()

Following the EDA, a pre-processing was carried out. For this, a randomized search over all the possible transformations (that I could think of at the time) was implemented. 

The last 5 submissions (of a total of 10) used the transformations chosen by this method. 

Thereafter, randomized searches were carried out for a hyperparametrization. 

Finally, a voting regressor using the best models was the one employed to predict the wage.

3. Streamlit model deploy: [Deploy](https://share.streamlit.io/camilamaestrelli/wage-prediction-a-regression-competition/deploy_streamlit_wage_prediction.py)

In this final step, joblib was used to save the model. And then, streamlit for the interface. 

Note: Despite the fact that the EDA found some duplicated data, the deploy did not take this into account as well as the 'clustering'
