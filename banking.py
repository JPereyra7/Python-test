initialInvestment = input("Enter the initial investment amount: ")
annualInterestRate = input("Enter the annual interest rate (in %): ")
years = input("Enter the number of years: ")
# Convert inputs to appropriate types
annualInterestRate = float(annualInterestRate)
initialInvestment = float(initialInvestment)
# Convert percentage to decimal
annualInterestRate = (annualInterestRate / 100)
years = int(years)
# Compounding formula: future value=initial×(1+rate)^years
futurevalue = initialInvestment * (1 + annualInterestRate) ** years
print(f"The future value of the investment is: {futurevalue:.0f} SEK")