##############################################################################################################################################
# The Purpose of this file is to load the dataset (telco_churn_data.csv) which was acquired from Kaggle to then understand and clean the data
##############################################################################################################################################

##############################################################################################################################################
# LOAD THE DATASET

import pandas as pd

# CSV file has been loaded to PAIWP_ASSIGNMENT GitHub repository

file_path = '/workspaces/PAIWP_ASSIGNMENT/telco_churn_data.csv'
df = pd.read_csv(file_path)
##############################################################################################################################################

##############################################################################################################################################
# ANALYSIS OF THE DATASET

# df.shape - How many rows and columns does the dataset have? -- I have also used this function to test if the file has been loaded successfully
df_shape=df.shape

file_name_shape = "df_shape_output.txt"

with open(file_name_shape,'w') as file:
    file.write(f"Number of rows: {df_shape[0]}\n")
    file.write(f"Number of columns: {df_shape[1]}\n")

# df.info - Print a summary of the Dataset to identify the data type of each column and non-null values -- This will assist with identifying which columns need to be cleaned
from io import StringIO

buffer=StringIO()
df.info(buf=buffer)
info_str=buffer.getvalue()

file_name_info='df_info_output.txt'

with open(file_name_info,'w') as f:
    f.write(info_str)

# df.head - What does a small sample of the data look like? -- I have also used this function to test if the file has been loaded successfully
df_head_str=df.head(10).to_string(index=False)

file_path="df_head_output.txt"
with open(file_path, 'w') as f:
    f.write(df_head_str)
##############################################################################################################################################