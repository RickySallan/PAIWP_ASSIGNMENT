#############################################################################################################################################
# The Purpose of this file is to clean dataset (telco_churn_data.csv) and omit all fields which are not required for the ML Model.

##############################################################################################################################################

##############################################################################################################################################
# 1. LOAD THE DATASET

import pandas as pd

# CSV file has been loaded to PAIWP_ASSIGNMENT GitHub repository

file_path = '/workspaces/PAIWP_ASSIGNMENT/1. Dataset/telco_churn_data.csv'
df = pd.read_csv(file_path)
##############################################################################################################################################

##############################################################################################################################################
# 2. REMOVE UNNECESSARY COLUMNS - For the purposes of the ML Model to predict churn the only variables to be considered are "Tenure in Months", "Contract", "Churn Value", "Total Customer Svc Requests", "Product/Service Issues Reported" and "Customer Satisfaction". All other fields can be removed.

columns_to_drop = ['Customer ID','Referred a Friend','Number of Referrals','Offer','Phone Service','Avg Monthly Long Distance Charges','Multiple Lines','Internet Service','Internet Type','Avg Monthly GB Download','Online Security','Online Backup','Device Protection Plan','Premium Tech Support','Streaming TV','Streaming Movies','Streaming Music','Unlimited Data','Paperless Billing','Payment Method','Monthly Charge','Total Regular Charges','Total Refunds','Total Extra Data Charges','Total Long Distance Charges','Gender','Age','Under 30','Senior Citizen','Married','Dependents','Number of Dependents','City','Zip Code','Latitude','Longitude','Population','CLTV','Churn Category','Churn Reason']

df_cleaned=df.drop(columns=columns_to_drop)
##############################################################################################################################################

##############################################################################################################################################
# 3. CHECK IF UNNECESSARY COLUMNS HAVE SUCCESSFULLY BEEN REMOVED AND WHETHER THERE ARE ANY NULL VALUES

import os

output_folder='/workspaces/PAIWP_ASSIGNMENT/3. Data Cleaning'

# df_cleaned.shape - How many rows and columns does the dataset have? -- I have also used this function to test if the file has been loaded successfully
df_shape=df_cleaned.shape

file_name_shape = "df_cleaned_shape_output.txt"

full_file_path_shape=os.path.join(output_folder,file_name_shape)

with open(full_file_path_shape,'w') as file:
    file.write(f"Number of rows: {df_shape[0]}\n")
    file.write(f"Number of columns: {df_shape[1]}\n")

# df_cleaned.info - Print a summary of the Dataset to identify the data type of each column and non-null values -- This will assist with identifying which columns need to be cleaned
from io import StringIO

buffer=StringIO()
df_cleaned.info(buf=buffer)
info_str=buffer.getvalue()

file_name_info='df_cleaned_info_output.txt'

full_file_path_info=os.path.join(output_folder,file_name_info)

with open(full_file_path_info,'w') as f:
    f.write(info_str)

# df_cleaned.head - What does a small sample of the data look like? -- I have also used this function to test if the file has been loaded successfully
df_head_str=df_cleaned.head(10).to_string(index=False)

file_path_head="df_cleaned_head_output.txt"

full_file_path_head=os.path.join(output_folder,file_path_head)

with open(full_file_path_head, 'w') as f:
    f.write(df_head_str)
##############################################################################################################################################