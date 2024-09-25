try:
    file = open("my_file.txt", "w")
    file.write("Hello, Python!\nWelcome to Python 101\nPython rocks\n")
    print("File created and initial content written successfully.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    file.close()

try:
    file_object = open("my_file.txt", "r")
    file_contents = file_object.read()
    print("\n--- File Content After Initial Write ---")
    print(file_contents)
except FileNotFoundError:
    print("File not found. Please ensure the file exists.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
finally:
    file_object.close()

try:
    file = open("my_file.txt", "a")
    file.write("Woohoo, Python!\nI love Python\nPython is awesome!\n")
    print("\nNew content appended successfully.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")
finally:
    file.close()

try:
    file_object = open("my_file.txt", "r")
    file_contents = file_object.read()
    print("\n--- File Content After Appending ---")
    print(file_contents)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
finally:
    file_object.close()
