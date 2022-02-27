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


