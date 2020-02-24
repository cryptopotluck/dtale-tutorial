from datetime import datetime
import time


class ConvertUnixToDatetime:
    def __init__(self, date):
        self.date = date

    # Convert unix to date object
    def convert_unix(self):
        unix = self.date

        # Check if unix is a string or int & proceeds with correct conversion
        if type(unix).__name__ == 'str':
            unix = int(unix[0:10])
        else:
            unix = int(str(unix)[0:10])

        date = datetime.utcfromtimestamp(unix).strftime('%Y-%m-%d')

        return date

    # Convert date to unix object
    def convert_date(self):
        date = self.date

        # Check if datetime object or raise ValueError
        if type(date).__name__ == 'datetime':
            unixtime = int(time.mktime(date.timetuple()))
        else:
            raise ValueError('You are trying to pass a None Datetime object')
        return type(unixtime).__name__, unixtime


    def __repr__(self):
        return f'You sent in a {type(self.date).__name__} object with a value of {self.date}.' \
               f'\nAdd .convert_unix() if the object is a unix str or int to convert to date' \
               f'\nAdd .convert_date() if datetime object to convert to unix.'


if __name__ == '__main__':
    # Test Date
    date_test = ConvertUnixToDatetime(datetime.today())
    date_test = date_test.convert_date()
    print(date_test)

    # Test Unix
    unix_test = ConvertUnixToDatetime(15391296000)
    print(unix_test.convert_unix())
