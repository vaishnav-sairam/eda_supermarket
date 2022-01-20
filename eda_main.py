import pandas as pd
import seaborn as sns

df = pd.read_csv (r'C:\Users\vaish\Desktop\files for python proj\supermarket_sales - Sheet1.csv')
print(df)

# Top 5 elements of data frame
df.head()
df.columns
df.dtypes


df['Date']=pd.to_datetime(df['Date'])

# Set the date as index
df.set_index('Date',inplace=True)
df.head()

# Gives base statistics applied on the data frame
df.describe()

# Distribution of rating column
sns.distplot(df['Rating'])

# Histogram distribution of all the columns
df.hist()

# Showing aggregate of different branches
sns.countplot(df['Branch'])
df['Branch'].value_counts()

# Showing aggregate of different payment methods
sns.countplot(df['Payment'])

# Exploring relation between rating and gross income columns
sns.regplot(df['Rating'],df['gross income'])

# Boxplot analysis of columns
sns.boxplot(x=df['Branch'],y=df['gross income'])
sns.boxplot(x=df['Gender'],y=df['gross income'])

# Showing trend in the income column
df.groupby(df.index).mean()
sns.lineplot(x=df.groupby(df.index).mean().index,
             y=df.groupby(df.index).mean()['gross income'])

# Aggregate all duplicate values
df.duplicated().sum()

# Manipulating all missing values
df.isna().sum()
df.fillna(df.mean(),inplace=True)

# Correlation insights
correlation=round(df.corr(),2)
sns.heatmap(correlation,annot=True)
