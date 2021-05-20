import csv

def insert_details():
    emp_details = {"name": input("Enter the emp name \n"),
                   "Age": input("Enter the emp age \n"),
                   "Address": input("Enter the emp address \n")}
    emp_list.append(emp_details)


def print_details():
    for details in emp_list:
        print("------------------")
        print("name: {}\nage: {}\nAddress: {}\n".format(details["name"],details["Age"],details["Address"]))


def main():
    global emp_list
    emp_list = []
    insert_details()
    while True:
        input_info = input("Do you want to insert more:yes/no\n")
        if input_info == "yes":
            insert_details()
            continue
        else:
            print_details()
            break
    column_dict=["name","Age","Address"]
    csv_file_name = "employee_data.csv"
    with open(csv_file_name, 'w') as csvfile:
        #creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=column_dict)

        #writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(emp_list)


if __name__ == '__main__':
    main()
