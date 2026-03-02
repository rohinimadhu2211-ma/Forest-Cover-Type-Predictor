# Forest-Cover-Type-Predictor
Predict forest cover type interactively with Random Forest and 14 key environmental features
🌲 Forest Cover Type Prediction
Project Summary:
This project predicts the forest cover type based on environmental and geographic features using a Random Forest classifier. A Streamlit app allows users to input feature values and view predictions along with probability charts for all 7 forest types.
Objective
Predict forest cover type accurately using environmental features.
Build an interactive, user-friendly Streamlit web app.
Visualize prediction probabilities for all forest classes.
Handle derived features and feature alignment for consistent predictions.
Libraries Used
pandas, numpy — data handling
scikit-learn — modeling and evaluation
imblearn — handling class imbalance
joblib — model saving/loading
streamlit — web application
matplotlib, seaborn — visualization (optional for EDA)
Dataset
Source: UCI Forest CoverType Dataset
Features: Original 54, selected 14 key features
Target: Cover_Type (7 classes)
Spruce/Fir
Lodgepole Pine
Ponderosa Pine
Cottonwood/Willow
Aspen
Douglas-fir
Krummholz
Sample size: ~120,000 rows
Key Features Used
Elevation, Slope, Aspect
Soil_Type, Horizontal/Vertical Distances
Hillshade values (9am, Noon, 3pm)
Derived: Hillshade differences, Hydrology-Roadway ratio
Data Preprocessing
Checked missing values & duplicates — none found
Computed derived features for better prediction
Handled outliers using IQR
Corrected skewed numeric columns (optional)
Feature Engineering
Selected 14 numeric features for modeling
Encoded categorical variables as numeric
Saved feature list using joblib for Streamlit input alignment
Exploratory Data Analysis (EDA)
Visualized feature distributions with histograms and boxplots
Checked correlation between features
Identified class imbalance (majority class: Lodgepole Pine)
Handling Class Imbalance
Used RandomOverSampler to balance training data
Prevented over-prediction of majority class
Model Building
Tried multiple classifiers: Random Forest, Decision Tree, Logistic Regression, KNN, XGBoost
Evaluated using Accuracy, Confusion Matrix, Classification Report
Random Forest selected as final model
Hyperparameter Tuning
Optimized n_estimators, max_depth, max_features with RandomizedSearchCV
Final model: RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
Model Saving
Python

joblib.dump(rf, "rf_model.pkl")
joblib.dump(X_train_res.columns.tolist(), "model_features.pkl")
Ensures Streamlit input features match training order
Streamlit Web App
Manual numeric input fields (no +/- arrows)
Computes derived features automatically
Aligns inputs with saved features
Predicts forest cover type and shows probabilities for all classes
Handles numeric/string output without errors
Challenges Faced
Class imbalance → solved with oversampling
Feature alignment → saved feature list and filled missing columns
Target variable mapping → numeric vs string handled correctly
Derived feature computation in Streamlit → consistent with training
How to Run
Clone repository:

git clone https://github.com/YourUsername/forest_cover_app.git
cd forest_cover_app
Install dependencies:


pip install -r requirements.txt
Run the app:


streamlit run app.py
Enter feature values → Click Predict Forest Cover Type → View prediction and probability chart
