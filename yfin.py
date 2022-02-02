import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt


class Quotes:

    def __init__(self):
        self.date_start = '2000-01-01'
        self.date_end = '2023-01-01'
        self.ticker = 'GOOG'
        self.data = pd.DataFrame()

    def get_quotes(self):
        self.data = yf.download(self.ticker, self.date_start, self.date_end)['Adj Close']

    def print_quotes(self):
        self.get_quotes()
        print(self.data)

    def print_quotes_plot(self):
        self.get_quotes()
        self.data.plot()
        plt.title(self.ticker)
        plt.ylabel('Price')
        plt.show()

    def edit_ticker(self):
        self.ticker = input("Введите тикер: ")

    def edit_date_start(self):
        date_str = input("Введите дату начала периода (dd/mm/yyyy): ")
        self.date_start = dt.datetime.strptime(date_str, '%d/%m/%Y').date()

    def edit_date_end(self):
        date_str = input("Введите дату конца периода (dd/mm/yyyy): ")
        self.date_start = dt.datetime.strptime(date_str, '%d/%m/%Y').date()

    def menu(self):
        while 1:
            print('1 - Изменить тикер')
            print('2 - Изменить дату начала периода')
            print('3 - Изменить дату конца периода')
            print('4 - Вывести котировки')
            print('5 - Отобразить график котировок')
            print('Введите любое значение для выхода')
            option = input()
            if option == '1':
                self.edit_ticker()
            elif option == '2':
                self.edit_date_start()
            elif option == '3':
                self.edit_date_end()
            elif option == '4':
                self.print_quotes()
            elif option == '5':
                self.print_quotes_plot()
            else:
                break


a = Quotes()
a.menu()
