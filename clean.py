import numpy as np
import pandas as pd

books = pd.read_csv('data/books.csv',
                    sep=';',
                    error_bad_lines=False,
                    encoding='latin-1')

books = books.drop(['Image-URL-L', 'Image-URL-M', 'Image-URL-S'], axis=1)

books.columns = ['ISBN', 'title', 'author', 'year', 'publisher']

books.year.unique()

books = books[(books['year'] != 'DK Publishing Inc') &
              (books['year'] != 'Gallimard')]

books.year = books.year.astype('int32')
books.dtypes

books = books.dropna()
books.isnull().sum()

ratings = pd.read_csv('data/ratings.csv',
                    sep=';',
                    error_bad_lines=False,
                    encoding='latin-1')

ratings.head()
ratings = ratings.dropna()
ratings.columns = ['ID', 'ISBN', 'rating']

users = pd.read_csv('data/users.csv',
                    sep=';',
                    error_bad_lines=False,
                    encoding='latin-1')

users = users.dropna()
users.columns = ['ID', 'location', 'age']

users.loc[(users.age > 100) | (users.age < 5), 'age'] = users.age.mean()
sorted(users.age.unique())
users.age = users.age.astype('int32')
users.dtypes

users.columns
books.columns

