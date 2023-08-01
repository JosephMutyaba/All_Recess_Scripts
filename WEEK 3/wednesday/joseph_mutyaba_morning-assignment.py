    ##----------------------- Assignment A7:-------------------------------

"""
    1. a) Show a context manager for file handling that automatically 
        opens and closes a file.
        
       b) Shows a context manager for managing a database connection.
    
       c) Show a multithreading and multiprocessing  that allows us to run 
        the function for different amounts of time.
"""




"""
    1(a) Show a context manager for file handling that automatically opens and closes a file
"""


class FileHandler:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# usage:
file_name = "one.txt"
mode = "r"

with FileHandler(file_name, mode) as file:
    # Perform file operations
    contents = file.read()
    print(contents)


"""
    b) Shows a context manager for managing a database connection.
"""
import mysql.connector

class DatabaseConnection:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    def __enter__(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


# usage:
host = "localhost"
username = "root"
password = ""
database = "atm_service"

with DatabaseConnection(host, username, password, database) as connection:
    # Perform database operation
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customer")
    rows = cursor.fetchall()
    for row in rows:
        print(row)





"""
    c) Show a multithreading and multiprocessing that allows us to run the function for different amounts of time.
"""

import time
import threading
from multiprocessing import Process

# Function to run for a specified duration
def run_function(duration):
    print(f"Function started. Running for {duration} seconds...")
    time.sleep(duration)
    print(f"Function completed after {duration} seconds.")

# Multithreading 
def multi_threading():
    # List of durations for each thread
    durations = [3, 5, 2]

    print("Multithreading .....................")
    threads = []

    # Create and start a thread for each duration
    for duration in durations:
        t = threading.Thread(target=run_function, args=(duration,))
        threads.append(t)
        t.start()

    # Waiting all threads to complete
    for t in threads:
        t.join()

# Multiprocessing 
def multi_processing():
    # List of durations for each process
    durations = [3, 5, 2]

    print("Multiprocessing ................")
    processes = []

    # Create and start a process for each duration
    for duration in durations:
        p = Process(target=run_function, args=(duration,))
        processes.append(p)
        p.start()

    # Waiting all processes to complete
    for p in processes:
        p.join()

# Run the Functions
multi_threading()
print()

if __name__ == '__main__':
    multi_processing()
