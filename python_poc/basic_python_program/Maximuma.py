def input_of_numbers():

    a=input("Enter first number")
    b=input("Enter second number")
    print("User input \n first number :{} \n second number :{}".format(a,b))
    return a,b


def maximuma(a,b):
    first_number = a
    second_number = b
    if first_number>second_number:
        print("first number {} is greater then second number {}".format(first_number,second_number))
    else:
        print("second  number {} is greater then first number {}".format(second_number,first_number))

def main():
    a,b=input_of_numbers()
    maximuma(a,b)

main()