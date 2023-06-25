import mysql.connector
import datetime
from datetime import datetime


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="bakalarska_praca"
)

mycursor = mydb.cursor()


def man_input(input, value):
    sql = "INSERT INTO man_vstupy (absolutna_adresa, hodnota, cas) VALUES(%s,%s,%s)"
    now = datetime.now()
    timeNow = dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    val =(input, value, timeNow)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted to table man_vstupy.")

def man_output(output, value):
    sql = "INSERT INTO man_vystupy (absolutna_adresa, hodnota, cas) VALUES(%s,%s,%s)"
    now = datetime.now()
    timeNow = dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    val =(output, value, timeNow)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted to table man_vystupy.")

def man_memory(memory, value):
    sql = "INSERT INTO man_vystupy (absolutna_adresa, hodnota, cas) VALUES(%s,%s,%s)"
    now = datetime.now()
    timeNow = dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    val =(memory, value, timeNow)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted to table man_memory.")

def tr_input(input, value):
    sql = "INSERT INTO tr_vstupy (absolutna_adresa, hodnota, cas) VALUES(%s,%s,%s)"
    now = datetime.now()
    timeNow = dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    val =(input, value, timeNow)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted to table tr_vstupy.")

def tr_output(output, value):
    sql = "INSERT INTO tr_vystupy (absolutna_adresa, hodnota, cas) VALUES(%s,%s,%s)"
    now = datetime.now()
    timeNow = dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    val =(output, value, timeNow)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted to table tr_vystupy.")

def tr_memory(memory, value):
    sql = "INSERT INTO tr_vystupy (absolutna_adresa, hodnota, cas) VALUES(%s,%s,%s)"
    now = datetime.now()
    timeNow = dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    val =(memory, value, timeNow)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted to table tr_memory.")

def alarms(input1,input2,value):
    sql = "INSERT INTO chyby(snimac1, snimac2, nazov_chyby, cas_chyby) VALUES(%s,%s,%s,%s)"
    now = datetime.now()
    timeNow = dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    val = (input1, input2, value, timeNow)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted to table alarmy.")

#def man_output():