#!/usr/bin/env python
# coding: utf-8

# # login page

# In[ ]:


import mysql.connector
mydb = mysql.connector.connect(
      host='localhost',
      user='root',
      password='manu1234',
      database='MANU_DB',
      auth_plugin = 'mysql_native_password'
)

mycursor = mydb.cursor()

sql="select User_ID from User_Details"
mycursor.execute(sql)
myresult=mycursor.fetchall()
final=[]
for x in myresult:
    final.append(x[0])
    
code="select Password from User_Details"
mycursor.execute(code)
myresult=mycursor.fetchall()
last=[]
for x in myresult:
    last.append(x[0])
    
def choose1():
    print("===== MC TOURISM =====")
    print("1.login")
    print("2. create a new account")
    choose=int(input("choose a option="))
    if choose==1:
        print("login")
        def usr_pswd():
            userid=input("Enter the username= ")
            password=input("Enter the password= ")
            a=0
            for i in final:
                if userid==final[a] and password==last[a]:
                    print("loginned successfully")
                    break
                a=a+1
                    
                    
            else:
                print("invalid details- please try again")
                return usr_pswd()
        usr_pswd()

    elif choose==2:
        list=[]

        print("create a new account")

        upper_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        lower_case=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        decimal=['0','1','2','3','4','5','6','7','8','9']

        special_character=['@','!','#','$','%','^','&']

    
        def firstname():
            first_name=input("enter the first name=")
            for i in first_name:
                for j in special_character:
                    if i==j:
                        print("invalid first name -please enter a valid name")
                        return firstname()
                else:
                    continue
            else:
                for a in first_name:
                    for b in decimal:
                        if a==b:
                            print("invalid first name -please enter a valid name")
                            return firstname()
                    else:
                        continue
                else:
                    list.append(first_name)
                    return secondname()

        def secondname():
            second_name=input("enter the second name=")
            for i in second_name:
                for j in special_character:
                    if i==j:
                        print("invalid second name -please enter a valid name")
                        return secondname()
                else:
                    continue
        
            else:
                for e in second_name:
                    for f in decimal:
                        if e==f:
                            print("invalid second name -please enter a valid name")
                            return secondname()
                    else:
                        continue
                else:
                    list.append(second_name)
                    return mobile()

        def mobile():
                mbn=input("Enter mobile number=")
                if len(mbn)==10:
                    if mbn[0]=='9' or mbn[0]=='8' or mbn[0]=='7' or mbn[0]=='6':
                        if mbn[1]=='9'or mbn[1]=='8'or mbn[1]=='7'or mbn[1]=='6'or mbn[1]=='5'or mbn[1]=='4'or mbn[1]=='3'or mbn[1]=='2'or mbn[1]=='1'or mbn[1]=='0':
                            if mbn[2]=='9'or mbn[2]=='8'or mbn[2]=='7'or mbn[2]=='6'or mbn[2]=='5'or mbn[2]=='4'or mbn[2]=='3'or mbn[2]=='2'or mbn[2]=='1'or mbn[2]=='0':
                                if mbn[3]=='9'or mbn[3]=='8'or mbn[3]=='7'or mbn[3]=='6'or mbn[3]=='5'or mbn[3]=='4'or mbn[3]=='3'or mbn[3]=='2'or mbn[3]=='1'or mbn[3]=='0':
                                    if mbn[4]=='9'or mbn[4]=='8'or mbn[4]=='7'or mbn[4]=='6'or mbn[4]=='5'or mbn[4]=='4'or mbn[4]=='3'or mbn[4]=='2'or mbn[4]=='1'or mbn[4]=='0':
                                        if mbn[5]=='9'or mbn[5]=='8'or mbn[5]=='7'or mbn[5]=='6'or mbn[5]=='5'or mbn[5]=='4'or mbn[5]=='3'or mbn[5]=='2'or mbn[5]=='1'or mbn[5]=='0':
                                            if mbn[6]=='9'or mbn[6]=='8'or mbn[6]=='7'or mbn[6]=='6'or mbn[6]=='5'or mbn[6]=='4'or mbn[6]=='3'or mbn[6]=='2'or mbn[6]=='1'or mbn[6]=='0':
                                                if mbn[7]=='9'or mbn[7]=='8'or mbn[7]=='7'or mbn[7]=='6'or mbn[7]=='5'or mbn[7]=='4'or mbn[7]=='3'or mbn[7]=='2'or mbn[7]=='1'or mbn[7]=='0':
                                                    if mbn[8]=='9'or mbn[8]=='8'or mbn[8]=='7'or mbn[8]=='6'or mbn[8]=='5'or mbn[8]=='4'or mbn[8]=='3'or mbn[8]=='2'or mbn[8]=='1'or mbn[8]=='0':
                                                        if mbn[9]=='9'or mbn[9]=='8'or mbn[9]=='7'or mbn[9]=='6'or mbn[9]=='5'or mbn[9]=='4'or mbn[9]=='3'or mbn[9]=='2'or mbn[9]=='1'or mbn[9]=='0':
                                                            list.append(mbn)
                                                            return userid()
                                                        else:
                                                            print("Invalid mobile number- please enter a valid number")
                                                            return mobile()
                                                    else:
                                                        print("Invalid mobile number- please enter a valid number")
                                                        return mobile()
                                                else:
                                                    print("Invalid mobile number- please enter a valid number")
                                                    return mobile()
                                            else:
                                                print("Invalid mobile number- please enter a valid number")
                                                return mobile()
                                        else:
                                            print("Invalid mobile number- please enter a valid number")
                                            return mobile()
                                    else:
                                        print("Invalid mobile number- please enter a valid number")
                                        return mobile()
                                else:
                                    print("Invalid mobile number- please enter a valid number")
                                    return mobile()
                            else:
                                print("Invalid mobile number- please enter a valid number")
                                return mobile()
                        else:
                            print("Invalid mobile number- please enter a valid number")
                            return mobile()
                    else:
                        print("Invalid mobile number- please enter a valid number")
                        return mobile()
                else:
                    print("Invalid mobile number- please enter a valid number")
                    return mobile()


        def userid():

            user_id=input("Enter a user_id=")



            for m in user_id:
                for n in upper_case:
                    if m==n:
                        break
                else:
                    continue
                break
            else:
                print("There should be atleast one uppercase")


            for  k in user_id:
                for l in lower_case:
                    if k==l:
                        break
                else:
                    continue
                break
            else:
                print("There should be atleast one lowercase")



            if len(user_id)<8:
                 print("There should be atleast 8 characters ")
            else:
                pass

            for i in final:
                if i==user_id:
                    print("user_id already exists- try a different user_id")
                    return userid()
            else:
                list.append(user_id)  
                for m in user_id:
                    for n in upper_case:
                        if m==n:
                            for  k in user_id:
                                for l in lower_case:
                                    if k==l and len(user_id)>=8:
                                        return pwd()
                                else:
                                    continue    
                            else:
                                print("invalid user_id")
                                return userid()
                    else:
                        continue   
                else:
                    print("invalid user_id")
                    return userid()

        def pwd():    #creating a function pwd()

            password=input("enter a password=")  

            for i in password:            # to check does the password have a decimal       
                for j in decimal:                
                    if i==j:                     
                        break               
                else:
                    continue
                break
            else:
                print("There should be atleast one decimal")


            for m in password:          # to check does the password have a upper case
                for n in upper_case:
                    if m==n:
                        break
                else:
                    continue
                break
            else:
                print("there should be atleast one uppercase")


            for  k in password:         # to check does the password have a lower case
                for l in lower_case:
                    if k==l:
                        break
                else:
                    continue
                break
            else:
                print("there should be atleast one lowercase")


            for q in password:         # to check does the password have a special character
                for r in special_character:
                    if q==r:
                        break
                else:
                    continue
                break    

            else:
                print("there should be atleast one special character")


            if len(password)<8:      # to check does the password have sufficient length 
                print("There should be atleast 8 characters ")
            else:
                pass

            for i in password:      # to check the password is valid or not
                for j in decimal:
                    if i==j:
                        for m in password:
                            for n in upper_case:
                                if m==n:
                                    for  k in password:
                                        for l in lower_case:
                                            if k==l:
                                                for q in password:
                                                    for r in special_character:
                                                        if q==r and len(password)>=8:
                                                            list.append(password)
                                                            print("your account has created successfully")
                                                            break
                                                    else:
                                                        continue
                                                    break
                                                else:
                                                    print("invalid- please try a valid password")
                                                    return pwd()
                                                break        
                                        else:
                                            continue
                                        break    
                                    else:
                                        print("invalid- please try a valid password")
                                        return pwd()
                                    break    
                            else:
                                continue
                            break    
                        else:
                            print("invalid- please try a valid password")
                            return pwd()
                        break    
                else:
                    continue
                break    
            else:
                print("invalid- please try a valid password ")
                return pwd()
            
            sql = "INSERT INTO User_Details(First_Name, Last_Name,Mobile,User_ID,Password) VALUES(%s,%s,%s,%s,%s)"
            val = (list[0],list[1],list[2],list[3],list[4])
            mycursor.execute(sql,val)
            mydb.commit()
        firstname()
    else:
        print(" invalid choice--choose a valid option")
        return choose1()  
        
choose1()

    


# # ATM

# In[264]:


import mysql.connector
mydb = mysql.connector.connect(
       host='localhost',
       user='root',
       password='manu1234',
       database='MANU_DB',
       auth_plugin = 'mysql_native_password')

mycursor = mydb.cursor()   






def ATM():
    global Account_number
    Account_number=input("Enter your account number= ")
    
    PIN=int(input("please enter your four digit PIN="))
    
    sql="SELECT PIN FROM ATM"
    mycursor.execute(sql)
    list1=[]
    for i in mycursor:
        list1.append(i[0])
                
    sql="SELECT Account_number FROM ATM"
    mycursor.execute(sql)
    list2=[]
    for i in mycursor:
        list2.append(i[0])
    a=0
    for i in list1:
        if PIN==list1[a] and Account_number==list2[a]:
            return choose1()
        a=a+1
    else:
        print("invalid bank details- please try again")
        return ATM()
        
def choose1():
    print("1.withdrawal \n2.balance enquiry\n3.PIN change\n4.Debit")
    choose=int(input("choose an operation:"))
    
    if choose==1:
        return amount1()

    elif choose==2:
        return balance()
     

    elif choose==3:
        return new_pin()
    
    elif choose==4:
        return debit()
        
    else:
        print("choose a valid operation")
        return choose1()
    
def amount1():
    sql="SELECT Balance FROM ATM WHERE Account_number=%s"
    val=(Account_number,)
    mycursor.execute(sql,val)
    list3=[]
    for i in mycursor:
        list3.append(i[0])
    Balance=list3[0]    
    
    available_cash_atm=200000
    amount=int(input("enter the amount="))
    if amount%100==0:
        if amount<=available_cash_atm:
            if amount<=Balance:
                print("please collect your cash:",amount)
                Available_balance= Balance-amount
                print("availabale balance=",Available_balance)
                sql = "UPDATE ATM SET Balance = %s WHERE Account_number = %s"
                val=(Available_balance,Account_number)
                mycursor.execute(sql,val)
                mydb.commit()
            else:
                print("you have insufficient funds in your account")
                return amount1()
        else:
            print("this machine is out of cash\nplease try entering the less amount")
            return amount1()
    else:
        print("please enter the amount in 100 denominations")
        return amount1()
    
def balance():
    sql="SELECT Balance FROM ATM WHERE Account_number=%s"
    val=(Account_number,)
    mycursor.execute(sql,val)
    list3=[]
    for i in mycursor:
        list3.append(i[0])
    Balance=list3[0]
    print(" Available Balance=",Balance)
    
def new_pin():
    NEW_PIN=int(input("Enter the new four digit pin="))
    sql = "UPDATE ATM SET PIN = %s WHERE Account_number = %s"
    val=(NEW_PIN,Account_number)
    mycursor.execute(sql,val)
    mydb.commit()
    print("successfully updated your PIN")
    
def debit():
    sql="SELECT Balance FROM ATM WHERE Account_number=%s"
    val=(Account_number,)
    mycursor.execute(sql,val)
    list3=[]
    for i in mycursor:
        list3.append(i[0])
    Balance=list3[0] 
    
    debit_amount=int(input("Insert the amount="))
    Balance=Balance+debit_amount
    sql = "UPDATE ATM SET Balance = %s WHERE Account_number = %s"
    val=(Balance,Account_number)
    mycursor.execute(sql,val)
    mydb.commit()
    print("your amount is debited successfully")


# In[268]:


ATM()


# In[263]:


import mysql.connector
mydb = mysql.connector.connect(
       host='localhost',
       user='root',
       password='manu1234',
       database='MANU_DB',
       auth_plugin = 'mysql_native_password')

mycursor = mydb.cursor()

x="SELECT * FROM ATM"
mycursor.execute(x)
for i in mycursor:
    print(i)


# In[ ]:




