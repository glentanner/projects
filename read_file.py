try:
    # Prompt the user to enter the filename
    filename = input("Please enter the name of the file you want to open: ")

    # Open the file in read mode ('r')
    # The 'with' statement ensures the file is automatically closed
    with open(filename, 'r') as file:
        # Read the content of the file (or process it line by line, etc.)
        content = file.read()
        print(f"Content of '{filename}':\n{content}")

except FileNotFoundError:
    # Handle the case where the specified file does not exist
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    # Handle any other potential errors during file operations
    print(f"An unexpected error occurred: {e}")