##############################################################################################################################################
# The Purpose of this file is to load the dataset (telco_churn_data.csv) which was acquired from Kaggle to then understand and clean the data
##############################################################################################################################################

##############################################################################################################################################
# LOAD THE DATASET

import pandas as pd

# CSV file has been loaded to PAIWP_ASSIGNMENT GitHub repository

file_path = '/workspaces/PAIWP_ASSIGNMENT/telco_churn_data.csv'
df = pd.read_csv(file_path)
