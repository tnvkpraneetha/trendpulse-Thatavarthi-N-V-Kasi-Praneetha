import pandas as pd
import json
import numpy as np

#----------1 — Load and Explore ---------------------->
        #----------Load the JSON File--------
filename = "data/trends_clean.csv"

df=pd.read_csv(filename)
print("Number of rows loaded: ",len(df))
print("First 5 rows: \n",df[:5])
print("Shape of dataframe: ",df.shape)
print("Average score:", df["score"].mean())
print("Average comments:", df["num_comments"].mean())

#---------------- — Basic Analysis with NumPy---------------->
print("--- NumPy Stats ---\n")
scores = df["score"].to_numpy()
comments = df["num_comments"].to_numpy()

print("Mean score: ", np.mean(scores))
print("Median score: ",np.median(scores))
print("Std deviation: ", np.std(scores))
print("Max score : ",np.max(scores))
print("Min score : ",np.min(scores))

if isinstance(df["category"].iloc[0], list):
    cat_counts = df.explode("category")["category"].value_counts()
else:
    cat_counts = df["category"].value_counts()

top_category = cat_counts.idxmax()
top_category_count = cat_counts.max()

print(f"Most stories in: {top_category} ({top_category_count} stories)")

comments = df["num_comments"].to_numpy()
max_idx = np.argmax(comments)

top_title = df.iloc[max_idx]["title"]
top_comments = comments[max_idx]

print(f'\nMost commented story: "{top_title}" — {top_comments:,} comments')

output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")
