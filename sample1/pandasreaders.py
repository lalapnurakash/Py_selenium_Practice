import pandas as pd


ins=['he','she','it','then','when']
print(pd.DataFrame(ins))
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
print(pd.DataFrame(data))
data = pd.read_csv("D:\\downloads\\nba.csv",index_col='Name')

first = data.loc["R.J. Hunter"]
second = data.loc["Amir Johnson"]

print(first, "\n\n\n", second)

new = data["Team"].replace("Boston Celtics", "boss").copy()

# checking with custom string
