
import pymysql
from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="root"
app.config["MYSQL_DB"]="electronic_store"

db = MySQL(app)

@app.route("/admin_page", methods=["GET","POST"])

def admin():
    cur = db.connection.cursor()
    cur.execute("create table if not exists product_details(product_code int PRIMARY KEY, product_type varchar(20), product_brand varchar(20), product_price int)")
    if request.method == "POST":
        detail = request.form
        code = detail['code']
        name = detail['name']
        brand = detail['brand']
        price = detail['price']
        cur.execute("insert into product_details values(%s,%s,%s,%s)",(code,name,brand,price))
        db.connection.commit()
        
    return render_template("index.html")


@app.route("/delete/<int:code>")

def delete(code):
    cur = db.connection.cursor()
    cur.execute("delete from product_details where product_code=%s",(code,))
    db.connection.commit()

    return render_template("delete.html")


@app.route("/update", methods=["GET","POST"])

def update():
    cur = db.connection.cursor()
    if request.method == "POST":
        detail = request.form
        price = detail['price']
        code = detail['code']
        cur.execute("update product_details set product_price = %s where product_code = %s",(price,code))
        db.connection.commit()

    return render_template("update.html")

if __name__ == "__main__":
    app.run(debug = True)
