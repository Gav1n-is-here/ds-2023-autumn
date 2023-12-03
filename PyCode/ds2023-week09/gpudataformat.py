import pandas as pd
import openpyxl
from functools import reduce

df = pd.ExcelFile("gpu_modified.xlsx")
dfout = pd.DataFrame()#可用于生成图的df

sheets=df.sheet_names
gpuname=[]
for i in sheets:
    df_sub=df.parse(sheet_name=i)
    #print(df_sub)

    gpunamesub=df_sub['gpuname']
    for i in range(0,30):
        gpuname.append(gpunamesub[i])
    

func = lambda x,y:x if y in x else x + [y]
gpuname=reduce(func, [[], ] + gpuname)
#print(gpuname)
dfout['gpuname']=gpuname

for i in sheets:

    newcolumnname=i
    newcolumnvalue=[]
    df_sub=df.parse(sheet_name=i)
    for j in gpuname:
        col=df_sub.loc[df_sub['gpuname']==j]
        if col.empty:
            a=0
        else:
            #print(col)
            a=col.loc[:,'percentage'].values[0]
            print(a)
            a=float(a.strip('%'))
            print(a)
        newcolumnvalue.append(a)
    dfout[newcolumnname]=newcolumnvalue
print(dfout)

dfout.to_excel('gpu_data.xlsx',            # 路径和文件名
            sheet_name='sheet1',     # sheet 的名字
            )  

