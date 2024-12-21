
def create_x_y(df):
    '''
    Separate features from target
    '''
    X = df.drop("median_house_value", axis =1)
    y = df["median_house_value"]
    print("✅ X and y have been created")
    return X, y
