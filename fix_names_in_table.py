import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    
    # using vectorization -- vectorize str method
    
    # users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()

    users['name'] = users['name'].str.capitalize() # capitalize method
    
    return users.sort_values(by = ['user_id'])