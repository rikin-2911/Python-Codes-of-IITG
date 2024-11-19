import pandas as pd   

#Creating a dataframe..!
data = {'Name' : ['Alice', 'Bob', 'Charlie'],
        'Age' : [25, 30, 35],
        'City' : ['New York', 'Los Angeles', 'Chicage']
        }

df = pd.DataFrame(data)

print(df)

