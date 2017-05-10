from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('bt_home.html')

@app.route('/login')
def login():
	return render_template('bt_login.html')
	
@app.route('/reLogin')
def reLogin(err):
	return render_template('bt_reLogin.html',err)
	
@app.route('/login_check',methods = ['POST', 'GET'])
def login_check():
	if request.method == 'POST':
		con = sqlite3.connect('bugTracker_sample.db')
		id = request.form['id']
		paswd = request.form['paswd']
         
#         with sql.connect("database") as con:
		cur = con.cursor()
		cur.execute("SELECT * FROM users WHERE id = ? and paswd = ?",(id,paswd) )
		row = cur.fetchone()
		if(row):
			return render_template('bt_mainPage.html',user = str(row[1]))
		else:
			err = "Username or Password is Incorrect"
			return render_template('bt_reLogin.html',err = err)
	
@app.route('/register')
def register():
	return render_template('bt_register.html')
	
@app.route('/reRegister')
def reRegister(iderr,nmerr,perr):
	return render_template('bt_reRegister.html',iderr,nmerr,perr)
	
@app.route('/register_check',methods = ['POST', 'GET'])
def register_check():
	if request.method == 'POST':
		con = sqlite3.connect('bugTracker_sample.db')
		flag = 0
		perr = ''
		nmerr = ''
		iderr = ''
		try:
			id = request.form['id']
			uname = request.form['uName']
			paswd = request.form['paswd']
			cpaswd = request.form['cPaswd']
			
			if(id == ''):
				flag = 1
				iderr = "* Fill in the Unique ID field" 
				
			if(uname == ''):
				flag = 1
				nmerr = "* Fill in the User Name field"
			elif len(uname) >= 10 :
				flag = 1
				nmerr = "* User Name cannot exceed 10 characters"
			elif (uname.isalnum() != True) and (uname[0].isalpha() != True):
				flag = 1
				nmerr = "* User name is case sensitive and should begin with an alphabet, and can contain numbers and alphabets only"
				
			if(paswd == ''):
				flag = 1
				perr = "* Fill in the password field"
			elif(paswd != cpaswd):
				flag = 1
				perr = "* Passwords are not matching"
			elif(len(paswd) <= 4):
				flag = 1
				perr = "* Password should be at least 5 characters long"
			elif(len(paswd) > 12):
				flag = 1
				perr = "* Password can not exceed 12 characters"
			elif(paswd.isalnum() != True):
				flag = 1
				perr = "* Password can contain only alphabets and numbers"
			
         
#         with sql.connect("database") as con:
			if(flag != 1):
				cur = con.cursor()
				cur.execute("INSERT INTO users (id,uname,paswd) VALUES (?,?,?)",(id,uname,paswd) )            
				con.commit()
				msg = "Record successfully added"
			else:
				return render_template("bt_reRegister.html",iderr = iderr, nmerr = nmerr, perr = perr)
				
		except:
			con.rollback()
			flag = 1
			msg = "Error in Registration"
      
		finally:
			if flag == 0:
				return render_template("bt_register_result.html",msg = msg,flag = flag)
			con.close()

if __name__ == '__main__':
	app.run(debug = True)
