def employee_details(name, employee_id, department, salary):
    return f"Name: {name}\nEmployee ID: {employee_id}\nDepartment: {department}\nSalary: {salary}"

if_name_ == "_main_":
    name = sys.argv[1]
    employee_id = sys.argv[2]
    department = sys,argv[3]
    salary = sys.argv[4]

    print("\Employee Details")
    print("----------------")
    print(employee_details(name, employee_id, department, salary))