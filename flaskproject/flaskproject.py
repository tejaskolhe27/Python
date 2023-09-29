from flask import *
import sqlite3

conn=sqlite3.connect('mydb.db',check_same_thread=False)
cursor=conn.cursor()

app=Flask(__name__)
@app.route("/")
def home():
    #return "hello world"
    return render_template("helloworld.html")

@app.route('/products')
def displayProduct():
    
    cursor.execute("select * from product")
    rows=cursor.fetchall()
    return render_template("displayproduct.html",data=rows)

@app.route('/acceptproduct')
def displayform():
    return render_template("productdata.html")

@app.route('/product/addproduct',methods=["POST"])
def addproduct():
    pid=request.form.get("pid")
    pname=request.form.get('pname')
    qty=request.form.get('qty')
    price=request.form.get('price')

    # cursor.execute(f"insert into product values({pid},{pname},{qty},{price})")
    cursor.execute("insert into product values (?,?,?,?)",(pid,pname,qty,price))
    conn.commit()

    return redirect('/products')




if __name__ =="__main__":
    app.run(debug=True)