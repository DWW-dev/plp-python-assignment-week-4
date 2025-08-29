def main():
    filename = input("Enter the filename to read: ")
    try:
        # Try reading the file
        with open(filename, 'r') as infile:
            content = infile.read()
            print("\nOriginal file content:\n")
            print(content)
    except FileNotFoundError:
        print("Error: File not found. Please type the correct name of the file.")
        return
    except PermissionError:
        print("Error: You don't have permission to read this file.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    # Write to a new file
    new_filename = "modified_output.txt"
    try:
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"\nModified content written to {new_filename}")
        print("ooooohraaaaay!!!! input.txt created, processed, and output.txt generated successfully!")
    except IOError:
        print("Error: Cannot write to the new file.")


if __name__ == "__main__":
    main()
