import mysql.connector

def create_database():
    connection = mysql.connector.connect(user='root', password='123456789', host='localhost')
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Store ")
    #cursor.execute("CREATE TABLE IF NOT EXISTS Purchases(ProductCode int(2) Primary Key, ProductName varchar(20), PurchaseDate Date, PurchasePrice int(3), ProductStock int(2))")
    cursor.close()
    connection.close()

def create_table():
    connection = mysql.connector.connect(user='root', password='123456789', host='localhost', database='Store')
    cursor = connection.cursor()
    #Table for supplier
    cursor.execute("CREATE TABLE IF NOT EXISTS Supplier(Supplier_ID int(10) primary key, Name varchar(40), Address varchar(40), Phone varchar(30), Email varchar(40))")
    # table for category
    cursor.execute("CREATE TABLE IF NOT EXISTS Category(Category_ID int(10) primary key, Category_Name varchar(30), Description varchar(40))")
    # table for Products
    cursor.execute("CREATE TABLE IF NOT EXISTS Product(Product_ID varchar(40) primary key not null, Product_Name varchar(40), Product_Description varchar(40), Price float(8,1), Quantity int(10), Supplier_ID int(10), Category_ID int(10), FOREIGN KEY (Supplier_ID) REFERENCES Supplier(Supplier_ID), foreign key (Category_ID) references Category(Category_ID)) ")
    # table for Roles
    cursor.execute("create table if not exists Roles(Role_ID int(10) primary key not null, Role_Name varchar(40), Description varchar(40))")
    # table for Staff
    cursor.execute("create table if not exists Staff(Staff_ID int(10) primary key not null, First_Name varchar(40), Last_Name varchar(40), Address varchar(40), Phone varchar(30), Email varchar(40), Username varchar (30), Password varchar(40), Role_ID int(10), foreign key (Role_ID) references Roles(Role_ID))")
    # table for Customer
    cursor.execute("create table if not exists Customer(Phone varchar(30) primary key not null, First_Name varchar(30), Last_Name varchar(30), Address varchar(40), Email varchar(40))")
     # table for transaction
    cursor.execute("create table if not exists transaction(Bill_number int(10), Payment_Type varchar(20), Phone varchar(30), Staff_ID int(10), Product_ID varchar(40), Quantity int(10), foreign key (Phone) references Customer(Phone),foreign key (Product_ID) references Product(Product_ID),primary key (bill_number, Product_ID))")
    cursor.execute("drop trigger if exists t1")
    connection.commit()
    cursor.execute("CREATE TRIGGER t1 after INSERT ON transaction FOR EACH ROW BEGIN update product set Quantity=product.quantity-new.quantity; END")
    # TODO: edit order to include payment foreign keys
    # table for Sales
    #cursor.execute("create table if not exists Sales(Order_ID int(10) primary key not null, Date DATE, Phone varchar(30),  foreign key (Phone) references Customer(Phone),Bill_number int(10), foreign key (Bill_number) references Payment(Bill_number))")

    #create trigger after update

    #create product delete

    cursor.close()
    connection.close()


