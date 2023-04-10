class Property():
    """
    The Property class asks for a user to input the 
    total_invested, monthly_income and monthly_expenses 
    as in integer with no commas seperating the digits
    and will return the users ROI as a float

    """
    def __init__(self, total_invested, monthly_income, monthly_expenses):
        self.total_invested = total_invested
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses
        
    def calculate_roi(self):
        annual_rent = self.monthly_income * 12
        annual_expenses = self.monthly_expenses * 12
        net_income = annual_rent - annual_expenses
        roi = (net_income / self.total_invested) * 100
        return roi

print("\nPlease do NOT use a comma ',' to separate digits. EXAPMLE: 50000 \n")
property1 = Property(int(input("What is the total invested? ")), 
                         int(input("What is your total monthly income? ")), 
                         int(input("What are your monthly expenses? ")))


roi = property1.calculate_roi()
print(f"\nThe ROI for this property is {roi}%")
