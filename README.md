<div align="center">
    <h1>MLOps Solution for Machine Predictive Maintenance</h1>
    ![Project Architecture](_assets/architecture.gif)
</div>

## Table of Contents
1. [Problem Statement](#-problem-statement)
2. [Goals Achieved](#-goals-achieved)
3. [Project Methodology](#%EF%B8%8F-project-methodology)
   - [Data Ingestion](#data-ingestion)
   - [Data Validation](#data-validation)
   - [Data Transformation](#data-transformation)
   - [Model Building & Testing](#model-building--testing)
   - [Deployment Pipeline](#deployment-pipeline)

## Problem Statement
This project performs machine predictive maintenance by classifying whether a machine will fail or not, and if a failure occurs, predicting the type of failure, such as Heat Dissipation Failure, Power Failure, Overstrain Failure, Tool Wear Failure, Random Failures, or No Failure if the machine does not fail. It helps businesses anticipate maintenance needs, optimize operations, and improve overall efficiency.

## Features
Key features in the dataset include:
| **Feature Name**           | **Description**                                                                 |
|----------------------------|-------------------------------------------------------------------------------|
| `UDI`                      | unique identifier ranging from 1 to 10000.                      |
| `Product ID`               | A unique identifier for each product, consisting of a letter (L, M, H) for quality (Low, Medium, High) followed by a serial number. |
| `type`                     | consisting of a letter L, M, or H for low (50% of all products), medium (30%), and high (20%) as product quality variants and a variant-specific serial number. |
| `air temperature`          | generated using a random walk process later normalized to a standard deviation of 2 K around 300 K. |
| `process temperature`      | generated using a random walk process normalized to a standard deviation of 1 K, added to the air temperature plus 10 K.               |
| `rotational speed`         | calculated from power of 2860 W, overlaid with a normally distributed noise.                         |
| `torque`              | torque values are normally distributed around 40 Nm with an Ïƒ = 10 Nm and no negative values.                          |
| `tool wear`          | The quality variants H/M/L add 5/3/2 minutes of tool wear to the used tool in the process.       |
| `Failure Type`             | 'machine failure' label that indicates, whether the machine has failed in this particular data point for any of the following failure modes are true.                                      |
| `Target`                   | Failure or Not.                                           |


## 🎯 Goals Achieved
- Developed a comprehensive pipeline for data ingestion, validation, transformation, and model training.
- Implemented a machine learning model capable of predicting machine failure and the type of failure with high accuracy.
- Established a deployment pipeline to facilitate continuous integration and continuous delivery/deployment of the model.

## 🛠️ Project Methodology
### Data Ingestion
The project begins with data ingestion, where data is collected from a MongoDB database. The data is then exported into a structured format for further processing.
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/8eaa17e2-1359-4828-a4fd-3d5908dc44aa">

### Data Validation
Once the data is ingested, it undergoes validation to ensure its quality and integrity. This step checks for schema conformity, and potential dataset drift.
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/842306b2-8aff-4a69-9f0e-785316f33956">

### Data Transformation
After validation, the data is transformed to prepare it for modeling. This includes handling missing values, feature scaling, and encoding categorical variables.
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/4fe65518-b248-4297-ba97-e94679d1e22c">

### Model Building & Testing
The core of the project involves building and testing various machine learning models. The best-performing model is selected based on evaluation metrics such as f1-score.
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/d5d7bd50-0590-45d8-a864-2fe01c314d5f">

### Deployment Pipeline
Finally, the trained model is deployed using FastAPI, allowing users to make predictions through a web interface. The deployment pipeline ensures that the model can be updated seamlessly as new data becomes available.
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/6369e6e6-65c3-4a1e-965e-f2cc2252db08">

