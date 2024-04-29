'''
[Factory Design Pattern] Build a logging system using the Factory Design Pattern. 
Create a LoggerFactory class that generates different types of loggers (e.g., FileLogger, ConsoleLogger, DatabaseLogger). 
Implement methods in each logger to write logs to their respective destinations. Show how the Factory Design Pattern helps 
to decouple the logging system from the application and allows for flexible log handling.
'''

import sqlite3
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass


class FileLogger(Logger):
    def log(self, message):
        with open('log.txt', 'a') as file:
            file.write(f'{message}\n')
        print(f'Logged "{message}" to the file')


class ConsoleLogger(Logger):
    def log(self, message):
        print(message)


class DatabaseLogger(Logger):
    def __init__(self):
        self.connection = sqlite3.connect('database_logs.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, message TEXT)''')
        self.connection.commit()

    def log(self, message):
        self.cursor.execute('''INSERT INTO logs (message) VALUES (?)''', (message,))
        self.connection.commit()
        print(f'Logged "{message}" to the database')

    def __del__(self):
        self.connection.close()


class LoggerFactory:
    @staticmethod
    def get_logger(logger_type):
        if logger_type == 'file':
            return FileLogger()
        elif logger_type == 'console':
            return ConsoleLogger()
        elif logger_type == 'database':
            return DatabaseLogger()
        else:
            raise ValueError('Invalid logger type')

# running tests
if __name__ == "__main__":
    file_logger = LoggerFactory.get_logger('file')
    file_logger.log('This is a file log message')

    console_logger = LoggerFactory.get_logger('console')
    console_logger.log('This is a console log message')

    database_logger = LoggerFactory.get_logger('database')
    database_logger.log('This is a database log message')