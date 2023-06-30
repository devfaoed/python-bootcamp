# This import must be made if you are working locally on your machine.
# import os

def read_file(file_name):
    # Naive approach
    # file = open(file_name)
    # file_content = file.read()
    # print(file_content)
    # file.close()
    # return file_content
    
    # Better one
    # with open(file_name) as file:
    #     file_content = file.read()
    #     print(file_content)
    #     return file_content

    try:
        with open(file_name, encoding='utf-8') as file:
            file_content = file.read()
            print(file_content)
            return file_content
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{file_name}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")

def read_file_into_list(file_name):
    # Approach without try and except
    # with open(file_name) as file:
    #     file_content = file.read()
    #     file_content_list = file_content.split("\n")
    #     return file_content_list
    
    try:
        with open(file_name, encoding='utf-8') as file:
            file_content = file.readlines()
            # tests doesn't like if we remove \n from the end of our lines
            # file_content_list = [line.strip() for line in file_content]
            file_content_list = [line for line in file_content]
            return file_content_list
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{file_name}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")

def write_first_line_to_file(file_contents, output_filename):
    # This is redundant thing to do because we can pass the necessary path
    # through arguments, but if we will do this test will fail =(
    # So what this code does, it basically creates a path for our online.txt output file
    # which will be created beside our py file in the same folder.
    # This code is not necessary if you are working in courseras code editor
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # output_path = os.path.join(current_dir, output_filename)
    
    lines = file_contents.split("\n")
    first_line = lines[0]
    
    # approach without using an try except
    # used output_path here because i work locally on my machine
    # and i want to save files properly in folder i specifically want
    # with open(output_path, "w", encoding='utf-8') as file:
    #     file.write(first_line)

    try:
        # with open(output_path, "w", encoding='utf-8') as file:
        #     file.write(first_line)
        with open(output_filename, "w", encoding='utf-8') as file:
            file.write(first_line)
    except OSError as e:
        print(f"Error occurred while writing to file: {e}")

def read_even_numbered_lines(file_name):
    # Straight forward approach
    # with open(file_name, encoding='utf-8') as file:
    #     file_content = file.readlines()
    #     even_numbered_lines_list = []
    #     for index, line in enumerate(file_content):
    #         if index % 2 == 0:
    #             even_numbered_lines_list.append(line)
    #     return even_numbered_lines_list
    
    try:
        with open(file_name, encoding='utf-8') as file:
            file_content = file.readlines()
            even_numbered_lines_list = [line for index, line in enumerate(file_content, start=1) if index % 2 == 0]
            return even_numbered_lines_list
    except OSError as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def read_file_in_reverse(file_name):
    # We can't use reverse function because it returns None.
    # However there are many ways how we can reverse content in a list
    # For example we can use for loop or we can use more hacky way writing 
    # reversed_lines_list = file_content[::-1]
    # In my solution i used a reversed function, it yields the lines in reverse order.
    # And i used a list function which basically converts the output of reversed function to a list.
    
    # Non hackers approach
    # try:
    #     with open(file_name, encoding='utf-8') as file:
    #         file_content = file.readlines()
    #         reversed_lines_list = list(reversed(file_content))
    #         return reversed_lines_list 
    # except OSError as e:
    #     print(f"An error occurred while reading the file: {e}")
    #     return []
    
    try:
        with open(file_name, encoding='utf-8') as file:
            return [line for line in reversed(file.readlines())]
    except OSError as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def main():
    # We here are getting the current opened dir path
    # We must do it if we are working locally on our machine.
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # current_dir is needed in file_path
    # print(current_dir)
    
    # Here we are combining current_dir path and our sampletext.txt path 
    # Also this is required when working locally on our machine
    # Otherwise we won't have access to the sampletext.txt file
    # file_path = os.path.join(current_dir, "sampletext.txt")
    # If you work locally you want to pass as argument file_path instead of "sampletext.txt"
    # print(file_path)
    
    file_contents = read_file("file/sampletext.txt")
    print(read_file_into_list("file/sampletext.txt"))
    write_first_line_to_file(file_contents, "./online.txt")
    print(read_even_numbered_lines("file/sampletext.txt"))
    print(read_file_in_reverse("file/sampletext.txt"))

if __name__ == "__main__":
    main()