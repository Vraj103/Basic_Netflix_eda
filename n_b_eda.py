# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 22:42:42 2021

@author: Lenovo
"""

"""Starting a little project based on a netflix dataset, the type of this dataset is Exploratory data analysis
starting with two basic lists first 
Two lists : Years and Duration(mins) (which will continue throughout the eda.)"""

import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

#Two lists.
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary with the two lists
movie_dict = {'years': years, 'durations': durations}
#movie_dict = dict(zip(years,durations))

# Print the dictionary
print(movie_dict)

#Now creating a dataframe with the dictionary using pandas
# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)

# Print the DataFrame
print(durations_df)

"""Now to visualize the data we plot it using matplotlib. 
Which here, shows us that the length has been decreasing over time."""

fig = plt.figure()

# Draw a line plot of release_years and durations
plt.plot(durations_df['years'], durations_df['durations'])

# Create a title
plt.title("Netflix Movie Durations 2011-2020")

# Show the plot
plt.show()

"""Now, working on the real dataset"""

netflix_df = pd.read_csv("netflix_data.csv")

print(netflix_df.head()) #First 5 rows of netflix_df

"""We only want Movies here and no TV shows.
Thus, we filter out the TV shows and keep only movies."""

# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[['title','country','genre','release_year','duration']]

# Print the first five rows of the new DataFrame
print(netflix_movies_col_subset.head())

""" Now, a line plot won't work for a large dataset,
so we visualize the filtered data using scattered plot."""

# Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset['release_year'] , netflix_movies_col_subset['duration'])

# Create a title
plt.title("Movie Duration by Year of Release")

# Show the plot
plt.show()

"""After this, we come to the main question, which is :
    Are movies getting shorter?
    Thus, we fliter out movies that are less than 60 minutes."""

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] < 60]

#Now, we catagorize these short movies by genres using colors.
#Tip : Use .iterrows() here for itterating through dataframe's rows and labels

colors = []

for lab, row in netflix_movies_col_subset.iterrows() :
    if row['genre'] == 'Children' :
        colors.append("red")
    elif row['genre'] == 'Documentaries' :
        colors.append("blue")
    elif row['genre'] == "Stand-Up" :
        colors.append("green")
    else:
        colors.append("black")
        
""" Now, plotting the coloured figure"""

# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'], c = colors)

# Create a title and axis labels
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
pop_a = mpatches.Patch(color='red', label='Children')
pop_b = mpatches.Patch(color='blue', label='Documentaries')
pop_c = mpatches.Patch(color='green', label='Stand-up')
pop_d = mpatches.Patch(color='black', label='Other')
plt.legend(handles=[pop_a,pop_b,pop_c,pop_d])

# Show the plot
plt.show()

#Conclusion!
print("Now, watching the plots we can conclude that maybe movies are getting shorter in length!")

        