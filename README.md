# Split-Large-Excel-Into-Few-Files
Split excel with many data into few files with specific rows in each file.


<h3>1. Install Library</h3>
<p>
  Pandas is a Python library used to analyze data.
</p>

```
pip install pandas
```


<h3>2. Import Library</h3>
<p>
  Import library under 'pd' alias.
</p>

```
import pandas as pd
```


<h3>3. Read CSV and Specify Number of Data Per File</h3>
<p>
  Read CSV content and specify how many data to have in each excel file
</p>

```
df = pd.read_csv('your_csv_file.csv')

partitions = 100000
```


<h3>4. Slice Object and Wrte to Excel Sheet </h3>
<p>
  Pandas DataFrame is a 2 dimensional data structure which consists of three principal components -- data, rows, and columns. 
  <br/>
  - .iloc is a purely integer-location based indexing for selection by position. 
  <br/>
  - [(i*partitions):((i+1)*partitions)] is the row indexes.
  <br/>
  - .empty is to indicate whether Series/DataFrame is empty.
</p>

```
for i in range(partitions):
    sub_df = df.iloc[(i*partitions):((i+1)*partitions)]
    sub_df.to_excel(f"Disk:\\folder\\folder\\new_file_name-{i}.xlsx", sheet_name="Worksheet")
    if sub_df.empty:
        print('last')
        break
```
