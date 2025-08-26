
# This program asks the user for a filename, reads its content,
# modifies it, and writes the modified content to a new file.

def main():
    try:
        # Ask user for the file name
        filename = input("Enter the filename to read: ")

        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (example: make everything uppercase)
        modified_content = content.upper()

        # Create a new output file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"File has been successfully modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print(" Error: The file does not exist. Please check the name and try again.")
    except PermissionError:
        print(" Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
