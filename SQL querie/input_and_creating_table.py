import sqlite3
conn=sqlite3.connect('customer_data.db')
c=conn.cursor()


 
def patient_details():
     name=input("Enter name of the customer")
     customer_id=input("Enter customer ID")
     cust_open_date=input("Enter date(dd/mm/yyyy) of customer Enrolled ")
     last_consult=input("Enter last date(dd/mm/yyyy) customer consulted")
     vac_type=input("Enter type of vaccination")
     doct_name=input("Enter name of the doctor consulted ")
     state=input("Enter  name of state ")
     country=input("Enter name of country")
     post_code=input("Enter  postal code")
     dob=input("Enter date of birth of customer(dd/mm/yyy)") 
     active_cust=input("Enter active status of the customer")

     c.execute("CREATE TABLE IF NOT EXISTS patient_details1 (customer_name TEXT,customer_id	INTEGER, open_date	INTEGER, last_consulted_date INTEGER, vaccination_id TEXT, doctor_name	TEXT,states	TEXT, country	TEXT,dob INTEGER, is_active TEXT)")

     c.execute("INSERT INTO patient_details1 VALUES(?,?,?,?,?,?,?,?,?,?)",(name,customer_id,cust_open_date,last_consult,vac_type,doct_name,state,country,dob,active_cust))
     conn.commit( )
     c.close()
     conn.close()
    
patient_details()




