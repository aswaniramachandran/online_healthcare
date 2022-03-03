from flask import *
from database import *
import demjson

api=Blueprint('api',__name__)

@api.route('/login')
def login():
	data={}
	username=request.args['username']
	password=request.args['password']
	q="select * from login where username='%s' and password='%s'"%(username,password)
	res=select(q)
	print(res)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)



@api.route('/user_registration')
def user_registration():
	data={}
	firstname=request.args['first_name']
	lastname=request.args['last_name']
	place=request.args['place']
	phone=request.args['phone_no']
	email=request.args['email']
	username=request.args['username']
	password=request.args['password']
	
	q="select * from login where username='%s' and password='%s'"%(username,password)
	res=select(q)
	if res:
		data['status']="duplicate"
	else:
		q="insert into login values(null,'%s','%s','user')"%(username,password)
		id=insert(q)
		q="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,firstname,lastname,place,phone,email)
		insert(q)
		print(q)
		data['status']="success"
	return demjson.encode(data)

@api.route('/userviewdoctors')
def userviewdoctors():
	data={}
	q="select * from doctor"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="userviewdoctors"
	return demjson.encode(data)


@api.route('/viewdoctorsssss')
def viewdoctorsssss():
	data={}
	symptom=request.args['search']
	print(symptom)
	symptoms=symptom.split(",")
	print(len(symptoms))
	llm=len(symptoms)
	ll=len(symptoms)-1
	# if len(symptoms)>
	s=""
	for row in symptoms:
		if s=="":
			s="('"+row+"'"
		else:
			s=s+",'"+row+"'"
		if symptoms.index(row)==ll:
			s=s+")"
	# print(s)
	# ss=('sssss','vvvv')

	for row in symptoms:

		q="""select * from doctor inner join specialists using(doctorid) where diseaseid in(SELECT diseaseid
		FROM `symptoms`
		WHERE `symptoms` IN %s
		GROUP BY `diseaseid`
		HAVING COUNT(*) = '%s') """ %(s,llm-symptoms.index(row))
		print(q)
		res=select(q)
		print(res)

		if res:
			data['status']="success"
			data['data']=res
			break
		else:
			data['status']="failed"
	data['method']="viewdoctorsssss"
	return demjson.encode(data)

@api.route('/userviewdoctorsspecialistin')
def userviewdoctorsspecialistin():
	data={}
	did=request.args['did']
	q="select * from disease where diseaseid in (select diseaseid from specialists where doctorid='%s')" %(did)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="userviewdoctorsspecialistin"
	return demjson.encode(data)

@api.route('/viewhospitals')
def viewhospitals():
	data={}
	did=request.args['did']
	q="select * from hospital where hospitalid in (select hospitalid from doctorhospital where doctorid='%s')" %(did)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewhospitals"
	return demjson.encode(data)

@api.route('/Viewdisease')
def Viewdisease():
	data={}
	q="select * from disease"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="Viewdisease"
	return demjson.encode(data)

@api.route('/Viewsymptoms')
def Viewsymptoms():
	data={}
	did=request.args['did']
	q="select * from symptoms where diseaseid='%s'" %(did)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="Viewsymptoms"
	return demjson.encode(data)

@api.route('/Viewdiseases')
def Viewdiseases():
	data={}
	symptom=request.args['search']
	print(symptom)
	symptoms=symptom.split(",")
	print(len(symptoms))
	llm=len(symptoms)
	ll=len(symptoms)-1
	# if len(symptoms)>
	s=""
	for row in symptoms:
		if s=="":
			s="('"+row+"'"
		else:
			s=s+",'"+row+"'"
		if symptoms.index(row)==ll:
			s=s+")"
	# print(s)
	# ss=('sssss','vvvv')

	for row in symptoms:

		q="""select * from doctor inner join specialists using(doctor_id) where disease_id in(SELECT diseaseid
		FROM `symptoms`
		WHERE `symptoms` IN %s
		GROUP BY `diseaseid`
		HAVING COUNT(*) = '%s')) """ %(s,llm-symptoms.index(row))
		print(q)
		res=select(q)
		print(res)

		if res:
			data['status']="success"
			data['data']=res
			break
		else:
			data['status']="failed"
	data['method']="Viewdisease"
	return demjson.encode(data)


@api.route('/Viewsymptomsss')
def Viewsymptomsss():
	data={}
	q="select * from symptoms group by symptoms"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="Viewsymptomsss"
	return demjson.encode(data)

@api.route('/Viewsymptomssss')
def Viewsymptomssss():
	data={}
	serached="%"+request.args['serached']+"%"
	q="select *  from symptoms where symptoms like '%s' group by symptoms" %(serached)
	print(q)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="Viewsymptomsss"
	return demjson.encode(data)

# SELECT `symptomsid`
# FROM `symptoms`
# WHERE `symptoms` IN ('sssss', 'vvvv')
# GROUP BY `diseaseid`
# HAVING COUNT(*) = 2 

@api.route('/userviewdoctorss')
def userviewdoctorss():
	data={}
	did=request.args['did']
	q="select * from hospital inner join doctorhospital using(hospitalid)  where doctorid ='%s'" %(did)
	print(q)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="userviewdoctorss"
	return demjson.encode(data)


@api.route('/userrating')
def userrating():
	data={}
	rating=request.args['rating']
	review=request.args['review']
	logid=request.args['logid']

	q="SELECT * FROM `rating` WHERE `userid`=(SELECT `userid` FROM `user` WHERE `loginid`='%s')"%(logid)
	res=select(q)
	if res:
		q="UPDATE `rating` SET `rating`='%s',`review`='%s',`date`=CURDATE() WHERE `userid`=(SELECT `userid` FROM `user` WHERE `loginid`='%s')"%(rating,review,logid)
		update(q)
		data['status']="success"
	else:
		q="INSERT INTO `rating` VALUES(NULL,(SELECT `userid` FROM `user` WHERE `loginid`='%s'),'%s','%s',CURDATE())"%(logid,rating,review)
		insert(q)
		data['status']="success"
	data['method']="userrating"
	return demjson.encode(data)




@api.route('/viewrating')
def viewrating():
	data={}
	logid=request.args['logid']
	q="SELECT * FROM `rating` WHERE `userid`=(SELECT `userid` FROM `user` WHERE `loginid`='%s')"%(logid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res[0]['rating']
		data['data1']=res[0]['review']

	else:
		data['status']="failed"
	data['method']="viewrating"
	return demjson.encode(data)