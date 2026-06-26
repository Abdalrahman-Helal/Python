#write a Python program to count the Number of words in a file.

def count_words_in_file(file_path):
    with open(file_path , 'r' ) as file:
            f = file.read()
            word_count = len(f.split())
    return word_count
#example usage:
file_path = 'sample.txt'  
count = count_words_in_file(file_path)
print(f"The number of words in the file '{file_path}' is: {count}")



    