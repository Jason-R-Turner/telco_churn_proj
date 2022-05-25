import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def prep_telco(df):
    '''
    Prepares acquired telco dataframe for exploration
    '''
    train, test = train_test_split(df, 
                               train_size = 0.8, 
                               stratify = df.churn, 
                               random_state=5678)
    
    train, validate = train_test_split(train,
                                    train_size = 0.7,
                                    stratify = train.churn,
                                    random_state=5678)
    return train, validate, test

# def encode_telco(df):

def clean_telco_cat(df):
    '''
    Prepares Telco data by dropping continuous/index-like data, duplicate or redundant columns and converting  remaining columns into binary data.
    '''
    df = df.drop_duplicates()
    
    cols_to_drop = ['payment_type_id', 'internet_service_type_id', 'contract_type_id',  'customer_id', 'tenure', 'monthly_charges', 'total_charges']
    
    df = df.drop(columns=cols_to_drop)
    
    dummy_df = pd.get_dummies(df, dummy_na=False, drop_first=[True, True])
    
    
    return dummy_df


def telco_clean_services(df):
    '''
    Drops extraneous columns that are virtual duplicates or are not services offered by telco except for churn.
    '''
    df = df.drop_duplicates()

    cols_to_drop = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id', 'gender', 'senior_citizen', 'partner', 'dependents', 'tenure', 'monthly_charges', 'total_charges', 'contract_type', 'payment_type']
    
    df = df.drop(columns=cols_to_drop)

    return df