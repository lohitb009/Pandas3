import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    # make modification in DataFrame
    
    # convert to series
    df = patients['conditions'].str.startswith('DIAB1') | patients['conditions'].str.contains(' DIAB1')

    # convert to dataframe
    df = patients[df]

    return df