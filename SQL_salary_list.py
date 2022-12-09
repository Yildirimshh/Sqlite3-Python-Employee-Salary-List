import sqlite3


db = sqlite3.connect("WorkerSalaryData.db")

authority = db.cursor()
First_Name = input("First Name:")
Last_Name = input("Last Name:")
Birthday = input("Birthday Date:")
Jop_Title = input("Job Title:")
Salary = input('Salary Amout:')

print(f"Process Completed, New Employee Name:{First_Name},{Last_Name}")

authority.execute("CREATE TABLE IF NOT EXISTS WorkerSalaryData (First Name,Last Name,Birthday,Jop Title,Salary)")
authority.execute(f'INSERT INTO WorkerSalaryData VALUES("{First_Name}","{Last_Name}","{Birthday}","{Jop_Title}","{Salary}")')

write = authority.fetchall()

while True:

    qtn = input("1-Add Employee:\n2-Open Employee Salary List\n")
    if qtn == "1":
        First_Name = input("First Name:")
        Last_Name = input("Last Name:")
        Birthday = input("Birthday Date:")
        Jop_Title = input("Job Title:")
        Salary = input("Salary Amout:")
        authority.execute(f"INSERT INTO WorkerSalaryData VALUES('{First_Name}','{Last_Name}','{Birthday}','{Jop_Title}','{Salary}')")
        db.commit()
        print(f"Process Completed, New Employee Name:{First_Name},{Last_Name}")
        
    elif qtn == "2":
        authority.execute("SELECT *FROM WorkerSalaryData")
        write = authority.fetchall()
        db.commit()
       
        say = 1
        for i in write:
            print("--------Employee Information--------")
            print(f"{say}:First Name:{i[0]}\nLast Name:{i[1]}\nSalary Amout:{i[2]}\n")
            say+=1
        a = input("Want To Continue? Yes/No:").lower()
        if a == "yes":
            continue
            print("user typed yes")
        else:
            break
            print("****Thank You****")




