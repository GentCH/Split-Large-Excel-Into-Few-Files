import pandas as pd

df = pd.read_csv('your_csv_file.csv')

#Specify how many rows in each file
partitions = 100000

for i in range(partitions):
    sub_df = df.iloc[(i*partitions):((i+1)*partitions)]
    sub_df.to_excel(f"Disk:\\folder\\folder\\new_file_name-{i}.xlsx", sheet_name="Worksheet")
    if sub_df.empty:
        print('last')
        break
