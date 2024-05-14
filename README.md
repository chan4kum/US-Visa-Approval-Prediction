# US Visa Prediction Project

## Life Cycle of Machine Learning Project

### Understanding the Problem Statement**
1. **Data Collection**
2. **Exploratory Data Analysis**
3. **Data Cleaning**
4. **Data Pre-Processing**
5. **Model Training**
6. **Choosing the Best Model**

### About

The US Visa Prediction Project aims to streamline the visa application process by leveraging machine learning algorithms to predict the outcome of visa applications. This project is essential for both employers and applicants, providing insights into the likelihood of visa approval based on historical data.

#### Problem Statement

The Office of Foreign Labor Certification (OFLC) receives numerous job certification applications from employers seeking to hire foreign workers. With the increasing volume of applications, there is a need for efficient and accurate screening processes. The US Visa Prediction Project addresses this need by developing classification models to assess the probability of visa approval for each application.

**Objectives of the Project:**

1. To predict the outcome of visa applications (certified or denied) based on historical data.
2. To identify key factors influencing visa approval decisions.
3. To provide recommendations for improving the visa application process.

### Data Collection

The dataset used in this project is sourced from Kaggle, consisting of 25,480 rows and 12 columns. It includes various features such as employment details, education background, and geographical information.

[Dataset Source: Kaggle - Easy Visa Dataset](https://www.kaggle.com/datasets/moro23/easyvisa-dataset)

### Exploring Data

The exploratory data analysis (EDA) phase involves analyzing numerical and categorical features to gain insights into the data. Key steps include identifying outliers, handling missing values, and visualizing data distributions.

### Final Report

- **Data Preprocessing:** 
  1. Dropping irrelevant columns (`case_id`).
  2. Handling outliers in `no_of_employees` and `prevailing_wage` columns.
  3. Combining low-count categories in the `continent` column.

- **Model Training:** 
  1. Utilizing machine learning algorithms to train classification models.
  2. Evaluating model performance and selecting the best-performing model.

