import pandas as pd


def read_data():
    df = yf.download('GBR', period='max')
    df.to_csv('file1.csv')


# добавление пропущенных дат
def add_nan():
    df = pd.read_csv('file1.csv')
    idx = pd.date_range(df['Date'].min(), df['Date'].max())
    df.index = pd.DatetimeIndex(df['Date'])
    df = df.reindex(idx, fill_value='NaN')
    del df['Date']
    df.index.name = 'Date'
    df.to_csv('file2.csv')


# линейная интреполяция
def linear():
    df = pd.read_csv('file2.csv')
    columns = list(df)
    for i in columns:
        df[i].interpolate(method='linear', inplace=True)
    print(df)


# квадратичная интерполяция
def quadratic():
    df = pd.read_csv('file2.csv')
    columns = list(df)
    for i in columns:
        df[i].interpolate(method='quadratic', inplace=True)
    print(df)


# заполняет пропуски ближайшими значениями
def nearest():
    df = pd.read_csv('file2.csv')
    columns = list(df)
    for i in columns:
        df[i].interpolate(method='nearest', inplace=True)
    print(df)


nearest()
linear()
quadratic()
