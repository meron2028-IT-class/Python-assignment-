income_of_a_person = float(input("Enter your total income: "))

def tax_for_an_income(income):
    if income <= 2000:
        tax_rate = 0
    elif income <= 4000:
        tax_rate = 0.15
    elif income <= 7000:
        tax_rate = 0.2
    elif income <= 10000:
        tax_rate = 0.25
    elif income <= 14000:
        tax_rate = 0.3
    else:
        tax_rate = 0.35


    tax_value_percent = income * tax_rate
    net_income = income - tax_value_percent

    return tax_value_percent, net_income

tax_value_percent, net_income = tax_for_an_income(income_of_a_person)


print(f"Tax Value: {tax_value_percent:}")
print(f"Net Income: {net_income:}")
