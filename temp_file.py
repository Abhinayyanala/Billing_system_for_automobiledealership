import mysql.connector
from mysql.connector import Error
import datetime

db = {
  'host': 'localhost',
  'port': 3307,
  'user': "root",
  'password': "abhi@123",
  'database': "tata"
}

def __connect_database():
  try:
    conn = mysql.connector.connect(**db)
    if(conn.is_connected()):
      print('Database successfully connected!')
      return conn
  except Error as e:
    print(f'Error:{e}')
    return None
  
def insert_customer(customer: str, phone: int, bill_date):
  conn = __connect_database()
  if conn:
    try:
      cursor = conn.cursor()
      sql = "INSERT INTO bills (customer, phone, billdate) VALUES (%s, %s, %s)"
      val = (customer, phone, bill_date)
      cursor.execute(sql, val)
      conn.commit()
      print(f"{customer} data successfully!")
    except Error as e:
      print(f"Error: {e}")
      return None
def emi_calculator(price, dpamt, emi_period: int ):
  principal= price-dpamt
  rate= 0.12
  emi = (principal * rate *(1 + rate)**emi_period ) / ((1 + rate)**(emi_period)-1)
  return emi

def generate_receipt(billid, datebill, customer, car, dpamt,paymode, emiperiod: int,phone,price):
  if price is None:  # Check if price is None (car not found)
        print(f"Car {car} not found. Receipt cannot be generated.")
        return
  Principal= price-dpamt
  print("--------------Transaction Receipt-----------")
  print(f"Bill ID: {billid}")
  print(f"Billdat: {datebill}")
  print(f"Customer Name: {customer}")
  print(f"Phone: {phone}")
  print(f" Car name: {car}")
  print(f"Downpayment amount paid:{dpamt}")
  print(f"Paymanet Mode: {paymode}")
  print(f"Emiperiod chosen:{emiperiod}")
  print(f"Principal: {Principal}INR")
  print("Interest rate: 12%")
  print(f"EMI:{emi_calculator(price,dpamt,emiperiod)}")
  print("-------------------***-------------------")
  return
def get_car_price(car):
  conn= __connect_database()
  if conn:
    try:
      cursor = conn.cursor()
      sql= "SELECT price FROM CARS WHERE carname=%s"
      val= (car,)
      cursor.execute(sql,val)
      myresult= cursor.fetchone()
      if myresult:
                return myresult[0]
      else:
                return None  # Return None if car not found
    except Error as e:
            print(f"Error: {e}")
            return None
    finally:
            if conn:
                conn.close()
  

def insert_transaction(car,dpamt,phone,paymode, emiperiod):
  conn = __connect_database()
  if conn:
    try:
      cursor = conn.cursor()
      sql= "INSERT INTO transac (car, dpamt, phone, paymode, emiperiod) VALUES(%s, %s,%s,%s,%s)"
      val= (car, dpamt, phone, paymode, emiperiod)
      cursor.execute(sql, val)
      conn.commit()
    except Error as e:
      print(f"Error: {e}")
      return None
def get_billid(customer):
    conn = __connect_database()
    if conn:
        try:
            cursor = conn.cursor()
            sql="SELECT  billid FROM BILLS WHERE customer=%s "
            val=(customer)
            cursor.execute(sql,val)
            myresult= cursor.fetchone()
            cursor.close()
            conn.close()
            return myresult[0] 
        except Error as e:
            print(f"Error: {e}")
        return None
def get_billdate(customer):
    conn = __connect_database()
    if conn:
        try:
            cursor = conn.cursor()
            sql="SELECT  billdate FROM BILLS WHERE customer=%s "
            val=(customer)
            cursor.execute(sql,val)
            myresult= cursor.fetchone()
            cursor.close()
            conn.close()
            return myresult[0] 
        except Error as e:
          print(f"Error: {e}")
        return None


      
  
    
def main():
  customer = input("your name")
  phone = int(input("phone number"))
  bill_date = datetime.date.today()

  insert_customer(customer=customer, phone=phone, bill_date=bill_date)
  conn = __connect_database()
  
      
  car=input("Car name:")
  dpamt= int(input("Downpayment amount paid:"))
  paymode= input(" Mode of Payment:")
  emiperiod= int(input("EMI period chosen:"))
  
  price= get_car_price(car)
 
  insert_transaction(car,dpamt, phone,paymode,emiperiod)
  generate_receipt(get_billid(customer), get_billdate(customer), customer , car, dpamt, paymode, emiperiod,phone,price)

main()
