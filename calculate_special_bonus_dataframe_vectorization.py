import pandas as pd

# approach -- vectorization i.e. adding extra column to the dataframe

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    # use vectorization -- creating additional column and performing lambda expression
    employees['bonus'] = employees.apply(

        lambda x : x['salary']
            if x['employee_id'] %2 != 0 and not x['name'].startswith('M')
            else 0,
        
        axis = 1

    )
    
    # sort employees by employee_id
    employees.sort_values(by=['employee_id'], inplace = True)

    return employees[['employee_id', 'bonus']]