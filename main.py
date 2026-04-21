## write a python function which will take user input as a number and will print the table of that number


def print_table():
    num = int(input("Enter a number: "))
    
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

print_table(10)