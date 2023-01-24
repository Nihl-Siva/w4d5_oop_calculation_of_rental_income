class Property():
    def __init__(self):
        self.address = None
        self.income = 0
        self.expenses = 0
        self.total_investment = 0
        self.cashflow_monthly = 0
        self.cashflow_annual = 0
        self.roi = 0

    def add_prop(self):
        address = input("What is the address of the property? ")
        self.address = address  
        income = int(input("What is the monthly income of this propety? "))
        self.income = income
        expenses =  int(input("What are the monthly expenses of the propety? "))
        self.expenses = expenses
        total_investment = int(input("What is your total investment in this propety? "))
        self.total_investment = total_investment
        self.cashflow_monthly = income - expenses
        self.cashflow_annual = self.cashflow_monthly*12
        self.roi = (self.cashflow_annual/self.total_investment)*100
        self.show_prop()
    
    def show_prop(self):
        print("Your Property")
        print(f""""
        Address: {self.address}
        Income: {self.income}
        Expenses: {self.expenses}
        Total Investment: {self.total_investment}
        Monthly Cashflow: {self.cashflow_monthly}
        Annual Cashflow: {self.cashflow_annual}
        ROI: {self.roi}
        """)

    
class Main():
    def run():
        my_property = Property()
        print("Hello! Welcome to the Property ROI Calculator!")
        my_property.add_prop()
        

Main.run()