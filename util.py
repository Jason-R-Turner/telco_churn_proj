import pandas as pd

def frequency(ds, vars):
    '''
    takes in a df and the list of column names to produce the frequency for 
    each group we're looking for.
    '''
    
# if statement that runs if there is more than one item in the column name list
    if len(vars) > 1:
        
# creates a variable to hold the first col in col name list from the df
        c1 = ds[vars[0]]

# creates a variable representing an empty list
        c2 = []
    
# for loop that continues for the length of the col name list, many times
        for i in range(1,len(vars)):
        
# adds each iteration through the loop to the end of the formally empty c2 list
            c2.append(ds[vars[i]])
    
# creates an empty list for the dataframes we'll be using for the crosstab
        dfs = []
    
# adds each iteration of the crosstabulation to dfs list 
        dfs.append(pd.crosstab(c1,c2).unstack().reset_index().rename(columns={0:'Count'}))
        dfs.append(pd.crosstab(c1,c2, normalize='all').unstack().reset_index().rename(columns={0:'Percent'}))
        dfs = [df.set_index(vars) for df in dfs]
        df = dfs[0].join(dfs[1:]).reset_index()
        return df
    
# def touch_up(df):