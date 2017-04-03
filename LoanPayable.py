def loan_Payable(Amount,rate,time):
    '''input -> float
       output -> float
    '''

    Amount = float(input("Enter the loan amount:"))
    rate = float(input("Enter the interest rate:"))
    time = float(input("Enter time:"))


    solution = (Amount * rate * time) + Amount

    return solution

print (loan_Payable(100000,0.12,12))

