
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_mysql_username'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_database_name'

mysql = MySQL(app)

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from form
    data = request.form['input_name']
    
    # Insert data into database
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO your_table (column_name) VALUES (%s)', (data,))
    mysql.connection.commit()
    cursor.close()
    
    # Return a response
    return 'Data submitted successfully!'

""" #cursor = mysql.connection.cursor()
#cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
#mysql.connection.commit()
#cursor.close()

????

from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)
 
@app.route('/login')
def login():
    return render_template('login.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        FirstName = request.form['fname']
        LastName = request.form['lname']
        Gender = request.form['gender']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s,%s)''',(FirstName,LastName,Gender))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
 
app.run(host='localhost', port=5000)
"""