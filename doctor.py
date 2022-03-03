from flask import *
from database import *
import uuid

doctor=Blueprint('doctor',__name__)

@doctor.route('/doctorhome',methods=['get','post'])
def doctorhome():
	return render_template('doctorhome.html')

@doctor.route('/doctormanagemyspecialist',methods=['get','post'])
def doctormanagemyspecialist():
	data={}
	q="select * from disease"
	r=select(q)
	data['dis']=r

	if 'add' in request.form:
		did=session['doctor_id']
		disease=request.form['disease_id']
		print("$$$$$$$$$444444")
		print(disease)
		q="insert into specialists values (null,'%s','%s')"%(did,disease)
		print(q)
		insert(q)
		return redirect(url_for('doctor.doctormanagemyspecialist'))

	if 'action' in request.args:
		action=request.args['action']
		lid=request.args['lid']

	else:
		action=None
	if action=="delete":
		q="delete from specialists where diseaseid='%s'"%(lid)
		delete(q)
		return redirect(url_for('doctor.doctormanagemyspecialist'))
	if action=="update":	
		q="select * from specialists where diseaseid='%s'"%(lid)
		res=select(q)
		data['updatedisease']=res
	if 'update' in request.form:
		disease=request.form['disease_id']

		q="update specialists set disease='%s',where diseaseid='%s'"%(disease,lid)
		update(q)
		return redirect(url_for('doctor.doctormanagemyspecialist'))
		
	
	return render_template('doctormanagemyspecialist.html',data=data)


@doctor.route('/doctor_view_hospitals')
def doctor_view_hospitals():
	data={}
	doctor_id=session['doctor_id']
	q="select * from hospital"
	res=select(q)
	data['doc']=res
	if 'action' in request.args:
		action=request.args['action']
		hospitalid=request.args['hospitalid']

	else:
		action=None
	if action=="assign":
		q="insert into doctorhospital values(null,'%s','%s')"%(doctor_id,hospitalid)
		insert(q)
		flash("add to my hospital")
		return redirect(url_for('doctor.doctor_view_hospitals'))
	return render_template("doctor_view_hospitals.html",data=data)


@doctor.route('/doctor_view_update_profile',methods=['get','post'])
def  doctor_view_update_profile():
	data={}
	doc_id=session['doctor_id']
	q="select * from doctor where doctorid='%s'"%(doc_id)
	res=select(q)
	data['doctor']=res

	if 'update' in request.form:
		firstname=request.form['firstname']
		lastname=request.form['lastname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		qualification=request.form['qualification']
		q="update doctor set firstname='%s',lastname='%s',place='%s',phone='%s',email='%s',qualification='%s' where doctorid='%s'"%(firstname,lastname,place,phone,email,qualification,doc_id)
		update(q)
		return redirect(url_for('doctor.doctor_view_update_profile'))
	return render_template("doctor_view_update_profile.html",data=data)