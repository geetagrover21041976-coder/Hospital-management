import mysql.connector as m1
try:
    con=m1.connect(host='localhost',username='root',password='your_password',database='project')
    cur= con.cursor()
    print("*"*20)
    print("TRINITY MULTI SPECIALITY HOSPITAL")
    print("*"*20)
except m1.error as err:
    print("Record not found")
#Definitions for all edits
def display_doc():
           
           cur=con.cursor()
           query='SELECT * FROM DOCTORS'
           cur.execute(query)
           result=cur.fetchall()
           for i in result:
               print(i)
def display_pat():
            cur=con.cursor()
            query='SELECT * FROM PATIENTS'
            cur.execute(query)
            result=cur.fetchall()
            for i in result:
                print(i)
def search_doc(no):
            cur=con.cursor()
            query="SELECT * FROM DOCTORS WHERE DOCTOR_ID=%s"
            cur.execute(query,(no,))
            result=cur.fetchall()
            if result!=None:
                print(result)
            else:
                print("Record not found")
def search_pat(no):
            cur=con.cursor()
            query="SELECT * FROM PATIENTS WHERE DOCTOR_ID=%s"
            cur.execute(query,(no,))
            result=cur.fetchall()
            if result!=None:
                print(result)
            else:
                print("Record not found")
def edit_pat():
           cur=con.cursor()
           print("What action would you like to perform?")
           print("A: Add new record")
           print("B: Delete a record")
           print("C: Update record")
           action=input("Enter your choice: ")
           if action=='A' or action=='a':
               name=input("Enter patient's name: ")
               age=int(input("Enter his/her age: "))
               gender=input("Enter gender: ")
               prob=input("What are they dealing with? ")
               doc_name=input("Doctor assigned: ")
               ward_fees=input("Enter ward fees: ")
               no=input("Enter no of days patient has been admitted: ")
               query="SELECT DOCTOR_ID FROM DOCTORS WHERE DOCTOR_NAME=%s"
               cur.execute(query,(doc_name,))
               
               ID=cur.fetchall()
               print("The details of this patient are: ",name,age,gender,prob,doc_name,ID)
               ID_add=input("Enter doctor ID you see on the screen: ")
               ward=input("Enter ward alloted: ")
               Query="INSERT INTO PATIENTS VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
               cur.execute(Query,(name,age,gender,prob,doc_name,ID_add,ward,ward_fees,no))
               con.commit()
               print("Record added successfully")
           elif action=='B' or action=='b':
                name=input("Enter patient's name: ")
                age=int(input("Enter his/her age: "))
                query= "SELECT * FROM PATIENTS WHERE Name=%s AND Age=%s"
                cur.execute(query,(name,age,))
                data=cur.fetchall()
                print("The details of the patient are: ",data)
                delete=input("Do you want to delete this? (y/n) ")
                if delete=='y' or delete=='Y':
                    Query='DELETE FROM PATIENTS WHERE NAME=%s AND AGE=%s'
                    cur.execute(Query,(name,age,))
                    con.commit()
                    print("Record deleted successfully")
                else:
                    print("Deletion cancelled. Returning to main menu...")
           elif action=='C' or action=='c':
               #age=int(input("Enter his/her age: "))
                 print("The columns available to change are:")
                 print(" 1:Name\n 2:Age\n 3:Problem\n 4:Ward_Alloted")
                 action=input("Enter the no. adjacent to your choice: ")
                 if action=='1':
                     name=input("Enter patient's name: ")
                     new_name=input("Enter patient's new name: ")
                     query='UPDATE PATIENTS SET NAME=%s WHERE NAME=%s'
                     cur.execute(query,(new_name,name,))
                     con.commit()
                     print("Record updated successfully")
                 elif action=='2':
                     name=input("Enter patient's name: ")
                     age=input("Enter patient's age: ")
                     new_age=input("Enter patient's new age: ")
                     query='UPDATE PATIENTS SET AGE=%s WHERE NAME=%s AND AGE=%s'
                     cur.execute(query,(new_age,name,age,))
                     con.commit()
                     print("Record updated successfully")
                 elif action=='3':
                     name=input("Enter patient's name: ")
                     prob=input("Enter the previous symptom: ")
                     new_prob=input("Enter the new issue: ")
                     query='UPDATE PATIENTS SET PROBLEM=%s WHERE NAME=%s AND PROBLEM=%s'
                     cur.execute(query,(new_prob,name,prob,))
                     con.commit()
                     print("Record updated successfully")
                 elif action=='4':
                     name=input("Enter patient's name: ")
                     age=input("Enter patient's age: ")
                     ward=input("Enter previous ward: ")
                     new_ward=input("Enter the change in ward: ")
                     query='UPDATE PATIENTS SET WARD_ALLOTED=%s WHERE NAME=%s AND WARD_ALLOTED=%s'
                     cur.execute(query,(new_ward,name,ward,))
                     con.commit()
                     print("Record updated successfully")
                 else:
                     print("Input error. Try again")
def bill_cal():
    ID=input("Enter doctor's id: ")
    ward=input("Enter ward: ")
    name=input("Enter patient's name: ")
    query="select fees from doctors where doctor_id =%s"
    cur.execute(query,(ID,))
    cost1=cur.fetchone()
    query="SELECT WARD_FEES FROM PATIENTS WHERE Ward_Alloted=%s"
    cur.execute(query ,(ward,))
    cost2=cur.fetchone()
    query=" select no_of_days from patients where name=%s"
    cur.execute(query,(name,))
    no=cur.fetchone()
    if int(no[0])>7:
        cost=cost1[0]*2 + cost2[0]*int(no[0])
    else:
        cost=cost1[0]+ cost2[0]*int(no[0])
    print("The total bill calculated is ",cost)
#Program starts here basically
print("Which table would you like to refer?")
print("A: Doctor table")
print("B: Patients table")
while True:
    choice=input("Enter your choice: ")
    #Code for doctors' table
    if choice=='A' or choice =='a':
        print("Redirecting to the Admin block...")
        print('What action would you like to perform? ')
        print('A: Display')
        print('B: Search')
        action=input("Enter your choice: ")
        if action=='A' or action=='a':
            display_doc()
        elif action=='B' or action=='b':
            no=input("Enter Doctor's ID to search: ")
            search_doc(no)
    #Code for patients' table
    elif choice=='B' or choice=='b':
        print("Redirecting to the Patient block...")
        print('What action would you like to perform? ')
        print('A: Display')
        print('B: Search')
        print('c: Edit')
        print('D: Bill Calcultion')
        action=input("Enter your choice: ")
        if action=='A' or action=='a':
            display_pat()
        elif action=='B' or action=='b':
            no=input("Enter Doctor's ID to search: ")
            search_pat(no)
        elif action=='C' or action=='c':
            edit_pat()
        elif action=='d' or action=='D':
            bill_cal()
    else:
        print("Choose again")
        
    
