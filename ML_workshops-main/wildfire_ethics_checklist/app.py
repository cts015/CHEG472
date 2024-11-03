import gradio as gr

# Markdown content
md_content = """
# Ethics Checklist for Forest Wildfire Prediction Model

## 1. Data Collection
- **Input Variables**: Temperature, Humidity, Wind Speed, Rainfall, Fuel Moisture, Vegetation Type, Slope, Region
- **Output Variables**: Fire Size, Fire Duration, Suppression Cost, Fire Occurrence
- Are the data sources, such as weather, vegetation, and geographic data, properly licensed and legally available?
    - Data is randomly generated, so there are no issues with obtaining or licensing of data.
- Has any sensitive information, such as private property or personal location data, been anonymized?
    - The data is randomly generated, so no personal or private information is included.
- Have you obtained consent for data collected from private or proprietary sources, such as satellite imagery or drone footage?
    - The data is randomly generated, so no propietary or private information is included.

## 2. Fairness & Justice
- How will you ensure that the model’s predictions are fair and do not disproportionately affect specific regions or communities (e.g., indigenous lands, rural areas)?
    - The data is randomly generated, so it does not unfairly affect specific regions or communities.
- What biases might exist in the historical data (e.g., underreporting of fires in certain regions), and how will you address these to ensure the model does not unfairly target or neglect specific areas?
    - This data is not historic, so the model does not unfairly target specific areas.
- How will you balance fairness in handling both false positives (predicting a fire where there is none) and false negatives (failing to predict a fire)?
    - The model is not predicting real wildfires, because it is being fed randomly generated data.
- Have you tested the model across different regions to ensure consistent performance across various forest types (tropical, temperate, etc.)?
    - The data is not real, so it is not applicable to any real forest.

## 3. Transparency
- How will you ensure transparency about the data sources, algorithms, and decision-making process of the model?
    - All the code and data will be publicly available.
- What information will you make available to government agencies, the public, and environmental organizations?
    - All the code, data, and decision-making logic will be publicly available.
- How will you communicate the model’s predictions and limitations to decision-makers so that they understand the risks involved?
    - False negatives and postives and the accuracy of the model will be reported.
- How will you explain false positives and false negatives to the affected communities or stakeholders, especially during critical events like evacuations?
    - No model will be 100% accurate, but we will strive to continuously improve the accuracy of the model.

## 4. Privacy
- How will you ensure the privacy of individuals whose data might be inadvertently captured (e.g., campers, rural residents) through satellite images, drones, or weather stations?
    - The data is randomly generated, so there are no privacy concerns.
- What steps will you take to prevent the misuse of this data, especially in terms of tracking human activities in forest areas without their consent?
    - All human activity will be anonymized.
- If external data sources, such as drones or surveillance tools, are integrated into the model, how will you balance the need for accurate predictions with protecting individual privacy?
    - We will obtain consent any time private property is accessed and ensure anonimity.

## 5. Accountability
- Who will be held accountable if the model incorrectly predicts a wildfire, resulting in unnecessary evacuations or failure to prevent a disaster?
    - The makers of the app and those who collected the data, if it is not accurate.
- What system will you establish to monitor and adjust the model over time, ensuring it adapts to changing environmental and climate conditions?
    - The model will continuously be fed new data in order to adapt to environmental and climate fluctuation.
- How will you communicate accountability measures to the public, especially in high-risk areas where wildfire prediction is critical?
    - We do not claim 100% accuracy, but strive to be as accurate as possible and will adjust the model if we have false positives or negatives.

## 6. Inclusivity
- How will you ensure the model includes diverse data from different types of forests (e.g., tropical, temperate) and regions, especially those that may be underrepresented in historical data collection?
    - We will collect data from a wide range of forests and regions to increase representation of all communities.
- How will you ensure the model accounts for the needs of different communities, including vulnerable populations such as indigenous groups or rural residents who have unique relationships with the land?
    - We will strive to take input from rural and indigenous communities to adjust our model.
- If certain regions or communities lack sufficient data (e.g., underreporting, lack of resources), how will you address this to avoid biased predictions?
    - We will assign extra weight to data for areas that are traditionally underreported so as to increse their representation.


## 7. Sustainability
- How will the model’s predictions affect long-term forestry practices, land management, and firefighting strategies over time?
    - We will use the model's predictions to help reduce the risk of catastrophic forest fires through informed land management practices. 
- How will you ensure the model remains sustainable, considering the evolving nature of climate change and its effects on wildfire patterns?
    - The model will continuously be fed new data in order to adapt to environmental and climate fluctuation.
- What are the broader social and environmental implications if this model becomes widely adopted (e.g., impacts on land use, deforestation policies, wildlife conservation)?
    - It will help to reduce the risk of catastrophic forest fires through informed forestry and land management practices.
"""

def display_markdown():
    return md_content

# Create a Gradio interface
iface = gr.Interface(fn=display_markdown, inputs=[], outputs="markdown")
iface.launch()
