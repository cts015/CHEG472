# pest_disease_prediction
A machine learning model to predict agricultural pests and diseases

First read sample data from xls or csv file.
Then, perform exploratory data analysis (EDA) of sample data.
EDA includes removing duplicates, filling missing values with the mean for the column, and normalization/standardization if necessary.
The app will then categorize the data into targets and features.
Cross-validation should be performed. This entails:
  Perform test-train splits at varying percentages.
  Train multiple machine learning models on the training data and validate performance of each model with the testing data.
  Assess the performance of each model by analyzing R2, mean average error (MAE), and mean squared error (MSE).
Once the best model is selected based on R2, MAE, MSE perform a test-train split and train then test the model.
Code for Gradio GUI and copy files to huggingface.
