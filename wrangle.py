def new_zillow_data():
    '''
    This reads the zillow data from the Codeup db into a df
    '''
    sql_query = """
                SELECT id, propertylandusetypeid, bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips from properties_2017
                WHERE propertylandusetypeid = '261';
                """
    
    # Read in DataFrame from Codeup.
    df = pd.read_sql(sql_query, get_db_url('zillow'))
    
    return df

def get_zillow_data():
    '''
    This reads in telco data from Codeup database, writes data to
    a csv if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('zillow.csv'):
        
        # read in data from csv file if one exists
        df = pd.read_csv('zillow.csv', index_col=0)
        
    else:
        
        # Read data from db into a DataFrame
        df = new_zillow_data()
        
        # Cache to .csv
        df.to_csv('zillow.csv')
        
    return df

def split_data(df, test_size=.2, validate_size=.25, col_to_stratify=None, random_state=None):
    '''
    This splits data into test,train and validate data
    '''
    # This takes in a default variable or a variable to determine target variable for stratification
    if col_to_stratify == None:
    # this splits the data
        train_validate, test = train_test_split(df, test_size=test_size, random_state=random_state)
        train, validate = train_test_split(train_validate,
                                       test_size=validate_size,
                                       random_state=random_state,)
    else:                                                        
        train_validate, test = train_test_split(df, test_size=test_size, random_state=random_state, stratify=df[col_to_stratify])
        train, validate = train_test_split(train_validate,
                                       test_size=validate_size,
                                       random_state=random_state,
                                       stratify=train_validate[col_to_stratify])
    return train, validate, test

def wrangle_zillow():
    '''
    Read zillow data into a pandas DataFrame from mySQL,
    drop property use id column, drop rows with null values,
    return cleaned zillow DataFrame.
    '''

    # Acquire data

    df = get_zillow_data()
    
    # drop property use id column
    
    df = df.drop(columns=['propertylandusetypeid'])

    # Drop all rows with NaN values.
    
    df = df.dropna()

    return df

def minmax_scaler(train, validate, test):
    scaler_minmax = sklearn.preprocessing.MinMaxScaler()

    scaler_minmax.fit(x_train)

    x_train_scaled_minmax = scaler_minmax.transform(x_train)
    x_validate_scaled_minmax = scaler_minmax.transform(x_validate)
    x_test_scaled_minmax = scaler_minmax.transform(x_test)
    
    return x_train_scaled_minmax, x_validate_scaled_minmax, x_test_scaled_minmax