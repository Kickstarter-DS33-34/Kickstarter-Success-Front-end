import pandas as pd

# This function inputs a dictionary of
# key-value pairs provided from the form
# in the 'prediction' route of app.py.
# It ouputs a dataframe to be used
# in the final prediction function.
def transform(data_dict):
    transformed_data = {}
    for key, value in data_dict.items():
        transformed_data[key] = [value]
    transformed_df = pd.DataFrame.from_dict(transformed_data)
    return transformed_df