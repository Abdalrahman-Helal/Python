"""Write a Python list to a text file."""


def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
	        file.write(f"{item}\n")
	
# Test
cars = ["BMW" , "Mercedes", "Toyota", "Honda" , "VW"]
write_list_to_file("cars.txt", cars)
print("File created successfully!")