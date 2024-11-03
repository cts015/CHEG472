import subprocess
import sys

# Force install scikit-learn if not found
try:
    import sklearn
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scikit-learn"])
    import sklearn  # Import again after installation

import gradio as gr
import pandas as pd
import pickle

# Load the pre-trained model
with open('best_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the label encoder
with open('label_encoder.pkl', 'rb') as label_encoder_file:
    label_encoder = pickle.load(label_encoder_file)

def predict_coffee_type(time_of_day, coffee_strength, sweetness_level, milk_type, coffee_temperature, flavored_coffee, caffeine_tolerance, coffee_bean, coffee_size, dietary_preferences):
    # Creating input DataFrame for the model
    input_data = pd.DataFrame({
        'Token_0': [time_of_day],
        'Token_1': [coffee_strength],
        'Token_2': [sweetness_level],
        'Token_3': [milk_type],
        'Token_4': [coffee_temperature],
        'Token_5': [flavored_coffee],
        'Token_6': [caffeine_tolerance],
        'Token_7': [coffee_bean],
        'Token_8': [coffee_size],
        'Token_9': [dietary_preferences]
    })

    # One-hot encode the input data (ensure it matches the training data)
    input_encoded = pd.get_dummies(input_data)

    # Align columns with the training data (required columns)
    required_columns = model.feature_names_in_  # Get the feature columns from the model
    for col in required_columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[required_columns]

    # Make the prediction
    prediction = model.predict(input_encoded)[0]

    # Reverse the label encoding (map the prediction back to the coffee type)
    coffee_type = label_encoder.inverse_transform([prediction])[0]

    return coffee_type

# Gradio Interface using components
interface = gr.Interface(
    fn=predict_coffee_type,
    inputs=[
        gr.Dropdown(['morning', 'afternoon', 'evening'], label="Time of Day"),
        gr.Dropdown(['mild', 'regular', 'strong'], label="Coffee Strength"),
        gr.Dropdown(['unsweetened', 'lightly sweetened', 'sweet'], label="Sweetness Level"),
        gr.Dropdown(['none', 'regular', 'skim', 'almond'], label="Milk Type"),
        gr.Dropdown(['hot', 'iced', 'cold brew'], label="Coffee Temperature"),
        gr.Dropdown(['yes', 'no'], label="Flavored Coffee"),
        gr.Dropdown(['low', 'medium', 'high'], label="Caffeine Tolerance"),
        gr.Dropdown(['Arabica', 'Robusta', 'blend'], label="Coffee Bean"),
        gr.Dropdown(['small', 'medium', 'large'], label="Coffee Size"),
        gr.Dropdown(['none', 'vegan', 'lactose-intolerant'], label="Dietary Preferences")
    ],
    outputs=gr.Textbox(label="Recommended Coffee Type"),
    title="Coffee Type Recommendation"
)

if __name__ == "__main__":
    interface.launch()
