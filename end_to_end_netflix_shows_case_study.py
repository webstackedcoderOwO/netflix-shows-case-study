# -*- coding: utf-8 -*-
"""end-to-end-netflix-shows-case-study.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/142t5hkkgjhdj9LyKsNFXsp7L_ozBo6lP

# **Netflix Case Study Project**

## **Viewing and Importing the Necessary Libraries**
"""

# Import the Dataset
# Import the Pandas Library
import pandas as pd
data = pd.read_csv("/content/8. Netflix Dataset.csv")

data

"""## **Getting some Basic Information about Dataset**"""

data.head()

data.tail()

data.shape

data.size

data.columns

data.dtypes

data.info()

data.duplicated()

# Dropping the Duplicates
data[data.duplicated()]

# Dropping the Duplicates and Saving in the Dataframe
data.drop_duplicates(inplace=True)

data

# Showing the Rows and Columns of the Dataframe
data.shape

# Checking if their are any NULL values in the Dataframe in Boolean Form
data.isnull()

# Checking the total Number of NULL Values in the Dataframe
data.isnull().sum()

# To import Seaborn Library
import seaborn as sns

"""**Showing the NULL Values in the Heatmap**"""

sns.heatmap(data.isnull())

# Show only title Column
data['Title']

"""## **Analyzing and Answering Some Questions Regarding the Data**

###**Q. Show the row where the Title is 'House of Cards'**###
"""

data[data['Title'].isin(['House of Cards'])]

data[data['Title'].str.contains('House of Cards')]

"""###**Q. Add a new Column as 'Date_N' to denaote the Release Date**###"""

data['Date_N'] = pd.to_datetime(data['Release_Date'])

data.head()

data.dtypes

data['Date_N'].dt.year.value_counts()

"""###**Q. With the Help of Bar Graph show that how Many Movies were Released in each Year ?**###"""

data['Date_N'].dt.year.value_counts().plot(kind='bar')

data.head(10)

data.groupby('Category').Category.count()

data.head()

# Make a new column known as Year and put only the Year Column in that Column
data['Year'] = data['Date_N'].dt.year

data.head(5)

"""###**Q. Print out the Shows List whose Category is Movie and Released in the Year 2020.**"""

data[(data['Category'] == 'Movie') & (data['Year'] == 2020.0) ]

data.head(6)

"""###**Q. Print out just the Title of the Movies whose Category is TV Show and the Country is India.** """

data[ (data['Category'] == 'TV Show') & (data['Country'] == 'India')] ['Title']

data[ (data['Category'] == 'TV Show') & (data['Country'] == 'India')] ['Title']

data['Director'].value_counts()

data['Director'].value_counts().head(10)

data.head()

"""###**Q. Print out the data of the Shows whose Category is Movies and Type is Comedies.** """

data[ (data['Category'] == 'Movie') & (data['Type'] == 'Comedies') ]

"""###**Q. Print out the data of the Shows whose Category is Movies and Type is Comedies OR the Shows which were Released in the United Kingdom.** """

data[ (data['Category'] == 'Movie') & (data['Type'] == 'Comedies') | (data['Country'] == 'United Kingdom') ]

data.head()

"""###**Q. Print out the Data of the Shows whose Cast is only Tom Cruise.**"""

data[ (data['Cast'] == 'Tom Cruise') ]

data_new = data.dropna()

data_new.head()

"""###**Q. Print out the Data of the Shows where Tom Cruise is Casted.**"""

# To use the str.contains we have to drop all the NULL values which we dropped Above
data_new[ data_new['Cast'].str.contains('Tom Cruise') ]

data.head(2)

"""###**Q. Print out the number and different types of Ratings in the Dataframe.**"""

data.Rating.nunique()

data['Rating'].unique()

data.head(2)

"""###**Q. Print out the Data of the Shows whose Category is Movie and Rating is TV-14.**"""

data[ (data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') ]

"""###**Q. Print out the Data of the Shows whose Category is Movie, Rating is TV-14 and also Country is Canada.**"""

data[ (data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') & (data['Country'] == 'Canada') ]

"""###**Q. Print out the Shape or Rows and Column of the Data of the Shows whose Category is Movie, Rating is TV-14 and Country is Canada.**"""

data[ (data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') & (data['Country'] == 'Canada') ].shape

data.head(2)

"""###**Q. Print out the Data of the Shows whose Category is TV Shows and Rating is R.**"""

data[ (data['Category'] == 'TV Show') & (data['Rating'] == 'R') ]

"""###**Q. Print out the Data of the Shows whose Category is Movie, Rating is R and Release Year is after Year 2018.**"""

data[ (data['Category'] == 'TV Show') & (data['Rating'] == 'R')  & (data['Year'] > 2018.0) ]

data.head(2)

"""###**Getting some information about Duration**"""

data.Duration.unique()

data.Duration.dtypes

data.head(2)

# Splitting the Duration COlumn into two Columns that is Minutes and Unit.
data[['Minutes', 'Unit']] = data['Duration'].str.split(' ', expand=True)

data.head(2)

# Finding the Show with the Most Duration
data['Minutes'].max()

# Finding the Show with the Minimum Duration
data['Minutes'].min()

data.head(2)

"""###**Getting some more information about the Data and Sorting**"""

data_tvshow = data[ data['Category'] == 'TV Show' ]

data_tvshow.head(3)

data_tvshow.Country.value_counts()

data_tvshow.Country.value_counts().head()

data.head(2)

data.sort_values(by='Year').head()

data.sort_values(by='Year', ascending=False).head()

data.head(3)

"""###**Q. Print out the information about the shows whose Category is Movie and Type is Dramas.**"""

data[ (data['Category'] == 'Movie') & (data['Type'] == 'Dramas') ].head()

"""###**Q. Print out the information about the shows whose Category is TV Show and Type is Kids TV.**"""

data[ (data['Category'] == 'TV Show') & (data['Type'] == "Kids' TV") ].head()

"""###**Q. Print out the information about the shows whose Category is Movie and Type is Dramas OR whose Category is TV Show and Type is Kids TV.**"""

data[ (data['Category'] == 'Movie') & (data['Type'] == 'Dramas') | (data['Category'] == 'TV Show') & (data['Type'] == "Kids' TV") ]

"""# **END**"""