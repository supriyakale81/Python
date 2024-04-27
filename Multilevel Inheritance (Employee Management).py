"""Employee Management System:
Design a system with classes such as Employee as the base class, Manager and Developer
inheriting from Employee, and then a class like SeniorManager inheriting from Manager.
This setup can model an employee management system with various levels of hierarchy and
responsibilities."""

class employee:
    def __init__(self, employee_name,company_name):
        self.employee_name = employee_name
        self.company_name=company_name
        print(f"{self.employee_name} working in a {self.company_name} ")
class manager(employee):
    def __init__(self,manager_name,employee_name,company_name,department):
        self.manager_name=manager_name
        self.department=department
        super().__init__(employee_name,company_name)
    def manager_details(self):
        print(f"Name : {self.employee_name} \n Manager name : {self.manager_name} company : {self.company_name} \n Department : {self.department}")
class developer(employee):
    def __init__(self,employee_name,company_name, dev_department,salary,):
        self.dev_deprtment=dev_department
        self.salary=salary
        super().__init__(employee_name,company_name)
    def dev_details(self):
        print(f"Name : {self.employee_name} \n company : {self.company_name} \n Department : {self.dev_department}")
class senior_manager(manager):
    def __init__(self,seionr_manag_name,manager_name, employee_name,company_name,department):
        self.senior_manager_name=seionr_manag_name
        super().__init__(manager_name,employee_name,company_name,department)
    def senior_manager_details(self):
        print(f" Employee name : {self.employee_name}\n Manager name : {self.manager_name} \n senior manager Name : {self.senior_manager_name} \n company : {self.company_name} \n Department : {self.department}")


d=senior_manager("Rashmi","Rahul","riya","tcs","IT")
d.senior_manager_details()