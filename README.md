# Crop Yield Prediction for Smart Agriculture

## Project Topic
Predicting crop yield using remote sensing and environmental variables to support data-driven agricultural planning, yield estimation, and farm management decisions.

## Problem Statement
Agriculture is a critical sector in Kenya and many developing economies, yet farmers and agricultural stakeholders often face uncertainty in forecasting harvest output. Traditional yield estimation methods are usually manual, time-consuming, and dependent on limited field observations. This creates challenges in planning for food security, input allocation, pricing, storage, and risk management.

The lack of reliable, timely, and scalable yield prediction tools makes it difficult for farmers, agribusinesses, and policymakers to anticipate production levels before harvest. This project addresses that challenge by building a machine learning model that estimates crop yield using satellite-derived vegetation indices, soil, and weather-related features.

## Project Motivation
Accurate crop yield prediction can help:
- farmers make informed planting and management decisions
- agricultural extension services target support more efficiently
- agribusiness companies forecast supply and demand
- policymakers improve food security planning
- researchers analyze climate and land productivity relationships

With increasing climate variability and pressure on food systems, predictive analytics offers a practical solution for more resilient agriculture.

## Objectives
The main objectives of this project are to:
1. Analyze crop yield data and identify the most relevant agronomic features.
2. Build a predictive model that estimates crop yield from field and environmental indicators.
3. Engineer meaningful variables such as vegetation and soil interactions to improve model performance.
4. Develop a user-friendly web application for demonstration and practical use.
5. Present the findings in a clear and interpretable way for stakeholders and academic evaluation.

## Scope
This project focuses on crop yield prediction for agricultural fields using variables such as:
- latitude and longitude
- NDVI, GNDVI, NDWI, and SAVI
- soil moisture
- temperature
- rainfall
- crop type

The project uses historical field-level data and a machine learning model to estimate expected yield.

## Dataset Description
The dataset used in this project contains agricultural field observations with the following key features:

- field_id: unique field identifier
- date_of_image: date of the observation
- latitude, longitude: geographical location of the field
- NDVI: Normalized Difference Vegetation Index
- GNDVI: Green Normalized Difference Vegetation Index
- NDWI: Normalized Difference Water Index
- SAVI: Soil-Adjusted Vegetation Index
- soil_moisture: soil moisture level
- temperature: field or climatic temperature
- rainfall: precipitation value
- crop_type: type of crop grown
- yield: target variable representing crop output

## Business and Research Value
This project combines data science, remote sensing, and agricultural analytics to solve a real-world production problem. It demonstrates how machine learning can convert environmental and field data into actionable insights for yield forecasting.

## Data Preprocessing
The preprocessing pipeline includes:
- loading the agricultural dataset
- removing unnecessary columns
- converting data types where necessary
- handling missing values
- creating interaction features such as:
  - NDVI_temp = NDVI × temperature
  - NDVI_rainfall = NDVI × rainfall
  - SAVI_soil_moisture = SAVI × soil moisture
- encoding crop type values for model compatibility
- scaling numerical features using StandardScaler

## Feature Engineering
Feature engineering is an important part of this project because crop productivity is influenced by multiple interacting factors. For example:
- vegetation strength combined with temperature can reflect plant stress and growing conditions
- rainfall and vegetation interaction can indicate crop vigor or moisture availability
- soil moisture and vegetation index interaction can represent crop water status

These engineered features improve the model’s ability to relate environmental conditions to yield outcomes.

## Model Selection
A Random Forest Regressor was selected because it is robust, handles nonlinear relationships well, and performs strongly on tabular agricultural data. It can model complex interactions among environmental variables without requiring heavy feature assumptions.

## Model Workflow
The workflow for this project is:
1. Load the dataset
2. Explore variables and relationships
3. Clean and prepare data
4. Engineer interaction features
5. Encode categorical variables
6. Scale numerical features
7. Split data into train and test sets
8. Train the Random Forest model
9. Evaluate performance using regression metrics
10. Deploy the model in a simple web interface for predictions

## Evaluation Metric
The project evaluates the model using the R² score, which measures how well the model explains variability in crop yield.

### Current model performance
- R² Score: 0.9336
- Dataset rows used: 1625

This indicates that the model explains approximately 93.36% of the variation in yield based on the selected features, which is a strong result for this project.

## Web Application
A simple Flask web app was created to make the prediction model usable for demonstration and presentation. The interface allows users to input field conditions and get a predicted yield value instantly.

### App features
- user-friendly form for field inputs
- real-time yield prediction
- model summary section
- clean dashboard-style interface

## Project Structure
```text
Data-Science-Capstone-Project---Inceptor-Kenya/
├── app.py                      # Flask application and model logic
├── requirements.txt            # Python dependencies
├── yield_prediction_dataset.csv # Agricultural dataset
├── crop-yield-prediction-notebook.ipynb  # Notebook workflow
├── templates/
│   └── index.html              # Web form layout
├── static/
│   └── styles.css              # App styling
├── README.md                   # Project documentation
└── .venv/                      # Virtual environment (local only)
```

## How to Run the Project
### 1. Create a virtual environment
```bash
python3 -m venv .venv
```

### 2. Activate the environment
```bash
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the app
```bash
python app.py
```

### 5. Open in a browser
```text
http://localhost:5000
```

## Presentation Summary
This project demonstrates the application of machine learning in agriculture by predicting crop yield using real field and environmental data. It addresses a practical problem facing agricultural stakeholders and shows how predictive analytics can support better decision-making.

The solution combines data science, feature engineering, machine learning, and deployment into an easy-to-use web application. This makes it suitable for academic presentation, capstone defense, and demonstration to stakeholders interested in smart agriculture and digital farming solutions.

## Key Takeaways
- machine learning can improve yield forecasting in agriculture
- vegetation and weather features are highly informative for production prediction
- feature engineering significantly improves model understanding
- a deployable web app makes the project more practical and impactful

## Future Improvements
Potential enhancements for future development include:
- integrating real-time weather and satellite data APIs
- testing additional algorithms such as XGBoost and Gradient Boosting
- comparing multiple crop types with separate models
- adding model explainability for stakeholder understanding
- extending the app to support broader farm management decision support

## Conclusion
This capstone project shows how data-driven insight can be used to address a real agricultural challenge. By predicting crop yield from environmental and field indicators, the system provides a valuable tool for farmers, agribusinesses, and decision-makers aiming to improve productivity and planning.
