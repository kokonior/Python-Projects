u=(input("ENTER MASTERPASSWORD "))
v=["1111"]
if(u!=v[0]):
    print("Access Denied")
    print("//Tip Enter Your Database Password//")
else:




    print("------------------------welcome--------------------")



    print("               /\ /\ /\ /\ /\ /\ /\ /\  ")
    print("               |_\__\__\__\__/__/__/__| ")
    print("               |                      | ")
    print("               | [[[[[[[      ]]]]]]] | ")
    print("               |  {_O_}        {_O_}  | ")
    print("               |          /           | ")
    print("               |         /            | ")
    print("               |        /__)          | ")
    print("               |    //////\\\\\\\\\\\\      | ") 
    print("               |     _____________    | ")
    print("               |     \__WELCOME__/    | ")               
    print("                \                    /  ") 
    print("                 \__________________/   ")

    print("I AM YOUR PASSWORD MANAGER, SIR")
    print()
    print()


    print("1.Show Passwords")
    print("2.Enter New Password")
    print("3.Delete Password")
    print("4.Update Password")
    print("5.About Us")
    print("6.Feedback")
    print("7.Exit")
    print()

    
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",\
        passwd=v[0])
    mycursor=mydb.cursor()  
    sql="create database if not exists manage_password ;"
    mycursor.execute(sql)
    mydb.commit()

    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",\
        passwd=v[0],database="manage_password")
    mycursor=mydb.cursor()  
    sql="create table if not exists manage (SerialNo int(5), Username varchar(20), Password varchar(20), \
        Email varchar(20), Website_App varchar(20));"
    mycursor.execute(sql)
    mydb.commit()
    

    a=int(input("Enter Your Option Sir: "))
    if(a==1):
        sql="select * from manage;"
        mycursor.execute(sql)
        r=mycursor.fetchall()
        print("-"*60)
        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format("SerialNo","Username", "Password", "Email", "Website_App"))
        print("-"*60)
        for x in r:
            print()
            print(x)

    if(a==2):
        b=[]
        serialno=input("Enter Serial No: ")
        b.append(serialno)
        print()
        username=input("Enter Username Sir: ")
        b.append(username)
        print()
        pword=input("Enter Password sir: ")
        b.append(pword)
        print()
        email=input("Enter Email sir: ")
        b.append(email)
        print()
        website=input("Enter Website/App Name sir: ")
        b.append(website)
        print()
        print()
        c=(b)
        sql="insert into manage values(%s,%s,%s,%s,%s)"
        mycursor.execute(sql,c)
        mydb.commit()
        print("Data Successfully Entered")


    if(a==3):
        print("1.Delete All Passwords")
        print()
        print("2.Delete Anyone Password")
        print()
        m=int(input("Enter Your Option Sir: "))
        if(m==1):
            mycursor.execute("delete from manage;")
            mydb.commit()
            print()
            print()
            print("Password Deleted Successfully")

        else:
            n=int(input("Enter Serial No : "))
            mycursor.execute("delete from manage where SerialNo=%s" %n)
            mydb.commit()
            print()
            print()
            print("Password Deleted Successfully")
        
    if(a==4):
        print("What Do You Want To Update")
        print()
        print("1.Update Serial No")
        print()
        print("2.Update Username ")
        print()
        print("3.Update Password")
        print()
        print("4.Update EmailId")
        print()
        print("5.Update Website/App name")
        print()
        print()

        o=int(input("Enter The Option Sir: "))
        print()
        if(o==1):
            print()
            f=input("Enter Old Serial Number ")
            print()
            g=input("Enter New Serial Number")
            sql="update manage set SerialNo=%s where SerialNo=%s"
            val=(g,f)
            mycursor.execute(sql,val)
            mydb.commit()
            print()
            print()
            print("Data Updated Successfully")

        if(o==2):
            f=input("Enter Serial Number ")
            g=input("Enter new Username")
            sql="update manage set Username=%s where SerialNo=%s"
            val=(g,f)
            mycursor.execute(sql,val)
            mydb.commit()
            print()
            print()
            print("Data Updated Successfully")

        if(o==3):
            f=input("Enter Serial Number ")
            g=input("Enter new Password")
            sql="update manage set Password=%s where SerialNo=%s"
            val=(g,f)
            mycursor.execute(sql,val)
            mydb.commit()
            print()
            print()
            print("Data Updated Successfully")

        if(o==4):
            f=input("Enter Serial Number ")
            g=input("Enter new Email")
            sql="update manage set Email=%s where SerialNo=%s"
            val=(g,f)
            mycursor.execute(sql,val)
            mydb.commit()
            print("Data Updated Successfully")

        if(o==5):
            f=input("Enter Serial Number ")
            g=input("Enter new Website/App Name")
            sql="update manage set Website_App=%s where SerialNo=%s"
            val=(g,f)
            mycursor.execute(sql,val)
            mydb.commit()
            print()
            print()
            print("Data Updated Successfully")



    if(a==5):
        print("We are a company of one People *\(^_^)/*")

    if(a==6):
        print("Give us feedback at Ultimate_security.com")
        print()
        print()
        print()
        print()
        print("Disclaimer above given website is not legit")
        print("(+_+)")


    if(a==7):
        mydb.close()

mydb.close()
        


        

            






