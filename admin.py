from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')

@admin.route('/adminviewhospital',methods=['get','post'])
def adminviewhospital():
	data={}
	q="select * from hospital"
	res=select(q)
	data['hos']=res

	return render_template('adminviewhospital.html',data=data)


@admin.route('/adminmanagedoctors',methods=['get','post'])
def adminmanagedoctors():
    data={}
    q="select * from doctor"	
    res=select(q)
    data['doc']=res
    if 'action' in request.args:
    	action=request.args['action']
    	lid=request.args['lid']
    else:
    	action=None
    if action=="delete":
    	q="delete from login where loginid='%s'"%(lid)
    	delete(q)
    	q="delete from doctor where loginid='%s'"%(lid)
    	delete(q)
    	return redirect(url_for('admin.adminmanagedoctors'))
    if action=="update":
    	q="select * from doctor where loginid='%s'"%(lid)
    	res=select(q)
    	data['doctor']=res
    if 'update' in request.form:
    	firstname=request.form['firstname']
    	lastname=request.form['lastname']
    	place=request.form['place']
    	phone=request.form['phone']
    	email=request.form['email']
    	qualification=request.form['qualification']
    	q="update doctor set firstname='%s',lastname='%s',place='%s',phone='%s',email='%s',qualification='%s' where loginid='%s'"%(firstname,lastname,place,phone,email,qualification,lid)
    	update(q)
    	return redirect(url_for('admin.adminmanagedoctors'))

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
    	return redirect(url_for('admin.adminmanagedoctors'))


    return render_template('adminmanagedoctors.html',data=data)



@admin.route('/admin_manage_disease',methods=['get','post'])
def admin_manage_disease():
	data={}
	q="select * from disease"
	res=select(q)
	data['des']=res
	if 'action' in request.args:
		action=request.args['action']
		did=request.args['did']
	else:
		action=None
	if action=="delete":
		q="delete from disease where diseaseid='%s'"%(did)
		delete(q)
		return redirect(url_for('admin.admin_manage_disease'))	
	if action=="update":	
		q="select * from disease where diseaseid='%s'"%(did)
		res=select(q)
		data['deses']=res
		if 'update' in request.form:
			disease=request.form['disease']
			disease_details=request.form['disease_details']
			q="update disease set disease='%s',details='%s' where diseaseid='%s'"%(disease,disease_details,did)
			update(q)
			return redirect(url_for('admin.admin_manage_disease'))
	if 'submit' in request.form:
		disease=request.form['disease']
		disease_details=request.form['disease_details']
		q="insert into disease values(null,'%s','%s')"%(disease,disease_details)
		insert(q)
		return redirect(url_for('admin.admin_manage_disease'))
	
	return render_template('admin_manage_disease.html',data=data)
	


@admin.route('/managehospital',methods=['get','post'])
def managehospital():
	data={}
	q="select * from hospital"
	res=select(q)
	data['doc']=res
	if 'action' in request.args:
		action=request.args['action']
		hid=request.args['hid']
	else:
		action=None
	if action=="delete":
		q="delete from hospital where hospitalid='%s'"%(hid)
		delete(q)
		return redirect(url_for('admin.managehospital'))
	if action=="update":	
		q="select * from hospital where hospitalid='%s'"%(hid)
		res=select(q)
		data['updatehospital']=res
	if 'update' in request.form:
		hname=request.form['Hname']
		place=request.form['Place']
		phone=request.form['Phone']
		email=request.form['Email']
		link=request.form['Link']
		q="update hospital set hname='%s',place='%s',phone='%s',email='%s',link='%s' where hospitalid='%s'"%(hname,place,phone,email,link,hid)
		update(q)
		return redirect(url_for('admin.managehospital'))
	if 'submit' in request.form:
		hname=request.form['Hname']
		place=request.form['Place']
		phone=request.form['Phone']
		email=request.form['Email']
		link=request.form['Link']
		username=request.form['username']
		password=request.form['password']
		q="insert into login values (null,'%s','%s','hospital')"%(username,password)
		id=insert(q)
		q="insert into hospital values (null,'%s','%s','%s','%s','%s','%s')"%(id,hname,place,phone,email,link)
		insert(q)
		return redirect(url_for('admin.managehospital'))
	return render_template('managehospital.html',data=data)


@admin.route('/adminmanagesymptoms',methods=['get','post'])
def adminmanagesymptoms():
	
	data={}
	did=request.args['did']
	data['did']=did
	q="select * from symptoms where diseaseid='%s'"%(did)
	res=select(q)
	data['symptoms']=res

	if 'submit' in request.form:
		symptoms=request.form['symptoms']
		q="insert into symptoms values(null,'%s','%s')"%(did,symptoms)
		insert(q)
		return redirect(url_for('admin.adminmanagesymptoms',did=did))
	return render_template("adminmanagesymptoms.html",data=data)



@admin.route('/adminviewworkinghospitals',methods=['get','post'])
def adminviewworkinghospitals():
	data={}
	did=request.args['did']
	q="SELECT * FROM `doctorhospital` INNER JOIN `hospital`USING(`hospitalid`)INNER JOIN `doctor` USING(`doctorid`) where doctorid='%s'"%(did)
	res=select(q)
	data['hos']=res

	return render_template('adminviewworkinghospitals.html',data=data)

