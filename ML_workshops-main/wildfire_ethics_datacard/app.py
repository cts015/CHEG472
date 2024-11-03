import gradio as gr

# Ethics DataCard content for forest wildfire prediction model
datacard_content = """
# Ethics DataCard for Forest Wildfire Prediction Model

## Dataset Overview
- **Input Variables**: Temperature, Humidity, Wind Speed, Rainfall, Fuel Moisture, Vegetation Type, Slope, Region
- **Output Variables**: Fire Size, Fire Duration, Suppression Cost, Fire Occurrence

## Data Collection Process
- Data is randomly generated, so there are no issues with obtaining or licensing of data and no personal, propietary, or private information is included.

## Bias Considerations
- The data is randomly generated, so it does not unfairly affect specific regions or communities.
- The data is not real, so it is not applicable to any real forest.

## Fairness & Justice
- The model is not predicting real wildfires, because it is being fed randomly generated data.

## Privacy and Security
- The data is randomly generated, so there are no privacy concerns.

## Sustainability and Environmental Impact
-The model will continuously be fed new data in order to adapt to environmental and climate fluctuation.

## Model Limitations
- We do not claim 100% accuracy, but strive to be as accurate as possible and will adjust the model if we have false positives or negatives.

## Accountability and Transparency
-All the code and data will be publicly available.

## Societal Impact
- The model is designed to protect both human lives and the environment by enabling better planning and response to wildfire threats.
- It has the potential to inform policy changes in land management, conservation, and emergency response strategies.
"""

# Function to display the DataCard
def display_datacard():
    return datacard_content

# Gradio interface to display the ethics DataCard
iface = gr.Interface(fn=display_datacard, inputs=[], outputs="markdown")

# Launch the Gradio interface
iface.launch()
