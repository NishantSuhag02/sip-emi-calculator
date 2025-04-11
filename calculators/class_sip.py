class sip():

    def __init__(self,monthly_investment, annual_rate, tenure_years):
        self.monthly_investment = monthly_investment
        self.annual_rate = annual_rate
        self.tenure_years = tenure_years

    def calculate_sip(self):
        r = self.annual_rate / 12 / 100
        n = self.tenure_years * 12

        future_value = self.monthly_investment * (((1 + r) ** n - 1) / r) * (1 + r)
        return round(future_value, 2)
