
import pandas as pd

data = {
    "Name": ["Ram","Sam","Prabhu"],
    "Account Number": [989389381 ,9893893898 , 9893893871],
    "Account Type": ["SB", "CA", "SB"],
    "Adhaar_No": [959389389173, 959389389179, 959389389159],
    "Balance": [8989839, 7690990, 989330]
}

df = pd.DataFrame(data)
df.to_csv("SBIAccountHolder.csv",index=False)
def append_record():
    name = input("Enter the name of the account holder: ")
    account_number = int(input("Enter the account number: "))
    if(df[df["Account Number"]==account_number].empty==False):
        print("Account number already exists")
        return
        
    account_type = input("Enter the account type: ")

    adhaar_number = int(input("Enter the adhaar number: "))
    balance = int(input("Enter the balance: "))
    df = pd.read_csv("SBIAccountHolder.csv")
    df = df.append({"Name":name,"Account Number":account_number,"Account Type":account_type,
                    "Adhaar_No":adhaar_number,"Balance":balance},ignore_index=True)
    df.to_csv("SBIAccountHolder.csv",index=False)
    print("Record appended successfully")
    
def delete_record():
    account_number = int(input("Enter the account number to delete: "))
    df = pd.read_csv("SBIAccountHolder.csv")
    if(df.empty):
        print("No records to delete")
    elif(df[df["Account Number"]==account_number].empty):
        print("Record not found")
    else:
        df = df[df["Account Number"]!=account_number]
        df.to_csv("SBIAccountHolder.csv",index=False)
        print("Record deleted successfully")
    
def credit():
    account_number = int(input("Enter the account number to credit: "))
    amount = int(input("Enter the amount to credit: "))
    df = pd.read_csv("SBIAccountHolder.csv")
    if(df.empty):
        print("No records to credit")
    elif(df[df["Account Number"]==account_number].empty):
        print("Record not found")
    else:
        df.loc[df["Account Number"]==account_number,"Balance"] += amount
        df.to_csv("SBIAccountHolder.csv",index=False)
        print("Amount credited successfully")
    
def debit():
    account_number = int(input("Enter the account number to debit: "))
    amount = int(input("Enter the amount to debit: "))
    df = pd.read_csv("SBIAccountHolder.csv")
    if(df.empty):
        print("No records to debit")
    elif(df[df["Account Number"]==account_number].empty):
        print("Record not found")
    elif(df[df["Account Number"]==account_number]["Balance"].values[0]-amount<0 and df[df["Account Number"]==account_number]["Account Type"].values[0]=="SB"):
            print("Insufficient balance")
    else:
        df.loc[df["Account Number"]==account_number,"Balance"] -= amount
        df.to_csv("SBIAccountHolder.csv",index=False)
        print("Amount debited successfully")

def print_record():
    account_number = int(input("Enter the account number to print: "))
    df = pd.read_csv("SBIAccountHolder.csv")
    if(df.empty):
        print("No records to print")
    
    elif(df[df["Account Number"]==account_number].empty):
        print("Record not found")
    else:
        
        print(df[df["Account Number"]==account_number])
        print("Record printed successfully")
    
    
option=0

while(option!=6):
    print("1. Append Record")
    print("2. Delete Record")
    print("3. Credit")
    print("4. Debit")
    print("5. Print Record")
    print("6. Exit")
    option = int(input("Enter your option: "))
    if(option==1):
        append_record()
    elif(option==2):
        delete_record()
    elif(option==3):
        credit()
    elif(option==4):
        debit()
    elif(option==5):
        print_record()
    elif(option==6):
        print("exited successfully")
    else:
        print("Invalid option")
        

        
    
