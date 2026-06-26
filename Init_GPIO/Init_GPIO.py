# Write python code to generate Init function of GPIO for AVR.

port_name = input("Enter port name (for example PORTA): ").strip().upper()
ddr_value = ""

for bit in range(7, -1, -1):
    mode = input(f"Please enter Bit {bit} mode (in/out): ").strip().lower()
    while mode not in ["in", "out"]:
        print("Invalid input. Please enter 'in' or 'out'.")
        mode = input(f"Please enter Bit {bit} mode (in/out): ").strip().lower()
    if mode == "in":
        ddr_value += "0"
    else:
        ddr_value += "1"
code = f"void Init_{port_name}_DIR (void)\n{{\n    DDR{port_name[-1]} = 0b{ddr_value};\n}}\n" 

with open("Init_GPIO.c", "w") as file:
	file.write(code)

print(code)





# Generate GPIO Initialization Function for AVR
# Get and validate port name
# port_name = input("Enter port name (PORTA, PORTB, PORTC, PORTD): ").strip().upper()

# while port_name not in ["PORTA", "PORTB", "PORTC", "PORTD"]:
#     print("Invalid port! Please enter PORTA, PORTB, PORTC, or PORTD.")
#     port_name = input("Enter port name: ").strip().upper()

# ddr_value = ""

# # Get mode for each bit (Bit7 -> Bit0)
# for bit in range(7, -1, -1):
#     mode = input(f"Please enter Bit {bit} mode (in/out): ").strip().lower()

#     # Validate input
#     while mode not in ["in", "out"]:
#         print("Invalid input. Please enter 'in' or 'out'.")
#         mode = input(f"Please enter Bit {bit} mode (in/out): ").strip().lower()

#     if mode == "in":
#         ddr_value += "0"
#     else:
#         ddr_value += "1"

# # Generate C code
# code = f"""void Init_{port_name}_DIR(void)
# {{
#     DDR{port_name[-1]} = 0b{ddr_value};
# }}
# """

# # Write to file (creates it if it doesn't exist)
# with open("Init_GPIO.c", "w", encoding="utf-8") as file:
#     file.write(code)

# print("\nGenerated C Code:\n")
# print(code)
# print("The file 'Init_GPIO.c' has been created successfully.")