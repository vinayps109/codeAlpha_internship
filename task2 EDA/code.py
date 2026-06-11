import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\code alpha\imdb_top250.csv")
highest_movie = df.loc[df['Rating'].idxmax()]
print(highest_movie ) #for highest rating
print("Movie :", highest_movie['Movie'])
print("Rating:", highest_movie['Rating'])
lowest_movie=df.loc[df['Rating'].idxmin()]
print("Movie :", lowest_movie['Movie'])
print("Rating:", lowest_movie['Rating'])
print("average rating :",df['Rating'].mean())
print("no of movies:",(df['Rating']>8.0).sum()) #for no of movies with rating greater than 8.0
print("no of movies with rating less than 8.0:",(df['Rating']<8.0).sum()) #for no of movies with rating less than 8.0
print(df['Rating'].describe()) #for statistical summary of ratings
print(df.head())
#print(df.show)
print(df.info())#for noof rows and columns
plt.hist(df['Rating'], bins=10, edgecolor='black')
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')

plt.ylabel('Frequency: no of movies')
plt.show()


sns.boxplot(df['Rating'])
plt.show()



