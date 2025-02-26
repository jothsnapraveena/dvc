import pandas as pd


Data=[

    {"name": "Jothsna","age":30,"city":"Boston"},
    {"name": "Mohan","age":35,"city":"NewYork"},
    {"name": "Trishika","age":4,"city":"Virginia"},
    {"name": "Ravi","age":35,"city":"Niagara"}
]

df=pd.DataFrame(Data)

df.to_csv("data/data.csv",index=False)


print("CSV file saved successfully!")
