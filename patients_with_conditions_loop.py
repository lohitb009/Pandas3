import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    
    # set the result
    result = []

    for i in range(0,len(patients)):

        p_id = patients['patient_id'][i]
        p_name = patients['patient_name'][i]
        p_conditions = patients['conditions'][i]

        for c in p_conditions.split():
            print(c)
            if c.startswith('DIAB1'):
                result.append([p_id, p_name, p_conditions])
                
                # for condition DIAB100 MYOP DIAB100 -- entry will be added twice
                break
        # end of condition for loop
    # end of patients iteration    
        
    # convert result to dataframe

    return pd.DataFrame(result, columns = ['patient_id', 'patient_name', 'conditions'])