import mysql.connector
import matplotlib.pyplot as plt


mydb = mysql.connector.connect(

  host="", #whatever you named generally localhost

  user="", #whatever you named generally root

  password="", #enter your own password

  database="med" #enter your database(DB) name, this is my DB name here in this parameter

)
cursor = mydb.cursor()

print()
 
print("******//////------WELCOME   TO   MEDICAL   STORE   INVENTORY   MANAGEMENT------\\\\\\******")

print()

def create_tables():
    cursor.execute("CREATE TABLE  IF NOT EXISTS doc_det(did int PRIMARY KEY AUTO_INCREMENT, doc_name VARCHAR(20),  depname VARCHAR(20), salary DECIMAL(10,2))")
    cursor.execute("CREATE TABLE IF NOT EXISTS pat_det (pid INT  PRIMARY KEY AUTO_INCREMENT, pname VARCHAR(20), address VARCHAR(50), phno INT, did INT, foreign key(did) references doc_det(did), age INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS room_det (rid INT  PRIMARY KEY AUTO_INCREMENT, rtype VARCHAR(20), price INT, status VARCHAR(20))")
    cursor.execute("CREATE TABLE IF NOT EXISTS billgenerator (billno  INT PRIMARY KEY AUTO_INCREMENT, pid INT, foreign key(pid) references pat_det(pid), rid INT, foreign key(rid) references room_det(rid) , date_of_add DATE, date_of_dis DATE, time_of_add TIME, time_of_dis TIME, totalcost INT, days int)")
    mydb.commit()
create_tables()    

def insert_doc_det():
    query = "INSERT INTO doc_det (doc_name, depname, salary) VALUES ( %s, %s, %s)"
    doc_name=input("Enter doctor name")
    depname=input("Enter department name")
    salary=int(input("Enter doctor's salary"))
    values = ( doc_name, depname, salary)
    cursor.execute(query, values)
    mydb.commit()
    print("Data inserted successfully into doc_det table")

# Function to insert data into pat_det table
def insert_pat_det():
    query = "INSERT INTO pat_det (pname, address, phno, did, age) VALUES ( %s, %s, %s, %s, %s)"
    pname=input("Enter patient name")
    address=input("Enter patient address")
    phno=int(input("Enter phone num"))
    did=int(input("Enter doc's id"))
    age=int(input("Enter age"))
    values = (pname, address, phno, did, age)
    cursor.execute(query, values)
    mydb.commit()
    print("Data inserted successfully into pat_det table")

# Function to insert data into room_det table
def insert_room_det():
    query = "INSERT INTO room_det (rtype, price, status) VALUES (  %s, %s, %s)"
    rtype=input("Enter room type")
    price=int(input("Enter price of the room"))
    status=input("Enter the status of room")
    values = (rtype, price, status)
    cursor.execute(query, values)
    mydb.commit()
    print("Data inserted successfully into med_det table")

# Function to delete data from doc_det table
def delete_doc_det():
    query = "DELETE FROM doc_det WHERE did = %s"
    did=input("Enter doctor id whose record you want to delete")
    values = [did]
    cursor.execute(query, values)
    mydb.commit()
    print("Data deleted successfully from doc_det table")

# Function to delete data from pat_det table
def delete_pat_det():
    query = "DELETE FROM pat_det WHERE pid = %s"
    pid=input("Enter patient id whose record you want to delete")
    values = [pid]
    cursor.execute(query, values)
    mydb.commit()
    print("Data deleted successfully from patient_det table")

# Function to delete data from med_det table
def delete_room_det():
    query = "DELETE FROM room_det WHERE rid = %s"
    rid=int(input("Enter room id whose record you want to delete"))
    values = [rid]
    cursor.execute(query, values)
    mydb.commit()
    print("Data deleted successfully from med_det table")

# Function to update data in doc_det table
def update_doc_det():
    query = "UPDATE doc_det SET doc_name = %s, depname = %s, salary = %s WHERE did = %s"
    did=input("Enter doctor id")
    doc_name=input("Enter doctor name")
    depname=input("Enter department name")
    salary=input("Enter salary")
    values = [doc_name, depname, salary, did]
    cursor.execute(query, values)
    mydb.commit()
    print("Data updated successfully in doc_det table")

# Function to update data in patient_det table
def update_pat_det():
    query = "UPDATE pat_det SET pname = %s, address = %s, phno = %s, did = %s, age = %s WHERE pid = %s"
    pid=input("Enter patient id")
    pname=input("Enter patient name")
    address=input("Enter patient address")
    phno=int(input("Enter phone num"))
    did=int(input("Enter doc's id"))
    age=int(input("Enter age"))
    values = (pname, address, phno, did, age, pid)
    cursor.execute(query, values)
    mydb.commit()
    print("Data updated successfully in pat_det table")

# Function to update data in med_det table
def update_room_det():
    query = "UPDATE room_det SET rtype = %s,  price = %s, status = %s WHERE rid = %s"
    rid=input("Enter room id")
    rtype=input("Enter room type")
    price=input("Enter price of the room")
    status=input("Enter the status of room")
    values = (rtype, price, status, rid)
    cursor.execute(query, values)
    mydb.commit()
    print("Data updated successfully in room_det table")

# Function to search data in doc_det table
def search_doc_det():
    query = "SELECT * FROM doc_det WHERE did = %s"
    did=int(input("Enter the doctor id whose record you want to find"))
    values=(did,)
    cursor.execute(query, values)
    result = cursor.fetchall()
    for data in result:
        print("did:", data[0])
        print("doc_name:", data[1])
        print("dep_no:", data[2])
        print("depname:", data[3])

# Function to search data in pat_det table
def search_pat_det():
    query = "SELECT * FROM pat_det WHERE pid = %s"
    pid=int(input("Enter patient id whose record you want to search"))
    values = (pid,)
    cursor.execute(query, values)
    result = cursor.fetchall()
    for data in result:
        print("pid:", data[0])
        print("pname:", data[1])
        print("address:", data[2])
        print("phno:", data[3])
        print("did:", data[4])
        print("age:", data[5])
        
# Function to search data in med_det table
def search_room_det():
    query = "SELECT * FROM room_det WHERE rid = %s"
    rid=int(input("Enter room id"))
    values = (rid,)
    cursor.execute(query, values)
    result = cursor.fetchall()
    for data in result:
        print("rid:", data[0])
        print("rtype:", data[1])
        print("price:", data[2])
        print("status", data[3])

# Function to search data in billgen table
def search_billgenerator():
    query = "SELECT * FROM billgenerator WHERE billno = %s"
    billno = int(input("Enter bill number: "))
    values = (billno,)
    cursor.execute(query, values)
    result = cursor.fetchall()
    for data in result:
        print("billno:", data[0])
        print("pid:", data[1])
        print("rid:", data[2])
        print("date_of_add:", data[3])
        print("time_of_add:", data[4])
        print("date_of_dis:", data[5])
        print("time_of_dis:", data[6])
        print("totalbill:", data[7])

# Function to display data in doc_det table
def display_doc_det():
    query = "SELECT * FROM doc_det"
    cursor.execute(query)
    result = cursor.fetchall()
    print("did\tdoc_name\tdep_no\tdepname")
    for data in result:
        print(data[0], "\t", data[1], "\t", data[2], "\t", data[3])

# Function to display data in pat_det table
def display_pat_det():
    query = "SELECT * FROM pat_det"
    cursor.execute(query)
    result = cursor.fetchall()
    print("pid\tpname\taddress\tphno\tdid\tage")
    for data in result:
        print(data[0], "\t", data[1], "\t", data[2], "\t", data[3], "\t", data[4], "\t", data[5])

# Function to display data in med_det table
def display_room_det():
    query = "SELECT * FROM room_det"
    cursor.execute(query)
    result = cursor.fetchall()
    print("rid\trtype\tprice\tstatus")
    for data in result:
        print(data[0], "\t", data[1], "\t", data[2], "\t", data[3])

#Function to display data in billgen table
def display_billgenerator():
    query = "SELECT * FROM billgenerator"
    cursor.execute(query)
    result = cursor.fetchall()
    print("Bill No\tPatient Id\tRoom Id\tDate of Admission\tTime of Admission\tDate of Discharge\tTime of Discharge\tTotal Bill")
    for data in result:
        print(*data)

#Generate graph for all the rooms vacant or in use in the hospital
def generate_graph():
    deluxe = int(input("Enter total number of deluxe rooms: "))
    semi = int(input("Enter total number of patient semi rooms: "))
    labour = int(input("Enter total number of patient labour wards: "))
    asylum = int(input("Enter total number of patient mental asylum rooms: "))
    general = int(input("Enter total number of patient general wards: "))
    ventilator = int(input("Enter total number of patient ventilator rooms: "))
    operation = int(input("Enter total number of patient operation theatre: "))
 
    room_types = ['Deluxe', 'Semi', 'General', 'Ventilator', 'Operation']
    patients = [deluxe, semi, general, ventilator, operation]
 
    plt.bar(room_types, patients, color='green')
    plt.xlabel("Room Types") #x axis of graph
    plt.ylabel("Number of patients") #y axis of graph
    plt.title("Number of patients Using Different Room Types in a Hospital") #graph title
 
    plt.show() #to show/display the graph

#This is used to insert record into billgenerator table at the time of admission
def admission():
    display_pat_det()
    print("The entries of the patient table are as above")
    print("Choose the record on which you want to admit the patient")
    
    quer = "SELECT * FROM room_det WHERE status='available'"
    cursor.execute(quer)
    result = cursor.fetchall()
    print("Rooms with available status are as follows:")
    for row in result:
        print(row)
    pid = int(input("Enter patient id: "))
    rid = int(input("Enter room id: "))
    que="SELECT status from room_det WHERE rid=%s"
    cursor.execute(que,(rid,))
    res=cursor.fetchone()
    for i in res:
        if i == 'unavailable':
            print("Room is not available")
    time_of_add = input("Enter time of admission (hh:mm:ss): ")
    date_of_add = input("Enter date of admission (YYYY-MM-DD): ")
    query="INSERT INTO billgenerator (pid, rid, date_of_add, date_of_dis, time_of_add, time_of_dis, totalcost) VALUES (  %s, %s, %s,  %s, %s, %s, %s)"
    val=(pid, rid, date_of_add, None , time_of_add, None, None)
    cursor.execute(query, val)
    mydb.commit()
    query="update room_det set status='unavailable' where rid=%s"
    cursor.execute(query, (rid,))
    mydb.commit()
    print("The room's status has been updated")
    qu="select billno from billgenerator where pid=%s"
    cursor.execute(qu, (pid,))
    result=cursor.fetchone()
    print("Bill No. of the patient is", result[0])
    mydb.commit()

#This is used to insert record into bill generator at the time of discharge
def dischargeandbill():

    display_room_det()
    
    print("The entries of the patient table and room table are as above")
    print("Choose the record on which you want to conduct discharge and generate bill")

    # Get the bill no from the billgenerator table based on the patient id and room id
    billno=int(input("Enter the bill number from the billgenerator table above whose time of discharge and date of discharge you want to update"))
    quey = "SELECT * from billgenerator WHERE billno=%s"
    cursor.execute(quey,(billno,))
    r=cursor.fetchone()
    
    time_of_dis = input("Enter time of discharge (hh:mm:ss): ")
    date_of_dis = input("Enter date of discharge (YYYY-MM-DD): ")
    days=int(input("Enter number of days"))
    
    quera = "UPDATE billgenerator SET date_of_dis=%s, time_of_dis=%s, days=%s WHERE billno=%s"
    values=(date_of_dis, time_of_dis,days, billno)
    cursor.execute(quera, values)
    quy="select * from billgenerator where billno=%s"
    cursor.execute(quy, (billno,))
    result = cursor.fetchone()
    print("THE BILL")
    print("Bill No\tPatient Id\tRoom Id\tDate of Admission\tTime of Admission\tDate of Discharge\tTime of Discharge\tTotal Bill")
    print(result)
    mydb.commit()

    # Calculate the total bill
    rid = int(input("Enter room id: "))
    queryi = "SELECT price FROM room_det WHERE rid = %s"
    cursor.execute(queryi, (rid,))
    result = cursor.fetchone()
    pric = result[0]
    price = int(pric)
    print("Price of room with id", rid, "is", price)
    mydb.commit()
    totalcost = days * price
    print("The total bill of the patient is", totalcost)

    # Update the billgenerator table with the calculated values 
    querya = "UPDATE billgenerator SET  totalcost=%s WHERE billno=%s"
    cursor.execute(querya, (totalcost, billno))
    query="update room_det set status='available' where rid=%s"
    cursor.execute(query, (rid,))
    print("The room's status has been updated")
    mydb.commit()
    
    
#Admin authorities
def admin():
    print()
    print("CHOOSE ANY ONE COMMAND AT A TIME FROM THE CHOICES BELOW")
    print("1 - Insert data into any table") 
    print("2 - Delete data from any table")
    print("3 - Update data of any table")
    print("4 - Search data from any table")
    print("5 - Display data from any table")
    print("6 - Print Graphs for all the rooms in the hospital")
    print("7 - To Admit patient")
    print("8 - To Discharge and Generate the bill of the user")
    ch=int(input("Enter anyone choice from above:"))
    if ch==1:
        print("1 - To insert into doctor record table")
        print("2 - To insert into patient record table")
        print("3 - To insert into room record table")
        q1=int(input("Enter you choice from above"))
        if q1==1:
            insert_doc_det()
        elif q1==2:
            insert_pat_det()
        elif q1==3:
            insert_room_det()
    elif ch==2:
        print("1 - To delete from doctor record table")
        print("2 - To delete from patient record table")
        print("3 - To delete from room record table")
        q2=int(input("Enter your choice from above"))
        if q2==1:
            delete_doc_det()
        elif q2==2:
            delete_pat_det()
        elif q2==3:
            delete_room_det()
    elif ch==3:
        print("1 - To update doctor record table")
        print("2 - To update patient record table")
        print("3 - To update room record table")
        q3=int(input("Enter your choice from above"))
        if q3==1:
            update_doc_det()
        elif q3==2:
            update_pat_det()
        elif q3==3:
            update_room_det()
    elif ch==4:
        print("1 - To search from doctor record table")
        print("2 - To search from patient record table")
        print("3 - To search from room record table")
        print("4 - To search from bill generator table")
        q4=int(input("Enter your choice from above"))
        if q4==1:
            search_doc_det()
        elif q4==2:
            search_pat_det()
        elif q4==3:
            search_room_det()
        elif q4==4:
            search_billgenerator()
    elif ch==5:
        print("1 - To display records from doctor record table")
        print("2 - To display records from patient record table")
        print("3 - To display records from room record table")
        print("4 - To display records from bill generator table")
        q5=int(input("Enter your choice from above"))
        if q5==1:
            display_doc_det()
        elif q5==2:
            display_pat_det()
        elif q5==3:
            display_room_det()
        elif q5==4:
            display_billgenerator()
    elif ch==6:
        generate_graph()
    elif ch==7:
        admission()
    elif ch==8:
        dischargeandbill()

        
#Staff authorities
def staff():
    print()
    print("CHOOSE ANY ONE COMMAND AT A TIME FROM THE CHOICES BELOW")
    print("1 - Search data from any table")
    print("2 - Display data from any table")
    print("3 - To Admit patient")
    print("4 - To Discharge and Generate the bill of the user")
    cho=int(input("Enter anyone choice from above:"))
    if cho==1:
        print("1 - To search from doctor record table")
        print("2 - To search from patient record table")
        print("3 - To search from room record table")
        print("4 - To search from bill generator table")
        q4=int(input("Enter your choice from above"))
        if q4==1:
            search_doc_det()
        elif q4==2:
            search_patient_det()
        elif q4==3:
            search_med_det()
        elif q4==4:
            search_billgenerator()
    elif cho==2:
        print("1 - To display records from doctor record table")
        print("2 - To display records from patient record table")
        print("3 - To display records from room record table")
        print("4 - To display records from bill generator table")
        q5=int(input("Enter your choice from above"))
        if q5==1:
            display_doc_det()
        elif q5==2:
            display_patient_det()
        elif q5==3:
            display_med_det()
        elif q5==4:
            display_billgenerator()
    elif cho==3:
        admission()
    elif cho==4:
        dischargeandbill()

#Login either as staff of admin
def login():
    print("LOGIN MENU")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(" LOGIN AS EITHER ADMIN OR STAFF")
    # for admin the username is admin and the password is admin1
    # for staff the username is staff and the password is staff2
    username=input("Enter your username")
    password=input("Enter your password")
    if username=='admin':
        if password=='admin1':
            print("YOU HAVE SUCCESSFULLY LOGGED!!! YOUR ROLE IS ADMIN")
            print()
            while True:
                admin()
                que=input("Do you want to continue[n/N to exit]")
                if que.lower()=='n':
                    break
        else:
            print("Oops!!! WRONG PASSWORD, Enter valid password")
    elif username=='staff':
        if password=='staff2':
            print("YOU HAVE SUCCESSFULLY LOGGED IN!!! YOUR ROLE IS STAFF")
            print()
            while True:
                staff()
                que=input("Do you want to continue[n/N to exit]")
                if que.lower()=='n':
                    break
                else:
                    continue
        else:
            print("Oops!!! WRONG PASSWORD, Enter valid password")
    else:
        print("Oops!!! WRONG USERNAME, Enter valid username")

login()
while True:
    ques=input("LOGIN AGAIN [n to exit]")
    if ques.lower()=='n':
        break
    else:
        login()
                
    
