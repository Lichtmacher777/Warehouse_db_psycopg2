import psycopg2


def get_warehouse_detail(warehouse_id):
    conn = psycopg2.connect(dbname="dci_db", user="postgres",
                            password="postgres", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM warehouse WHERE warehouse_id=%s",
                (warehouse_id,))
    warehouse = cur.fetchone()
    cur.close()
    conn.close()
    return warehouse


def get_employee_detail(employee_id):
    conn = psycopg2.connect(dbname="dci_db", user="postgres",
                            password="postgres", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee WHERE employee_id=%s", (employee_id,))
    employee = cur.fetchone()
    cur.close()
    conn.close()
    return employee


# Next, iterate record/resultSet to print all column values
warehouse = get_warehouse_detail(2)
print('Printing Warehouse record')
print('Warehouse ID: ', warehouse[0])
print('Warehouse Name: ', warehouse[1])
print('Employee Count: ', warehouse[2])

employee = get_employee_detail(105)
print('Printing Employee record')
print('Employee ID: ', employee[0])
print('Employee Name: ', employee[1])
print('Warehouse ID: ', employee[2])
print('Joining Date: ', employee[3])
print('speciality: ', employee[4])
print('Salary: ', employee[5])
print('Experience: ', employee[6])
