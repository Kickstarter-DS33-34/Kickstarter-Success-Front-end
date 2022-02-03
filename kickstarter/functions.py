import pandas as pd
# import tensorflow as tf


# Function that inputs the form data from the
# 'prediction.html' route and outputs a
# dictionary of tensors usable by our model.
def transform(data_dict):
    # Create empty dictionary
    transformed_data = {}
    for key, value in data_dict.items():
        # If the dictionary key is project_name 
        # or description, return the length of the input.
        if key == 'project_name' or key =='description':
            transformed_data[key] = [len(value)]
        # If the dictionary key is launch_month, 
        # days_of_campaign, or goal, convert the inputted
        # string into an integer.
        elif key == 'launch_month' or key == 'days_of_campaign' or key == 'goal':
            transformed_data[key] = [int(value)]
        # The rest are already integers so 
        # just assign.
        else:
            transformed_data[key] = [value]
    # Convert the dictionary values to tensors
    # input_dict = {name: tf.convert_to_tensor([value]) for name, value in transformed_data.items()}
    input_dict = transformed_data
    return input_dict