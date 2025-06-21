import sqlite3
file_name='hospital.db'
def setup_database():
    conn=sqlite3.connect(file_name)
    cursor=conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients
               (id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER, 
                address TEXT,
                phone TEXT,
                disease TEXT)
               ''')
    conn.commit()
    conn.close()
def create_record():
    name = input("Name:")
    while True:
        try:
            age = int(input("Age:"))
            if 0<=age<=120:
                break
            else:
                print("Invalid age")
        except ValueError:
            print("Please enter a valid age")
    address = input("Address:")
    while True:
        phone = input("Enter the phone number: ")
        if len(phone)==10:
            break
        else:
            print("Invalid phone number")
    disease = input("Disease:")
    conn=sqlite3.connect(file_name)
    cursor=conn.cursor()
    cursor.execute("INSERT INTO patients VALUES (NULL,?,?,?,?,?)",(name,age,address,phone,disease))
    conn.commit()
    conn.close()
    print("Record added")
def view_record():
    conn=sqlite3.connect(file_name)
    cursor=conn.cursor()
    for row in cursor.execute("SELECT * FROM patients"):
        print(f"ID:{row[0]},Name:{row[1]}, Age:{row[2]}")
        print(f"Address:{row[3]},Phone:{row[4]},Disease:{row[5]}")
    conn.close()
def update_record():
    patient_id = input("Enter patient ID to update:")
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE id=?", (patient_id,))
    patient = cursor.fetchone()
    if not patient:
        print("Patient not found")
        return
    print(f"1. Name: {patient[1]}")
    print(f"2. Age: {patient[2]}")
    print(f"3. Address: {patient[3]}")
    print(f"4. Phone: {patient[4]}")
    print(f"5. Disease: {patient[5]}")
    choice = input("Enter field number to update (1–5) or 'all':")
    if choice=='1' or choice=='all':
        new_name=input("New name: ") or patient[1]
    else:
        new_name = patient[1]
    if choice=='2' or choice=='all':
         while True:
            try:
                new_age = int(input(f"New age:")) or patient[2]
                if 0 <= new_age <= 120:
                    break
                else:
                    print("Invalid age")
            except ValueError:
                print("Please enter a valid age")
    else:
        new_age=(patient[2])
    if choice=='3' or choice=='all':
        new_address= input("New address:") or patient[3]
    else:
        new_address=patient[3]
    if choice=='4' or choice=='all':
        while True:
            new_phone = input("New phone:") or patient[4]
            if len(new_phone)==10:
                break
            print("Invalid phone number")
    else:
        new_phone=patient[4]
    if choice=='5'or choice=='all':
        new_disease=input("New disease:") or patient[5]
    else:
        new_disease=patient[5]
    cursor.execute('''UPDATE patients SET name=?, age=?, address=?, phone=?, disease=? WHERE id=?''',(new_name, new_age, new_address, new_phone, new_disease, patient_id))
    conn.commit()
    conn.close()
    print("Record updated")
def delete_record():
    patient_id = input("Enter patient ID to delete:")
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id=?",(patient_id,))
    conn.commit()
    conn.close()
    print("Record deleted")
