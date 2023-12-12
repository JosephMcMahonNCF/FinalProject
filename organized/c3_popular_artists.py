import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from a1_loading_and_fixing_data import df

# Creating tibble containing the number of times each artist is played
df_artist_counts = df.groupby('artistName').size().reset_index(name='Count')

# Sorting by count
df_artist_counts = df_artist_counts.sort_values(by='Count', ascending=False)


# Top 10 Most Listened to Artists

# Making figure size 20 inches by 10 inches
plt.figure(figsize=(20, 10))

# Using seaborn to intiate bar graph
sns.barplot(x='artistName', y='Count', data=df_artist_counts.head(10),
            hue='artistName', legend=False, palette='Paired')

# Creating labels using matplotlib
plt.title('Top 10 Most Listened to Artists')
plt.xlabel('Artist')
plt.ylabel('Count')

# Loading the graph
plt.show()


# It looks like Crumb is my most viewed artist!
# Next, let's visualize trends in my Crumb listening history