# %%
import  pandas as pd
import json


# %% Variant sheet
# Read and drop some rows
df = pd.read_excel('test.xlsx',sheet_name='Variant', header=2)
df = df.drop([0,1])

df = df.reset_index(drop=True)  # make sure indexes pair with number of rows

# df.to_json('data/all.json', orient = 'index')
for index in range(df.shape[0]):
    
    df_sub = df.iloc[[index],:]
    print(index)
    # print("data/"+df_sub['Linking ID'][index].replace('.', "_")+".json")
    df_sub.to_json("data/"+df_sub['Linking ID'][index].replace('.', "_").replace(':', "_").replace('>', "_")+".json", orient='records')

# %%
