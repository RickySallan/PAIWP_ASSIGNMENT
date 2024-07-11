##############################################################################################################################################
# The Purpose of this file is to load the dataset (telco_churn_data.csv) which was acquired from Kaggle to then understand and clean the data
##############################################################################################################################################

##############################################################################################################################################
# 1. LOAD THE DATASET

import pandas as pd

# CSV file has been loaded to PAIWP_ASSIGNMENT GitHub repository

file_path = '/workspaces/PAIWP_ASSIGNMENT/1. Dataset/telco_churn_data.csv'
df = pd.read_csv(file_path)
##############################################################################################################################################

##############################################################################################################################################
# 2. ANALYSIS OF THE DATASET

import os

output_folder='/workspaces/PAIWP_ASSIGNMENT/2. Initial Data Analysis'

# df.shape - How many rows and columns does the dataset have? -- I have also used this function to test if the file has been loaded successfully
df_shape=df.shape

file_name_shape = "df_shape_output.txt"

full_file_path_shape=os.path.join(output_folder,file_name_shape)

with open(full_file_path_shape,'w') as file:
    file.write(f"Number of rows: {df_shape[0]}\n")
    file.write(f"Number of columns: {df_shape[1]}\n")

# df.info - Print a summary of the Dataset to identify the data type of each column and non-null values -- This will assist with identifying which columns need to be cleaned
from io import StringIO

buffer=StringIO()
df.info(buf=buffer)
info_str=buffer.getvalue()

file_name_info='df_info_output.txt'

full_file_path_info=os.path.join(output_folder,file_name_info)

with open(full_file_path_info,'w') as f:
    f.write(info_str)

# df.head - What does a small sample of the data look like? -- I have also used this function to test if the file has been loaded successfully
df_head_str=df.head(10).to_string(index=False)

file_path_head="df_head_output.txt"

full_file_path_head=os.path.join(output_folder,file_path_head)

with open(full_file_path_head, 'w') as f:
    f.write(df_head_str)
##############################################################################################################################################