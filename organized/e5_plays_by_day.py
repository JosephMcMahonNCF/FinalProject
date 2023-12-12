import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from a1_loading_and_fixing_data import df


# Creating df of artist streams by time of tay
artists_by_time_of_day = df.groupby(['artistName', 'TimeCategory'],
                                    observed=True).size().reset_index(name='Count')
popular_artist_by_time = artists_by_time_of_day.\
    groupby('TimeCategory', observed=True).\
    apply(lambda x: x.loc[x['Count'].idxmax()]).reset_index(drop=True)

# Plotting most popular artists for each time of day
plt.figure(figsize=(10, 6))
sns.barplot(x='TimeCategory', y='Count', data=popular_artist_by_time,
            hue='artistName')
plt.title('Most Popular Artists by Time of Day')
plt.xlabel('')
plt.ylabel('Count')
plt.show()


# While Crumb is still highly represented, it looks like I listen to Kendrick Lamar at night more.

# The end

# Thank you for a fun semester and I hope to take one of your classes again in the future!