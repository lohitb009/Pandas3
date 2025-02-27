import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    # make a resultant list
    result = []

    for i in range(0,len(employees)):
        e_id = employees['employee_id'][i]
        e_name = employees['name'][i] # example [M,i,e,r]

        if e_id % 2 != 0 and e_name[0] != 'M':
            result.append([e_id, employees['salary'][i]])
        else:
            result.append([e_id, 0])
    
    # convert result to datatframe
    result = pd.DataFrame(result, columns= ['employee_id', 'bonus'])
    result.sort_values(by=['employee_id'], inplace = True)

    return result
    