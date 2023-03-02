import mysql
import mysql.connector
import database

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

connection = mysql.connector.connect(user='root', password='123456789', host='localhost')
cursor = connection.cursor()
database.create_database()
database.create_table()
cursor.execute("use store;")


@app.route('/')
def select():

    return render_template('select.html')

@app.route('/home')
def home():

    return render_template('home.html')

'''@app.route('/update_product',methods = ['POST','GET'] )
def update_product():
    if request.method == 'POST':
        search = request.form.get('search')
        Qty = request.form.get('Qty')
        cursor.execute("update product set Quantity=\""+Qty+"\" WHERE Product_ID=\""+search+"\";")
        data=cursor.fetchall()
        connection.commit()
        return render_template('delete_product.html', product=data,x=y)
    cursor.execute("select * from product;")
    pdata = cursor.fetchall()
    return render_template('delete_product.html',pdat = pdata )'''

@app.route('/update_product',methods = ['POST','GET'] )
def update_product():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        cursor.execute("update product set Quantity=\""+quantity+"\" WHERE Product_ID=\""+product_id+"\";")
        cursor.execute("select * from product")
        data=cursor.fetchall()
        connection.commit()
        return render_template('update_product.html', product=data)
    cursor.execute("select * from product;")
    pdata = cursor.fetchall()
    connection.commit()
    return render_template('update_product.html',product = pdata )


@app.route('/admin', methods = ['POST','GET'])
def admin():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if password =="admin":
            return redirect(url_for('admin_menu'))
        #return f"your username is: {username} \n and password is: {password}"

    return render_template('admin.html')


@app.route('/admin_menu')

def admin_menu():

    return render_template('admin_menu.html')


@app.route('/roles', methods = ['POST','GET'])

def roles():
    if request.method == 'POST':
        role_id = request.form.get('role_id')
        role_name = request.form.get('role_name')
        r_desc = request.form.get('r_desc')
        cursor.execute(''' INSERT INTO roles VALUES(%s,%s,%s)''',
                       (role_id, role_name, r_desc))
        connection.commit()
        return redirect(url_for('admin_menu'))
    return render_template('roles.html')


@app.route('/staff_info', methods = ['POST','GET'])
def staff_info():
    if request.method == 'POST':
        staff_id = request.form.get('staff_id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        address = request.form.get('address')
        phone = request.form.get('phone')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        role_id = request.form.get('role_id')

        cursor.execute(''' INSERT INTO staff VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                       (staff_id, first_name, last_name, address, phone, email, username, password, role_id))
        connection.commit()
        return redirect(url_for('select'))
    return render_template('staff_info.html')

@app.route('/staff', methods = ['POST','GET'])
def staff():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        cursor.execute("select * from staff WHERE username=\""+username+"\" and password=\""+password+"\";")
        for a in cursor:
            if a[6] == username and a[7] == password:
                return redirect(url_for('menu'))

       # if password=="world":
        #    return redirect(url_for('menu'))
        #return f"your username is: {username} \n and password is: {password}"

    return render_template('staff.html')


@app.route('/menu')
def menu():

    return render_template('menu.html')

@app.route('/view_menu')
def view_menu():

   return render_template('view_menu.html')


@app.route('/view_staff')
def view_staff():

    cursor.execute("select * from staff;")
    data=cursor.fetchall()

    return render_template('view_staff.html', staff=data)

@app.route('/view_customer',methods = ['POST','GET'] )
def view_customer():
   if request.method == 'POST':
        phone = request.form.get('phone')
        cursor.execute("select * from customer WHERE Phone=\""+phone+"\" ;")
        data=cursor.fetchall()
        return render_template('view_customer.html', customer=data)

   return render_template('view_customer.html')

@app.route('/view_product',methods = ['POST','GET'] )
def view_product():
   if request.method == 'POST':
        search = request.form.get('search')
        cursor.execute("select * from customer WHERE Product_ID=\""+search+"\" or WHERE Category_ID=\""+search+"\";")
        data=cursor.fetchall()
        return render_template('view_product.html', customer=data)

   return render_template('view_product.html')

@app.route('/view_payment',methods = ['POST','GET'] )
def view_payment():
   if request.method == 'POST':
        search = request.form.get('search')
        cursor.execute("select * from customer WHERE Phone=\""+search+"\";")
        data=cursor.fetchall()
        return render_template('view_payment.html', payment=data)

   return render_template('view_payment.html')   

@app.route('/view_order',methods = ['POST','GET'])
def view_order():
    if request.method == 'POST':
        bill_no = request.form.get('Bill')
        print(bill_no)
        cursor.execute("select Product_ID,Quantity,Payment_Type,Phone from transaction WHERE Bill_number=\""+bill_no+"\" ;")
        data=cursor.fetchall()
        return render_template('view_transaction.html', pdata=data)
    
    return render_template('view_transaction.html')

@app.route('/inventory_menu')
def inventory_menu():

    return render_template('inventory_menu.html')

@app.route('/menu2')
def menu2():

    return render_template('menu2.html')

@app.route('/sales_menu')
def sales_menu():

    return render_template('sales_menu.html')




@app.route('/supplier', methods = ['POST','GET'])
def supplier():
    if request.method == 'POST':
        supplier_name = request.form.get('supplier_name')
        supplier_id = request.form.get('supplier_id')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        #return address
        try:
            cursor.execute(''' INSERT INTO supplier VALUES(%s,%s,%s,%s,%s)''', (supplier_id, supplier_name, address, phone, email))
            connection.commit()
        except:
            return("no connection")


        return redirect(url_for('inventory_menu'))
    return render_template('supplier.html')

@app.route('/category', methods = ['POST','GET'])

def category():
    if request.method == 'POST':
        category_id = request.form.get('category_id')
        category_name = request.form.get('category_name')
        c_desc = request.form.get('c_desc')
        cursor.execute(''' INSERT INTO category VALUES(%s,%s,%s)''',
                       (category_id, category_name, c_desc))
        connection.commit()
        return redirect(url_for('inventory_menu'))
    return render_template('category.html')

@app.route('/product', methods = ['POST','GET'])

def product():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        product_name = request.form.get('product_name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        supplier_id = request.form.get('supplier_id')
        category_id = request.form.get('category_id')
        p_desc = request.form.get('p_desc')
        cursor.execute(''' INSERT INTO product VALUES(%s,%s,%s,%s,%s,%s,%s)''',
                       (product_id, product_name, p_desc, price, quantity, supplier_id, category_id))
        connection.commit()

        return redirect(url_for('menu'))
    cursor.execute("select product_id,product_name from product")
    data = cursor.fetchall()
    cursor.execute("select supplier_ID,Name from supplier;")
    supplier = cursor.fetchall()
    cursor.execute("select * from category;")
    ca = cursor.fetchall()
    return render_template('product.html',pdata = data,sdata=supplier,cdata = ca )







@app.route('/customer', methods = ['POST','GET'])
def customer():
    if request.method == 'POST':
        customer_id = request.form.get('customer_id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        address = request.form.get('address')
        #try:
        cursor.execute(''' INSERT INTO customer VALUES(%s,%s,%s,%s,%s)''',
                   (phone, first_name, last_name, address, email))
        #except:
         #   return("No Connection")
        connection.commit()
        return redirect(url_for('menu'))
    return render_template('customer.html')

global l
l = []
@app.route('/payment', methods = ['POST','GET'])
def payment():
    if request.method == 'POST':
        bill_number = request.form.get('bill_number')
        global bill
        bill = bill_number
        Payment_Type = request.form.get('Payment_Type')
        phone = request.form.get('phone')
        Staff_ID = request.form.get('Staff_ID')
        Product_ID = request.form.get('Product_ID')
        Quantity = request.form.get('Quantity')
        global l
        l.append((bill_number,Payment_Type,phone,Staff_ID,Product_ID,Quantity))
        return redirect(url_for('payment1'))
    return render_template('payment.html')

@app.route('/payment1', methods = ['POST','GET'])
def payment1():
    if request.method == 'POST':
        global l

        Product_ID = request.form.get('Product_ID')
        Quantity = request.form.get('Quantity')
        print(l[0])
        l.append((l[0][0],l[0][1],l[0][2],l[0][3],Product_ID,Quantity))
        return redirect(url_for('payment1'))
    return render_template('payment1.html')


'''@app.route('/retrieve', methods = ['POST','GET'])
def retrieve():
    if request.method == 'POST':
        phone = request.form.get('phone')
        cursor.execute("select * from customer WHERE Phone=\""+phone+"\" ;")
        for x in cursor:
             h1 = x[0]
             h2 = x[1]
             h3 = x[2]
             h4 = x[3]
             h5 = x[5]
             h6 = x[6]

    return render_template('customer.html')'''

@app.route('/total')
def total():
    global l
    cursor.execute("start transaction")
    print(l,"===")
    for i in range(0,len(l)):
        print(l[i])
        cursor.execute(''' INSERT INTO transaction(Bill_number, Payment_Type, Phone, Staff_ID,Product_ID, Quantity) VALUES(%s,%s,%s,%s,%s,%s)''',
                        (l[i][0],l[i][1],l[i][2],l[i][3],l[i][4],l[i][5]))
    connection.commit()
    l.clear()
    bill = 0
    return render_template('total.html')

if __name__ == '__main__':
     app.run(debug=True)
