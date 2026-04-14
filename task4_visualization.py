import pandas as pd
import os
import matplotlib.pyplot as plt

#-----------------------------1 — Setup-------------------
# -------- Load CSV --------
df = pd.read_csv("data/trends_analysed.csv")

# -------- Create outputs folder --------
if not os.path.exists("outputs"):
    os.makedirs("outputs")

#---------------------------Chart 1: Top 10 Stories by Score------------------

# Getting top 10 stories by score
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shortening titles to 50 characters
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

# horizontal bar chart
plt.figure()

plt.barh(top10["short_title"], top10["score"])

plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

plt.gca().invert_yaxis()

plt.savefig("outputs/chart1_top_stories.png")

plt.show()

#--------------------— Chart 2: Stories per Category ---------


if isinstance(df["category"].iloc[0], list):
    category_counts = df.explode("category")["category"].value_counts()
else:
    category_counts = df["category"].value_counts()

colors = ["red", "blue", "green", "orange", "purple"]
# Creating bar chart
plt.figure()

plt.bar(category_counts.index, category_counts.values,color=colors)

plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")

plt.show()

#-------------Chart 3: Score vs Comments ---------------

df["is_popular"] = df["score"] >= 100
popular = df[df["is_popular"] == True]
non_popular = df[df["is_popular"] == False]

plt.figure()

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(non_popular["score"], non_popular["num_comments"], label="Non-Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")

plt.legend()

plt.savefig("outputs/chart3_scatter.png")

plt.show()
