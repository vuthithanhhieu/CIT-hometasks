Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> import pandas as pd
>>> import requests
>>> import json
>>> data = 'D:\\data.csv'
>>> context = 'D:\\context.csv'
>>> def average_value(List_assessment_users):
	count = 0 
	S =0
	for i in range(0, len(List_assessment_users)):
		if (int(List_assessment_users[i])!=-1):
			S += int(List_assessment_users[i])
			count+=1
	avg = S/count
	return avg

>>> sim_uv = {}
>>> def cosine_metric(u1, u2):
	u = 0
	v = 0
	uv = 0
	for i in range(0, len(u1)):
		if ((int(u1[i])!=-1) and (int(u2[i])!=-1)):
			u += int(u1[i])**2
			v += int(u2[i])**2
			uv += int(u1[i]) * int(u2[i])
	sim_u_v = uv / (math.sqrt(u) * math.sqrt(v))
	return sim_u_v

>>> Users=pd.read_csv(data,encoding='ascii',index_col='Users')
>>> myuser = 35
>>> User35=Users.iloc[myuser-1]
>>> for x in range(0,len(Users)): 
	if x!= (myuser - 1):
		sim_uv[x]=cosine_metric(Users.iloc[x], User35)

		
>>> k =5
>>> sim_uv=dict(sorted(sim_uv.items(), key=lambda x: x[1], reverse=True)[:k])
>>> result = {}
>>> def Main(x): 
	total_sim_uv=0
	r_u=round(average_value(User35),2)
	result=0
	users_neighbour =sim_uv.keys()
	for key in users_neighbour:
		r_vi=(Users.iloc[key])[x]
		if r_vi!=-1:
			r_v=average_value(Users.iloc[key])  
			result+=sim_uv[key]*(r_vi - r_v)
			total_sim_uv+=abs(sim_uv[key])
	r_ui = (r_u+result/total_sim_uv)
	return r_ui

>>> for x in range(0,len(User35)):
	if User35[x]==-1:
		result[x+1]=Main(x)

		
>>> for i in result:
	print('Movie',i,':',round(result[i],2))

	
Movie 2 : 2.39
Movie 11 : 1.88
Movie 15 : 4.39
Movie 17 : 3.19
Movie 19 : 3.7
Movie 20 : 3.39
Movie 28 : 1.41
>>> Cont=pd.read_csv(context,encoding='ascii',index_col='Users')
>>> film = []
>>> for f in range (0,30): 
    if int(User35[f])==-1:
        film.append(f)

        
>>> for u in range(0,len(Users)):
     for f in range (0,30):
         dat= (Cont.iloc[u])[f]
         if (dat==' Mon'):
             (Users.iloc[u])[f]=-1

             
>>> for x in range(0,len(Users)):
	if x!=myuser:
		sim_uv[x]=cosine_metric(Users.iloc[x], User35)

		
>>> sim_uv=dict(sorted(sim_uv.items(), key=lambda x: x[1], reverse=True)[:k])
>>> for x in range(0,len(User35)):
	if User35[x]==-1:
		result[x+1]=Main(x)

		
>>> result=dict(sorted(result.items(), key=lambda x: x[1], reverse=True)[:1])
>>> for i in result:
	print('Movie',i,':',round(result[i],2))

	
Movie 27 : 3.69
>>> js={'content-type':'application/json'}
>>> url='https://cit-home1.herokuapp.com/api/rs_homework_1'
>>> result = json.dumps({'user': 35,'1':{"movie 2":2.39,"movie 11":1.88,"movie 15":4.39,"movie 17":3.19,"movie 19":3.7,"movie 20":3.39,"movie 28":1.41},'2':{"movie 27":4.41}})
>>> rs = requests.post(url, data = result, headers=js)
>>> print (rs.json())
