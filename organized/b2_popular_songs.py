import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from a1_loading_and_fixing_data import df

# Creating tibble containing the number of times each song is played
df_song_counts = df.groupby(['artistName', 'trackName']).size().reset_index(name='Count')

# Sorting by count
df_song_counts = df_song_counts.sort_values(by='Count', ascending=False)

# Graphing Top 10 Most Listened to Songs

# Making figure size 10 inches by 10 inches
plt.figure(figsize=(10, 10))

# Using seaborn to intiate bar graph
sns.barplot(x='trackName', y='Count',
            data=df_song_counts.head(10),
            hue='trackName', legend=False, palette='Paired')

# Creating labels using matplotlib
plt.title('Top 10 Most Listened to Songs')
plt.xlabel('Track Name')
plt.ylabel('Number of Plays')
plt.xticks(rotation=10, ha='right') # looks scuffed but not sure how to optimize

# Loading the graph
plt.show()


# Next we will create a graph that shows my top 10 most popular artists

