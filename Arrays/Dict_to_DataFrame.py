#convert dictionary to pandas data frame
import pandas as pd
emp_det = {'Employee':{'Dev':{'ID':'001',
                              'sal':'2000',
                              'Des':'Teamlead'},
                       'Eva': {'ID': '002',
                               'sal': '1000',
                               'Des': 'Associate'}
                       }}

df = pd.DataFrame(emp_det['Employee'])
print(df)


