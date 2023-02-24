#This involves too files one named employees.py but I will keep one just commented out. 

"""
#!/opt/homebrew/bin/python3

class Employees:
    def __init__(self, name, department, role, salary, years_employeed):
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary
        self.years_employeed = years_employeed
    def eligible_for_retirement(self):
        if self.years_employeed >= 20:
            return True
        else:
            return False
"""

#!/opt/homebrew/bin/python3

from employees import Employees

e1 = Employees("Sam", "Sales", "Director of Sales", 100000, 20)
e2 = Employees("Tina", "Executive", "CIO", 150000, 10)

print(e1.name)
print(e2.name, e2.role, e2.salary)
