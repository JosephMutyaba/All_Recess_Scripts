import shutil
import os


def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid operand types!")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("No exceptions occurred.")
    finally:
        print("Exception handling complete.")


if __name__ == '__main__':
    # Example usage
    divide_numbers(10, 2)  # Valid division
    divide_numbers(10, 0)  # ZeroDivisionError
    divide_numbers(10, "2")  # TypeError
    divide_numbers("10", 2)  # TypeError


"""
    file = open(filename, mode)
    
    with open(filename, 'r') as f
"""


def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)


def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)


def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " +
              new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)


def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)


if __name__ == '__main__':
    filename = "file1.txt"
    new_filename = "file24.txt"

    # create_file(filename)
    # read_file(filename)

    # append_file(filename, "This is some additional text.\n")
    # read_file(filename)

    # rename_file(filename, new_filename)
    # read_file(new_filename)

    # delete_file(new_filename)


# ---------------------------Directory handling------------------------


def create_directory(directory_path):
    os.mkdir(directory_path)
    print(f"Directory created: {directory_path}")


def list_directory_contents(directory_path):
    contents = os.listdir(directory_path)
    print(f"Contents of directory {directory_path}:")
    for item in contents:
        print(item)


def check_directory_existence(directory_path):
    if os.path.exists(directory_path):
        print(f"Directory exists: {directory_path}")
    else:
        print(f"Directory does not exist: {directory_path}")


def remove_directory(directory_path):
    os.rmdir(directory_path)
    print(f"Directory removed: {directory_path}")


def remove_dir(directory_path):
    shutil.rmtree(directory_path)
    print(f"Directory removed: {directory_path}")


if __name__ == '__main__':
    # Directory handling example
    directory_path = "folder1"
    non_empty_directory = "folder2"

    # create_directory(directory_path)

    # list_directory_contents(non_empty_directory)

   # check_directory_existence(non_empty_directory)

    # remove_directory(directory_path)

    # # Remove the directory which is not empty
    # remove_dir(non_empty_directory)
