print("-"*60)

customerNames=["teja","balaji","dhanush","karthik","shalini"]

customerPins=["1234","1212","5646","4564","5664"]#eg:1234=teja pin,1212=balajipin etc

customerBalances=[10000,20000,25000,8000,50000]#eg:10000=teja balance so on

customerAccno=[120106001,120106002,120106003,120106004,120106005]

deposition=0
withdrawal=0
balance=0
flag=True
lst_index_count=5
i=0

#this statement below helps the program to run continuously

while flag:
    print("="*60)
    print("-----------------Welcome to Kiran Bank----------------")
    print("******************************************************")
    print("=<<-----    1. Open a New Account                  >>=")
    print("=<<         2. Withdraw Money                      >>=")
    print("=<<         3. Deposit Money                       >>=")
    print("=<<         4. Check Customer Balance              >>=")
    print("=<<         5. Exit/Quit                           >>=")
    print("******************************************************")
    # print("            PLEASE SELECT(1-5) FROM ABOVE             ")

    #the below statement takes the choice from user.
    choiceNumber=input(" PLEASE SELECT(1-5) FROM ABOVE: ")
    if choiceNumber=="1":
        print("Choice Number 1 is selected by the customer")

        #The line below will take the the no of customers from the user
        noc=eval(input("Number Of Customers:"))#eval evaluates numbers in string eg:a="1+1"=1+1 but a=eval("1+1")=2
        i=i+noc

        #the if condition will restrict the number of new accounts to 5.
        if i>5:
            print("\n")
            print("Customer registration exceeded its reach")
            i=i-noc
        else:
            #the while loop will run acc to the no of customers
            while True:
                #the lines below will take information from customers

                name=input("Enter your FullName here :")
                customerNames.append(name)#the name we gave will  be appended to customerNames list  that we have created in the beginning
                accno=int(input("enter account number:"))
                customerAccno.append(accno)#the accno we gave will  be appended to customerAccno list  that we have created in the beginning

                pin=input("please enter a pin of your choice:")
                customerPins.append(pin)#the pin we gave will  be appended to customerPins list  that we have created in the beginning

                balance=0
                deposition=int(input("Please Enter your Deposit Amount"))#1000
                balance=balance+deposition #0+1000=1000
                customerBalances.append(balance)##the balance we have will  be appended to customerBalance list  that we have created in the beginning

                # lst_index_count=5 in list we have 0-4 indexes so when we append this name will become 5 and lst_index_count=5 it prints present givenname
                print("Name=", customerNames[lst_index_count])
                print("Accno=",customerAccno[lst_index_count])
                print("Pin=", customerNames[lst_index_count])
                print("Balance=",customerBalances[lst_index_count],"-/Rs")
                print("Your NAME,PIN,MONEY is added to the customer system")
                print("------------NEW ACCOUNT CREATED SUCCESSFULLY-------------")
                lst_index_count = lst_index_count + 1  # now it changes from 5 to 6 so that next when we enter the new customer and print using lst_indx_count we get that customer name
                break
    elif choiceNumber=="2":
        j=0
        print("Choice Number 2 is selected by the customer")
        while j<1:
            k=-1 #becuz list index starts from 0
            name=input("please enter your account name :")
            accno=int(input("please enter your account number :"))
            pin=input("please enter your pin")
            j=j+1
        #this while loop will keep the function running when variable k is smaller than the length of customerNames list
        while k< len(customerNames)-1:
            k=k+1
            ''' for eg balaji is index 1 but initial value of k=-1 later it became k=0(k=k+1)
                if name==customerNames[k] that means it checks if the name(input) we have given in above code 
                starting k=0 if will become false and control goes to the for loop again k<len(customer)-1==0<5-1
                0<4 now k value becomes 1(k=k+1) now the if condition will be true so it executes the if statement
                same for accno==customerAccno[k] and pin==customerPins[k] afterwards the loop runs until k value becomes >len(customerNames)
                 and control moves to the main while loop we have written in beginning'''

            if name==customerNames[k]:
                if accno==customerAccno[k]:
                    if pin==customerPins[k]:
                        j=j+1
                        print("Your Current Balance :",customerBalances[k],"-/Rs")
                        balance=customerBalances[k]
                        withdrawal=int(input("enter your withdraw amount:"))
                        if withdrawal>balance:
                            print("Your withdrawal amount is greater than your Bank Balance ")
                        else:
                            balance=balance-withdrawal #1000-500=500
                            print("\n")
                            print("-------------------------WITHDRAW SUCCESSFUL--------------------------------")
                            customerBalances[k]=balance
                            print("Your Current Balance :",balance,"-/Rs")


    elif choiceNumber=="3":
        print("Choice Number 3 is selected by the customer")
        n=0
        while n<1:
            k=-1
            name=input("enter your account name:")
            accno=int(input("enter your account number"))
            pin=int(input("enter your pin"))













