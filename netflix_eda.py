import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter

# Load the dataset
file_path = '/mnt/data/netflix_titles.csv'
netflix_df = pd.read_csv(file_path)

# Handle Missing Data
netflix_df['director'].fillna('Unknown', inplace=True)
netflix_df['cast'].fillna('Unknown', inplace=True)
netflix_df['country'].fillna('Unknown', inplace=True)
netflix_df['date_added'].fillna('Unknown', inplace=True)
netflix_df['rating'].fillna('Not Rated', inplace=True)

# 1. Distribution of Movie and TV Shows
plt.figure(figsize=(8, 6))
sns.countplot(data=netflix_df, x='type', palette='Set2')
plt.title("Distribution of Movies and TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# 2. Top 10 Genres
genres = netflix_df['listed_in'].str.split(',').sum()
genre_counts = Counter([genre.strip() for genre in genres])
top_genres = pd.DataFrame(genre_counts.most_common(10), columns=['Genre', 'Count'])

plt.figure(figsize=(10, 6))
sns.barplot(data=top_genres, x='Count', y='Genre', palette='Set3')
plt.title("Top 10 Genres")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()

# 3. Releases Over Time
plt.figure(figsize=(10, 6))
sns.histplot(data=netflix_df, x='release_year', bins=30, kde=True, color='skyblue')
plt.title("Content Releases Over Time")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.show()

# 4. Ratings Distribution
plt.figure(figsize=(12, 6))
rating_counts = netflix_df['rating'].value_counts()
rating_counts.plot(kind='bar', color='coral')
plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# 5. Word Cloud for Titles
titles = ' '.join(netflix_df['title'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)

plt.figure(figsize=(12, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Titles", fontsize=16)
plt.show()
