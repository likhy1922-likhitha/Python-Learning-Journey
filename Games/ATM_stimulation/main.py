'''
intial balance :10,000
then show the menu
--> check balance
--> Deposit
--> Withdraw
--> Exit
use select an option
perform the selected opeartion
repeate menu until user chooses exit
'''
intial_balance =10000


# user = int(input("Select the any option: "))



while True:
    print("ATM Menu")
    print("1.Check balance.")
    print("2.Deposit")
    print("3.withdraw")
    print("4.Exit")
    user = int(input("Select the any option: "))
    if(user==1):
        print(f"{intial_balance} is your current account balance")
        print("_______________________________________________")
        
    elif(user==2):
        amount = int (input("Enter the amount to deposit: "))
        Total_amount = amount+intial_balance
        print(f"{Total_amount} is the current account balance")
        print("_______________________________________________")

        
    elif(user==3):
        
        withdraw_amount = int(input("Enter the amount to withdraw: "))
        if(withdraw_amount<=intial_balance):
            withdraw = intial_balance-withdraw_amount
            final_amount = withdraw
            print(f"{final_amount} is the remaining balance")
            print("_______________________________________________")
        else:
            print("insufficent balance!")
            print("_______________________________________________")
        
        
    elif(user==4):
        print("Thank you Vist again!!")
        break
    
    else:
        print("Something went wrong")
        

        




