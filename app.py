import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Forest Cover Type Predictor", layout="wide")
st.title("🌲 Forest Cover Type Prediction")

# =========================
# Load model and features
# =========================
model = joblib.load("rf_model.pkl")              # Your retrained RandomForest
features = joblib.load("model_features.pkl")    # List of 14 features used in training

# =========================
# User input form
# =========================
st.subheader("Enter feature values:")

col1, col2 = st.columns(2)

with col1:
    elevation = st.text_input("Elevation", "3000")
    h_dist_road = st.text_input("Horizontal Distance To Roadways", "2500")
    soil_type = st.text_input("Soil Type (1-40)", "5")
    h_dist_fire = st.text_input("Horizontal Distance To Fire Points", "1200")
    h_dist_hydro = st.text_input("Horizontal Distance To Hydrology", "100")
    v_dist_hydro = st.text_input("Vertical Distance To Hydrology", "30")
with col2:
    aspect = st.text_input("Aspect", "180")
    hill_noon = st.text_input("Hillshade Noon", "220")
    hill_9am = st.text_input("Hillshade 9am", "200")
    hill_3pm = st.text_input("Hillshade 3pm", "150")
    slope = st.text_input("Slope", "12")

# =========================
# Convert inputs to numeric
# =========================
try:
    input_dict = {
        "Elevation": float(elevation),
        "Horizontal_Distance_To_Roadways": float(h_dist_road),
        "Soil_Type": int(soil_type),
        "Horizontal_Distance_To_Fire_Points": float(h_dist_fire),
        "Horizontal_Distance_To_Hydrology": float(h_dist_hydro),
        "Hydrology_Roadway_Ratio": float(h_dist_hydro)/(float(h_dist_road)+1),
        "Vertical_Distance_To_Hydrology": float(v_dist_hydro),
        "Aspect": float(aspect),
        "Hillshade_Noon": float(hill_noon),
        "Hillshade_Diff_Noon_3pm": float(hill_noon) - float(hill_3pm),
        "Hillshade_9am": float(hill_9am),
        "Hillshade_3pm": float(hill_3pm),
        "Hillshade_Diff_9am_Noon": float(hill_9am) - float(hill_noon),
        "Slope": float(slope)
    }
except ValueError:
    st.error("⚠️ Please enter valid numeric values")
    st.stop()

input_data = pd.DataFrame([input_dict])

# =========================
# Align input columns with training features
# =========================
for col in features:
    if col not in input_data.columns:
        input_data[col] = 0
extra_cols = [c for c in input_data.columns if c not in features]
if extra_cols:
    input_data.drop(columns=extra_cols, inplace=True)
input_data = input_data[features]

# =========================
# Predict button
# =========================
if st.button("Predict Forest Cover Type"):
    prediction = model.predict(input_data)[0]  # Works whether output is string or number

    # If prediction is numeric, map to forest name
    cover_names = {
        1: "Spruce/Fir",
        2: "Lodgepole Pine",
        3: "Ponderosa Pine",
        4: "Cottonwood/Willow",
        5: "Aspen",
        6: "Douglas-fir",
        7: "Krummholz"
    }

    if isinstance(prediction, (int, np.integer)):
        prediction_name = cover_names.get(int(prediction), "Unknown")
    else:
        prediction_name = str(prediction)

    st.success(f"🌲 Predicted Forest Cover Type: {prediction_name}")

    # =========================
    # Show probability bar chart if available
    # =========================
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_data)[0]
        st.subheader("Prediction Probabilities")
        proba_df = pd.DataFrame({
            "Forest Type": list(cover_names.values()),
            "Probability": proba
        })
        st.bar_chart(proba_df.set_index("Forest Type"))