import pandas as pd
import matplotlib.pyplot as plt

# Load dataset

df = pd.read_excel(r"C:\moviesrating\project\south_indian_movie_reviews.xlsx",
                   engine="openpyxl")

print("File loaded:", df.shape)

df.columns = df.columns.str.strip().str.lower()
print(df.columns)


# # Cleaning
#df.columns = df.columns.str.strip().str.lower()
#df["reviewcomment"] = df["reviewcomment"].fillna("No comment")
for c in ["movie","language","review"]:
    df[c] = df[c].astype(str).str.strip()
df["rating"] = df["rating"].astype(float)
df["year"] = pd.to_datetime(df["year"], errors="coerce").dt.year

df.drop_duplicates(inplace=True)

# # Analysis
print("Average rating per movie:\n", df.groupby("movie")["rating"].mean())
print("\nTop 5 reviews:\n", df.sort_values(by="rating", ascending=False).head(5))

#Histogram
df["rating"].plot(kind="hist", bins=10, title="Histogram of Ratings")
plt.xlabel("Rating")
plt.show()

# Average rating per movie as a bar chart
df.groupby("movie")["rating"].mean().plot(kind="bar", title="Average Rating by movie")
plt.ylabel("Average Rating")
plt.show()

# Pie chart of average rating per product
df.groupby("movie")["rating"].mean().plot(kind="pie",autopct='%1.1f%%', title="Rating by movie")
plt.ylabel(" ")  
plt.show()

#comparing product vs rating -scatter plot
df.reset_index().plot(kind="scatter", x="index", y="rating", title="Scatter: Product Index vs Rating")
plt.show()

# Cleaned excel file created 
df.to_excel("Cleaned_data.xlsx",index=False)



