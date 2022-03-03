from flask import *
from database import *
import uuid

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def home():
	return render_template('home.html')
@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(uname,password)
		res=select(q)
		if res:
			if res[0]['usertype']=='admin':
				flash("login successfully")
				return redirect(url_for('admin.adminhome'))
				
			elif res[0]['usertype']=='doctor':
				q1="select * from doctor where loginid='%s'"%(res[0]['loginid'])
				res1=select(q1)
				session['doctor_id']=res1[0]['doctorid']
				flash("login successfully")
				return redirect(url_for('doctor.doctorhome'))
		else:
			flash("invalid username or password")

	return render_template('login.html')
@public.route('/doctorregister',methods=['get','post'])
def doctorregister():
	if 'submit' in request.form:
		firstname=request.form['firstname'] 	
		lastname=request.form['lastname']
		image=request.files['image']
		path="static/"+str(uuid.uuid4())+image.filename
		image.save(path)
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		qualification=request.form['qualification']
		username=request.form['username']
		password=request.form['password']
		q="insert into login values (null,'%s','%s','doctor')"%(username,password)
		id=insert(q)
		q="insert into doctor values (null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(id,firstname,lastname,path,place,phone,email,qualification)
		insert(q)
	return render_template('doctorregister.html')	