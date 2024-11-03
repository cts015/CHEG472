# coffee_model
This app will use machine learning to reccomend a coffee drink based on the user's preferences.

Please view this readme in code mode.

First read sample data from xls or csv file.
Then, perform exploratory data analysis (EDA) of sample data. EDA includes:
  Removing duplicates
  Filling missing values with the mean for the column
  Normalization/standardization if necessary.
The app will then categorize the data into targets and features.
Use pickle in another coffee_exercise.ipynb to encode the target categorical labels and create label_encoder.pkl.
Perform a test-train split
Test multiple machine learning models and assess them by root mean squared error.
Once the best model is selected based on RMSE, create a pickle file best_model.pkl to encode for the best model of those tested.
Code for Gradio GUI and copy app.py, requirements.txt, best_model.pkl, and label_encoder.pkl to a huggingface space with gradio.
