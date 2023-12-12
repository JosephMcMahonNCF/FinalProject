import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import CategoricalDtype
from datetime import datetime
import mpld3

# Importing Spotify data using json
json_file1 = "C:/Users/josep/Downloads/my_spotify_data_2/MyData/StreamingHistory0.json"
json_file2 = "C:/Users/josep/Downloads/my_spotify_data_2/MyData/StreamingHistory1.json"

# Load JSON data
json_data1 = pd.read_json(json_file1)
json_data2 = pd.read_json(json_file2)

# Combine JSON data into a DataFrame
df = pd.concat([json_data1, json_data2], ignore_index=True)

# Convert milliseconds to seconds
df['sPlayed'] = df['msPlayed'] / 1000

# Convert seconds to minutes
df['mPlayed'] = pd.to_datetime(df['sPlayed'], unit='s').dt.strftime('%M:%S')

# Convert 'endTime' to datetime
df['endTime'] = pd.to_datetime(df['endTime'])

# Adding date variable
# Creating a new column 'Date' by converting the 'endTime' variable into a new date variable
df['Date'] = df['endTime'].dt.date

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])


# Create time of day categories
time_levels = ["Late Night", "Early morning", "Morning", "Afternoon", "Dusk", "Night"]
df['TimeCategory'] = pd.cut(df['endTime'].dt.hour,
                            bins=[-np.inf, 4, 8, 12, 16, 20, 24],
                            labels=time_levels,
                            right=False).astype(CategoricalDtype(categories=time_levels, ordered=True))

# Creating criteria for streams to count towards counts
df_song_length = df.groupby('trackName')['sPlayed'].max().reset_index(name='max_sPlayed')
df = pd.merge(df, df_song_length, on='trackName', how='left')

# Filtering out podcasts
df_songs_only = df[df['max_sPlayed'] < 1100]

# Filtering out songs where less than 1/2 of the length of the track was played
df_half_played = df_songs_only[df_songs_only['sPlayed'] > df_songs_only['max_sPlayed'] * 0.5]

# Changing "$" in artistName to "s"
df.loc[:, 'artistName'] = df_half_played['artistName'].str.replace('$', 's')

# Removing brown noise entries
condition = df['trackName'].str.contains('Brown Sleep Noise')
df = df[~condition]

# Now we have a polished dataframe of my spotify data nicely named "df"
df

# Next we will create a graph that shows my top 10 most popular songs!
