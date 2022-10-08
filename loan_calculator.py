#loan_principal = 'Loan principal: 1000'
#final_output = 'The loan has been repaid!'
#first_month = 'Month 1: repaid 250'
#second_month = 'Month 2: repaid 250'
#third_month = 'Month 3: repaid 500'

# write your code here
#print(loan_principal)
#print(first_month)
#print(second_month)
#print(third_month)
#print(final_output)
import math
import argparse
import sys

loan_calculation = argparse.ArgumentParser(description="This program calculates value related to credits.")
loan_calculation.add_argument("--type", choices=["annuity", "diff"], help= "choose the type of payment between annuity or diff")
loan_calculation.add_argument("--payment", type = int, default = 0, help= "monthly payment amount")
loan_calculation.add_argument("--principal", type = int, default = 0, help = "the loan principal")
loan_calculation.add_argument("--periods", type = int, default = 0, help = "number of months needed to repay the loan")
loan_calculation.add_argument("--interest", type = float, default = 0, help="monthly interest rate")

args = loan_calculation.parse_args()

if((args.payment >= 0) and (args.principal >= 0) and (args.periods >= 0) and (args.interest > 0) and (len(sys.argv) == 5) and (args.interest != 0)):
    if args.type == "diff":
        if args.payment == 0:
            m = 1
            P = args.principal
            i = args.interest / (12*100)
            n = args.periods
            sum_pay = 0
            while m <= args.periods:
                diff_month_pay = math.ceil(P / n + i * (P-P*(m-1)/n))
                print(f"Month {m} payment is : {diff_month_pay}")
                sum_pay += diff_month_pay
                m += 1
            overpayment = P - sum_pay
            print(f"Overpayment : {overpayment}")
        else:
            print("Incorrect parameters")
    
    elif args.type == "annuity":
        if args.periods == 0:
            calculation = "n"

        elif args.payment == 0:
            calculation = "a"
            
        elif args.principal == 0:
            calculation = "p"
        
        if calculation == 'n':  #calculating the number of monthly payments
            loan_principal = args.principal #P
            monthly_payment = args.payment  #A
            loan_interest = args.interest #i
            nominal_int_rate = loan_interest / (12 * 100)  #anually to monthly
            
            no_periods = math.ceil(math.log((monthly_payment/(monthly_payment - nominal_int_rate * loan_principal)),(1 + nominal_int_rate)))
            
            if no_periods <= 1:
                print(f"It will take {no_periods} month to repay the loan")
            elif no_periods < 12:
                print(f"It will take {no_periods} months to repay the loan")
            else:
                print(f"It will take {no_periods//12} years and {no_periods%12} months to repay this loan!")
            
            overpayment = monthly_payment * no_periods - loan_principal
            print(f"Overpayment : {overpayment}")
        
                
        elif calculation == 'a':  #calculating the monthly payment (the annuity payment)
            
            loan_principal = args.principal  #P
            no_periods = args.periods  #n
            loan_interest = args.interest  #i
            nominal_int_rate = loan_interest / (12 * 100)  #anually to monthly
            i = nominal_int_rate
            monthly_payment = math.ceil(loan_principal *  (i*math.pow(1+i,no_periods)/(math.pow(1+i,no_periods)-1)))
            print(f"Your monthly payment = {monthly_payment}!")
            overpayment = monthly_payment * no_periods - loan_principal
            print(f"Overpayment : {overpayment}")
        
        else: #calculating the loan principal
            monthly_payment = args.payment
            no_periods = args.periods
            loan_interest = args.interest
            nominal_int_rate = loan_interest / (12 * 100)  #anually to monthly
            i = nominal_int_rate
        
            loan_principal = math.ceil(monthly_payment / ((i*math.pow(1+i,no_periods)/(math.pow(1+i,no_periods)-1))))
            print(f"Your loan principal = {loan_principal}!")
            overpayment = monthly_payment * no_periods - loan_principal
            print(f"Overpayment : {overpayment}")
    
    
    else:
        print("Incorrect parameters")

else:
    print("Incorrect parameters")

