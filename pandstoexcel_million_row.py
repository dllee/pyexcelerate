import pandas as pd
from pyexcelerate import Workbook

DATA_LENGTH = 30000000
df = pd.DataFrame({'Val1': [i for i in range(DATA_LENGTH)],
                   'Val2': [i for i in range(DATA_LENGTH)]})

def df_to_excel(df, excelfilename):
    SHEET_LENGTH = 1000000
    print(df)

    wbk = Workbook()
    for i in range(0, len(df), SHEET_LENGTH):
        print(i)
        df1 = df.iloc[i:i+SHEET_LENGTH, ]
        values = [df1.columns] + list(df1.values)
        wbk.new_sheet(sheet_name='Row {}'.format(i), data=values)
    wbk.save(excelfilename)

df_to_excel(df, 'test.xlsx')
