import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    for i in range(0,len(employees)):
        e_id = employees['employee_id'][i]
        e_name = employees['name'][i] # example [M,i,e,r]

        if e_id % 2 != 0 and e_name[0] != 'M':
            pass
        else:
            employees['salary'][i] = 0
    
    # sort employees by employee_id
    employees.sort_values(by=['employee_id'], inplace = True)

    return employees[['employee_id', 'salary']].rename(columns = {'salary' : 'bonus'})
    