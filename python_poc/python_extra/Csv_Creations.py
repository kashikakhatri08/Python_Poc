import csv

#employee details
column_dict = ["emp_id","emp_name","emp_age","emp_state"]
rows_dict =[{"emp_id":1,"emp_name":"kashika","emp_age":23,"emp_state":"rajasthan"}
    ,{"emp_id":1,"emp_name":"Sam","emp_age":23,"emp_state":"rajasthan"}
    ,{"emp_id":2,"emp_name":"Ryan","emp_age":26,"emp_state":"Pune"}
    ,{"emp_id":3,"emp_name":"Will","emp_age":24,"emp_state":"Karnataka"}
    ,{"emp_id":4,"emp_name":"Anne","emp_age":28,"emp_state":"Kerla"}
    ,{"emp_id":5,"emp_name":"Jhon","emp_age":25,"emp_state":"Bangal"}]

csv_file_name = "employee_details.csv"
with open(csv_file_name, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=column_dict)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(rows_dict)

