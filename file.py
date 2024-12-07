def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            # Read the content of the file
            content = infile.read()

        # Modify the content (converting to uppercase as an example)
        modified_content = content.upper()

        # Write the modified content to a new output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"The modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except IOError:
        print(f"Error: There was an issue reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for a filename to read and the output filename
input_filename = input("Enter the name of the file to read: ")
output_filename = input("Enter the name of the new file to write to: ")

# Call the function to process the file
read_and_modify_file(input_filename, output_filename)
