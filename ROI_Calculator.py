
class propertyROI():
    """
    A class for calculating the Return on Investment (ROI) of a rental property.
    
    Attributes:
    - expenses (int): the total monthly expenses of the property
    - income (int): the total monthly income of the property
    
    Methods:
    - calculate_income: prompts the user for the monthly rental, laundry, storage, and miscellaneous income, and returns the total income
    - calculate_expenses: prompts the user for various monthly expenses, such as taxes, insurance, utilities, and mortgage, and returns the total expenses
    - calculate_cash_flow: calculates the monthly cash flow of the property (income - expenses) and returns it
    - calculate_roi: prompts the user for various costs, such as down payment, closing costs, and rehab budget, and calculates the ROI of the property (annual net income / total invested * 100), returning it
    
    Example usage:
    prop = propertyROI()
    prop.calculate_income()
    prop.calculate_expenses()
    prop.calculate_cash_flow()
    prop.calculate_roi()
    """
    def __init__(self):
        self.expenses = 0
        self.income = 0
    
        
    def calculate_income(self):
        print('\nPlease fill in the following information')
        print("Please do NOT use a comma ',' to separate digits. EXAPMLE: 50000 \n")
        while True:
            try:
                rental_income = int(input("Monthly rent income: $"))
                laundry_income = int(input("Monthly laundry income: $"))
                storage_income = int(input("Monthly storage income: $"))
                misc_income = int(input("Monthly other income: $"))
                break
            except ValueError:
                print("Please enter a valid integer.")

        self.income = rental_income + laundry_income + storage_income + misc_income
        return self.income

    def calculate_expenses(self):
        print('\nPlease fill in the following information')
        print("Please do NOT use a comma ',' to separate digits. EXAPMLE: 50000 \n")
        while True:
            try:
                taxes = int(input("Annual taxes: $"))
                insurance = int(input("Monthly insurance: $"))
                utilities = int(input("Monthly utility: $"))
                electric = int(input("Monthly electric: $"))
                water = int(input("Monthly water: $"))
                sewer = int(input("Monthly sewer: $"))
                trash = int(input("Monthly trash: $"))
                gas = int(input("Monthly gas: $"))
                HOA = int(input("Monthly HOA fee? $"))
                landscape = int(input("Monthly landscape: $"))
                vacancy = int(input("Monthly vacancy savings: $"))
                repairs = int(input("Monthly repair savings: $"))
                CapEx = int(input("Monthly CapEx: $"))
                property_managment = int(input("Monthly property managment: $"))
                mortgage = int(input("Monthly mortgage: $"))
                break
            except ValueError:
                print("Please enter a valid integer.")

        self.expenses = taxes + insurance + utilities + electric + water + sewer + trash + gas + HOA + landscape + vacancy + repairs + CapEx + mortgage + property_managment
        return self.expenses

    def calculate_cash_flow(self):
        if self.expenses == 0 and self.income == 0:
            print("\nWe need your expenses and income first.")
            return None
        elif self.expenses == 0:
            print("\nWe need your expenses first")
            return None
        elif self.income == 0:
            print("\nWe need your income first.")
            return None
        else:
            cash_flow = self.income - self.expenses
            cashflow = cash_flow
            return cashflow

    def calculate_roi(self):
        print('\nPlease fill in the following information')
        print("Please do NOT use a comma ',' to separate digits. EXAPMLE: 50000 \n")
        if self.expenses == 0 and self.income == 0:
            print("\nWe need your expenses and income first.")
            return None
        elif self.expenses == 0:
            print("\nWe need your expenses first")
            return None
        elif self.income == 0:
            print("\nWe need your income first.")
            return None
        while True:
            try:
                down_payment = int(input("Down payment: $"))
                closing_cost = int(input("Closing cost: $"))
                rehab_budget = int(input("Total rehab budget: $"))
                misc_other = int(input("Other costs included: $"))
                break
            except ValueError:
                print("not a valid integer.")

        total_invested = down_payment + closing_cost + rehab_budget + misc_other
        annual_income = self.income * 12
        annual_expenses = self.expenses * 12
        net_income = annual_income - annual_expenses
        roi = (net_income / total_invested) * 100
        return roi
                
        
property1 = propertyROI()

def runProgram():

    while True:
        response1 = input(f"\nType 'Q' to quit 'I' for monthly income 'E' for expenses 'C' for cash flow 'R' for ROI: ")
        if response1.upper() == "I":
            income_ = property1.calculate_income()
            print (f"\nThe income for this property is ${income_}")
        elif response1.upper() == "E":
            expenses_ = property1.calculate_expenses()
            print(f"\nYour monthly expenses are ${expenses_}")
        elif response1.upper() == "C":
            cash_flow_ = property1.calculate_cash_flow()
            print(f"\nYour cash flow is ${cash_flow_}")
        elif response1.upper() == "R":
            roi = property1.calculate_roi()
            print(f"\nThe ROI for this property is {roi}%")
        elif response1.upper() == "Q":
            break
runProgram()