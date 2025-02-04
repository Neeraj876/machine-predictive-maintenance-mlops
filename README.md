<div align="center">
    <h1>MLOps Solution for Machine Predictive Maintenance Classification</h1>
</div>

## 📚 Table of Contents
1. [Problem Statement](#-problem-statement)
2. [Goals Achieved](#-goals-achieved)
3. [Project Methodology](#%EF%B8%8F-project-methodology)
   - [Data Ingestion](#data-ingestion)
   - [Data Validation](#data-validation)
   - [Data Transformation](#data-transformation)
   - [Model Building & Testing](#model-building--testing)
   - [Deployment Pipeline](#deployment-pipeline)
4. [Contribution](#-contribution)
5. [Project Outro](#-project-outro)

## 🚩 Problem Statement
The web is filled with malicious traffic which leads to numerous kinds of phishing attempts. This project aims to understand and detect phishing attempts in network traffic using various machine learning algorithms. By leveraging various data processing and modeling strategies, this project provides a robust solution for identifying malicious URLs and enhancing network security.

## 🎯 Goals Achieved
- Developed a comprehensive pipeline for data ingestion, validation, transformation, and model training.
- Implemented a machine learning model capable of predicting phishing attempts with high accuracy.
- Established a deployment pipeline to facilitate easy integration and continuous delivery of the model.

## 🛠️ Project Methodology
### Data Ingestion
The project begins with data ingestion, where data is collected from a MongoDB database. The data is then exported into a structured format for further processing.
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/8eaa17e2-1359-4828-a4fd-3d5908dc44aa">

### Data Validation
Once the data is ingested, it undergoes validation to ensure its quality and integrity. This step checks for missing values, schema conformity, and potential dataset drift.
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/842306b2-8aff-4a69-9f0e-785316f33956">

### Data Transformation
After validation, the data is transformed to prepare it for modeling. This includes handling missing values, feature scaling, and encoding categorical variables.
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/4fe65518-b248-4297-ba97-e94679d1e22c">

### Model Building & Testing
The core of the project involves building and testing various machine learning models. The best-performing model is selected based on evaluation metrics such as accuracy, precision, and recall.
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/d5d7bd50-0590-45d8-a864-2fe01c314d5f">

### Deployment Pipeline
Finally, the trained model is deployed using FastAPI, allowing users to make predictions through a web interface. The deployment pipeline ensures that the model can be updated seamlessly as new data becomes available.
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/6369e6e6-65c3-4a1e-965e-f2cc2252db08">

