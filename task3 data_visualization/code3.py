import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Load the dataset
df = pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\code alpha\task1 webscrabing\imdb.top250.csv")
plt.figure(figsize=(8,5))
plt.hist(df['Rating'], bins=10, edgecolor='black')
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Movies')
plt.show()
top10 = df.sort_values('Rating', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(data=top10, x='Rating', y='Movie')
plt.title('Top 10 Highest Rated Movies')
plt.show()
plt.figure(figsize=(6,4))
sns.boxplot(x=df['Rating'])
plt.title('Box Plot of Movie Ratings')
plt.show()
high = (df['Rating'] >= 8.5).sum()
medium = ((df['Rating'] >= 8.0) & (df['Rating'] < 8.5)).sum()

plt.figure(figsize=(6,6))
plt.pie([high, medium],
        labels=['Rating ≥ 8.5', 'Rating 8.0-8.4'],
        autopct='%1.1f%%')
plt.title('Movie Rating Categories')
plt.show()