import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from a1_loading_and_fixing_data import df


# Creating df of Crumb Plays by Day
crumb_plays_by_day = df[df['artistName'] == 'Crumb'].groupby('Date').size().reset_index(name='Count')

# Graphing Crumb Plays by Day
plt.figure(figsize=(10, 6))
plt.plot(crumb_plays_by_day['Date'], crumb_plays_by_day['Count'])
plt.title('Crumb Plays per Day')
plt.xlabel('Date')
plt.ylabel('Plays by Day')
plt.show()

# Let's zoom out a bit
# Graphing Crumb Plays by Month
crumb_plays_by_month = df[df['artistName'] == 'Crumb'].groupby(pd.Grouper(key='Date', freq='M')).size().reset_index(name='Count')
plt.figure(figsize=(10, 6))
plt.plot(crumb_plays_by_month['Date'], crumb_plays_by_month['Count'])
plt.title('Crumb Plays per Month')
plt.xlabel('Date')
plt.ylabel('Plays by Month')
plt.show()

# I notice an upward trend peaking in June.
# Is there a similar trend for streams of any artist?


# Graphing Total Plays by Month
plays_by_month = df.groupby(pd.Grouper(key='Date', freq='M')).size().reset_index(name='Count')
plt.figure(figsize=(10, 6))
plt.plot(plays_by_month['Date'], plays_by_month['Count'])
plt.title('Total Plays per Month')
plt.xlabel('Date')
plt.ylabel('Plays by Month')
plt.show()

# It looks like the peak number of streams for any artist occurred in a different month
# Let's plot the 2 lines on the same graph, using a log scale to get a clearer view

# Creating df containing combined Plays by Crumb and Total Plays
combined_data = pd.concat([
    plays_by_month.assign(Artist='All Artists'),
    crumb_plays_by_month.assign(Artist='Crumb')], ignore_index=True)

# Total Plays and Crumb Plays with Log Scale
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Count', hue='Artist', data=combined_data)
plt.title('Total Plays per Month')
plt.xlabel('Date')
plt.ylabel('Plays by Month')
plt.yscale('log')
plt.show()

# Cool!
# Lastly, let's look at who my favorite artist is for different times of day