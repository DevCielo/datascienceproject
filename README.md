# Wine Quality Prediction - End-to-End Data Science Project

This project is an end-to-end data science pipeline built to predict wine quality using machine learning. The project integrates a Flask web application for user interaction, along with MLflow and DagsHub for experiment tracking and model management.

## **Project Overview**

The goal of this project is to predict the quality of wine based on its physicochemical attributes. The machine learning pipeline includes data ingestion, validation, transformation, model training, evaluation, and deployment. The project is integrated with MLflow and DagsHub for tracking experiments and versioning.

---

## **Workflows**

### **1. Machine Learning Pipeline**

1. **Data Ingestion**:
   - Loads data from source files (CSV format).
   - Saves the raw data into the project directory.

2. **Data Validation**:
   - Validates the schema of the dataset to ensure consistency.
   - Checks for missing values, incorrect column names, or invalid data types.

3. **Data Transformation**:
   - Handles feature engineering and data preprocessing.
   - *Note*: No additional transformations were needed in this dataset as there were no missing values.

4. **Model Trainer**:
   - Trains a machine learning model on the dataset.
   - Saves the trained model for deployment.

5. **Model Evaluation**:
   - Uses metrics like RMSE, MAE, and R² to evaluate the model.
   - Logs metrics and artifacts into **MLflow** for tracking.
   - Integrates with **DagsHub** for remote experiment tracking.

6. **Flask Application**:
   - Provides a user-friendly interface to input wine attributes and predict quality.

---

### **2. Configuration Workflow**

1. Update `config.yaml`: Configuration for file paths, dataset URLs, and settings.
2. Update `schema.yaml`: Schema definitions for data validation.
3. Update `params.yaml`: Hyperparameter tuning and model-specific parameters.
4. Update the Entity: Create structured data entities for consistent handling.
5. Update the Configuration Manager in `src/config`: Centralized management for all configurations.
6. Update the Components: Modify or add new components for the ML pipeline.
7. Update the Pipeline: Integrate components into a unified pipeline.
8. Update `main.py`: The entry point to trigger the ML pipeline or Flask app.

---

## **Technologies Used**

- **Programming Language**: Python
- **Frameworks**: Flask, Scikit-learn, Jupyter Notebook
- **Experiment Tracking**: MLflow, DagsHub
- **Data Handling**: Pandas, NumPy
- **Version Control**: Git, GitHub
- **Environment Management**: Virtualenv

---

