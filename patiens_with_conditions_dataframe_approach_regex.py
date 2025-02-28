import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    # make modification in DataFrame
    
    # convert to series -- regex expressions
    df = patients['conditions'].str.contains(r"(^|\s)DIAB1", regex = True)

    # convert to dataframe
    df = patients[df]

    return df