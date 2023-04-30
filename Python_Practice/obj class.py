class Employee:
    department_name="Technical"
    
    def __init__(self,rcv_emp_id,rcv_salary,rcv_mgr_id)->None:
        self.emp_id=rcv_emp_id
        self.emp_salary=rcv_salary
        self.mgr_id=rcv_mgr_id
        print(f"{self} was created successfully with values {rcv_emp_id},{rcv_salary},{rcv_mgr_id}")
        
    def get_emp_salary(self):
        return self.emp_salary
    
    def set_emp_salary (self,rcv_salary):
        self.emp_salary = rcv_salary
    
    @classmethod 
    def get_department_name(cls,rcv_departmentname):
        cls.department_name = rcv_departmentname
                
    
    @staticmethod
    def field_expertice():
        print("Employees Expertise are \n1) C,C++\n2)Linux\n3)Python\n")
    
def main():
    print("I am in main")

    employee= Employee(100,1000,1)
    print(employee.emp_id)
    print(employee.emp_salary)
    print(employee.mgr_id)
    print("Before set call ", employee.get_emp_salary())
    employee.set_emp_salary(20000)
    print("After set call ", employee.get_emp_salary())

    print("Employee Department name is",employee.department_name)
    


    employee.field_expertice()
main()
        
        # 1) create an object employee(100,1000,1)  
        # 2) do the following for the created object
        # // direct access using .notation
        # empid
        # emp_salary
        # mgr_id
        # 3) print the department name 
        # 4) display the expertise for the employees 