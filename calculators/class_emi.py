class emi():

    def __init__(self,principal_amount, annual_rate, tenure_years):
        self.principal_amount = principal_amount
        self.annual_rate = annual_rate
        self.tenure_years = tenure_years

    def calculate_emi(self):
        monthly_rate = self.annual_rate / 12 / 100
        months = self.tenure_years * 12
        
        monthly_emi = (self.principal_amount * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
        return round(monthly_emi, 2)