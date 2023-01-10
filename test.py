import pandas as pd

'''dict1 = {
    "Values 1": [2, 15, 3, 24, 5, 16],
    "Values 2": [7, 10, 3, 5, 6, 23],
    "Values 3": ["Orange", "Apple", "Kiwi", "Cherry", "Banana", "Grape"],
}

dict2 = {
    "Values 1": [15, 2, 3, 5, 24, 16],
    "Values 2": [10, 7, 3, 6, 5, 23],
    "Values 3": ["Apple", "Orange", "Kiwi", "Banana", "Cherry", "Grape"],
}

dict3 = {
    "Values 1": [15, 2, 3, 5, 24],
    "Values 2": [10, 7, 3, 6, 5],
    "Values 3": ["Apple", "Orange", "Kiwi", "Banana", "Cherry"],
}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
df3 = pd.DataFrame(dict3)

df_merged_1 = pd.merge(
    df1, df2, how="outer", left_index=False, right_index=False, indicator=True
)

print(df_merged_1)

# print(df_merged["_merge"].unique())
print(df_merged_1["Values 3"].unique())
print(df_merged_1["_merge"].unique())
a = df_merged_1["_merge"].unique()
print(type(a))
print(len(a))

df_merged_2 = pd.merge(
    df1, df3, how="outer", left_index=False, right_index=False, indicator=True
)

print(df_merged_2)

a = df_merged_2["_merge"].unique()
print(a)
print(len(a))
print('right_only' in a)

print(a.categories, type(a.categories))
print(type(df_merged_1["_merge"]))
print(type(df_merged_1["_merge"].unique()))

b = a.remove_unused_categories()
print("xx")
print(b)
print("xx")
print(type(b.categories))
print(len(b.categories))'''

comparee_df: pd.DataFrame = pd.read_csv('cleaned_data/segments_gsr.csv')

print(comparee_df.columns)
print(comparee_df["Unnamed: 0"])
b = comparee_df.drop("Unnamed: 0", axis=1)
print(b.columns)
print(comparee_df.head())
print(b.head())