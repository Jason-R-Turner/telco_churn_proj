import pandas as pd
import env
import os

def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''
    Function allows user to access Codeup database using their own 
    credentials stored in  their env.py file
    '''
    
# Returns with correct address/password combinat to access the database
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def new_telco_data():
    '''
    SQL query that joins the customers table with, contract, payment, and \n
    internet service options
    '''
    
# SQL query that joins three other tables to customer table
    sql_query = '''
                SELECT * FROM customers
                JOIN contract_types using (contract_type_id)
                JOIN internet_service_types using (internet_service_type_id)
                JOIN payment_types using (payment_type_id)            
                '''
# Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    
# Returns the called dataframe
    return df

def get_telco_data():
    '''
    Function allows user to access telco_data from Codeup database and write it\n
    to a csv file then returns the dataframe.
    '''
    
# if statement that checks if there's already a .csv file to use 
    if os.path.isfile('telco.csv'):
        
# If csv file exists read in data from csv file.
        df = pd.read_csv('telco.csv', index_col=0)
        
# Alternative if no csv file found then
    else:
        
# Read fresh data from db into a DataFrame
        df = new_telco_data()
        
# Cache data for local use
        df.to_csv('telco.csv')

# Returns requested df
    return df