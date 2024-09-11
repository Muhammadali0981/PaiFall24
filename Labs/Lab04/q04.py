class employee:

    def get_data(self):
        self.name, self.salary, self.tax = input("enter details: ").split()

    def Salary_after_tax(self):
        print(int(self.salary) - int(self.salary) * float(self.tax))

    def update_tax_percentage(self):
        tax: float = float(input("enter new tax "))
        self.tax = tax


e1 = employee()
e1.get_data()
e1.Salary_after_tax()

e1.update_tax_percentage()
e1.Salary_after_tax()