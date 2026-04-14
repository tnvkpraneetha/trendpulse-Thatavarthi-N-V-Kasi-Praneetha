import pandas as pd
import json

#----------Load the JSON File--------
filename = "data/trends_20260414.json"

with open(filename, "r") as f:
    data = json.load(f)

df=pd.DataFrame(data)
print("Number of rows loaded: ",len(df))

#-----------Clean the Data-----------

df=df.drop_duplicates()
print("Number of rows after removing duplicates: ",len(df))

df=df.dropna(subset=["post_id","title","score"])
print("Number of rows after removing nulls: ",len(df))

print(df.info())

# Remove stories with score < 5
df = df[df["score"] >= 5]
print("After removing low scores: ",len(df))

df["title"] = df["title"].str.strip()

#-----------Save as CSV ---------
import os

if not os.path.exists("data"):
    os.makedirs("data")

file_path = "data/trends_clean.csv"
df.to_csv(file_path, index=False)

print(f"File saved as: {file_path}")
print("Total rows saved:", len(df))


if isinstance(df["category"].iloc[0], list):
    summary = df.explode("category")["category"].value_counts()
else:
    summary = df["category"].value_counts()

print("\nStories per category:")
print(summary)
