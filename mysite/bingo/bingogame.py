import pymysql #Libreria para conectar con mysql
import json
import random 
import string 
import time
import csv
import numpy as np
import pandas as pd

#arrays for temporal storage
cartones=[]
partidas2=[]
partidas = []  
balotas = []
bingos = []
nickname=[]
termi=[]
defin=[]
ubalota=[]
admin=[]

csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_NONE)
#gamefiles
# partidasFile = '/mnt/c/Unal/TPI/app/mysite/bingo/persist/partidas.csv'
# bingosFile = '/mnt/c/Unal/TPI/app/mysite/bingo/persist/bingos.csv'
# cartonesFile = '/mnt/c/Unal/TPI/app/mysite/bingo/persist/cartones.csv'
# nickFile = '/mnt/c/Unal/TPI/app/mysite/bingo/persist/nick.csv'
# balotasFile = '/mnt/c/Unal/TPI/app/mysite/bingo/persist/balotas.csv'
# ubalotaFile = '/mnt/c/Unal/TPI/app/mysite/bingo/persist/ubalota.csv'
# adminFile = '/mnt/c/Unal/TPI/app/mysite/bingo/persist/admin.csv'
# terminosFile = '/mnt/c/Unal/TPI/app/mysite/bingo/persist/terminos.csv'
# defFile = '/mnt/c/Unal/TPI/app/mysite/bingo/persist/def.csv'
#game files aws path
partidasFile = '/home/ec2-user/app/mysite/bingo/persist/partidas.csv'
bingosFile = '/home/ec2-user/app/mysite/bingo/persist/bingos.csv'
cartonesFile = '/home/ec2-user/app/mysite/bingo/persist/cartones.csv'
nickFile = '/home/ec2-user/app/mysite/bingo/persist/nick.csv'
balotasFile = '/home/ec2-user/app/mysite/bingo/persist/balotas.csv'
ubalotaFile = '/home/ec2-user/app/mysite/bingo/persist/ubalota.csv'
adminFile = '/home/ec2-user/app/mysite/bingo/persist/admin.csv'
terminosFile = '/home/ec2-user/app/mysite/bingo/persist/terminos.csv'
defFile = '/home/ec2-user/app/mysite/bingo/persist/def.csv'

#creates a macth and returns its id
def crearp():
	with open(partidasFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				row=str(row)
				row=row.replace(",", "")
				row=row.replace("'", "") 
				row=row.replace("[", "") 
				row=row.replace("]", "") 
				row=row.replace(" ", "") 
				partidas.append(row)
	with open(balotasFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				balotas.append(row)
	with open(ubalotaFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				row=str(row)
				row=row.replace(",", "")
				row=row.replace("'", "") 
				row=row.replace("[", "") 
				row=row.replace("]", "") 
				row=row.replace(" ", "")
				ubalota.append(row)
	with open(bingosFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				bingos.append(row)
	with open(cartonesFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				cartones.append(row)
	with open(adminFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				row=str(row)
				row=row.replace(",", "")
				row=row.replace("'", "") 
				row=row.replace("[", "") 
				row=row.replace("]", "") 
				row=row.replace(" ", "")
				admin.append(row)
	with open(nickFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				nickname.append(row)

	codigo = ''.join(random.sample(string.ascii_letters[26:], 4)) 
	partidas.append(codigo)
	#print(codigo)
	#print('Codigo de la partida ' +codigo) 
	balotas.append(list(range(1,76)))
	bingos.append(list(range(1,101)))
	nickname.append(list(range(1,101)))
	ubalota.append(str(0))
	admin.append(str(0))
	#print(ubalota)
	myFile = open(partidasFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(partidas)
	myFile = open(adminFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(admin)
	myFile = open(ubalotaFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(ubalota)

	myFile = open(balotasFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(balotas)

	myFile = open(bingosFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(bingos)

	myFile = open(nickFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(nickname)
	response = {'idgame' : codigo}
	return response
#new player joins existing match
def entrar(codigo, nic):
	succes  = 0
	with open(partidasFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
				#partidas.append(row)
			else:
				row=str(row)
				row=row.replace(",", "")
				row=row.replace("'", "") 
				row=row.replace("[", "") 
				row=row.replace("]", "") 
				row=row.replace(" ", "") 
				#print(row)
				partidas.append(row)
	with open(bingosFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				bingos.append(row)
	with open(cartonesFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				cartones.append(row)
	with open(adminFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				row=str(row)
				row=row.replace(",", "")
				row=row.replace("'", "") 
				row=row.replace("[", "") 
				row=row.replace("]", "") 
				row=row.replace(" ", "")
				admin.append(row)
	with open(nickFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				nickname.append(row)

	#print(len(bingos[partidas.index(codigo)]))
	print(admin[partidas.index(codigo)])
	
	if len(bingos[partidas.index(codigo)])>0:
		print('Entrando a la partida '+ partidas[partidas.index(codigo)]) 
		idcarton = random.choice(bingos[partidas.index(codigo)])
		bingos[partidas.index(codigo)].remove(idcarton) 
		idcarton = int(idcarton) 
		nickname[partidas.index(codigo)][idcarton-1]=nic
		carton = cartones[0][idcarton-1]
		if  admin[partidas.index(codigo)]=='0':
			print('Aqui')
			admin[partidas.index(codigo)]=nic
		#print('ID carton: '+str(idcarton)+' carton: '+carton+ ' Nick: '+nic )
		#print(bingos)
		succes = 1
	else:
		#print('partida llena')
		succes = 0

	myFile = open(adminFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(admin)

	myFile = open(nickFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(nickname)
		#print(nickname)

	myFile = open(bingosFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(bingos)
	if succes == 1:
		response = {
			'idboard': idcarton,
			'board': carton,
			'nickname': nic
		}
		return response
	else:
		response = {
			'idboard': 'full',
			'board': 'game',
			'nickname': 'error'
		}
		return response
#pulls random number from pool
def balota(codigo, nic):
	balotaPartida = 0
	with open(partidasFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
				#partidas.append(row)
			else:
				row=str(row)
				row=row.replace(",", "")
				row=row.replace("'", "") 
				row=row.replace("[", "") 
				row=row.replace("]", "") 
				row=row.replace(" ", "") 
				#print(row)
				partidas.append(row) 
	with open(balotasFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
				#partidas.append(row)
			else:
				balotas.append(row)
				#print(balotas)
	with open(adminFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				row=str(row)
				row=row.replace(",", "")
				row=row.replace("'", "") 
				row=row.replace("[", "") 
				row=row.replace("]", "") 
				row=row.replace(" ", "")
				admin.append(row)
	with open(ubalotaFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				row=str(row)
				row=row.replace(",", "")
				row=row.replace("'", "") 
				row=row.replace("[", "") 
				row=row.replace("]", "") 
				row=row.replace(" ", "")
				ubalota.append(row)
	#print(nic)
	#print(admin[partidas.index(codigo)])
	#print(ubalota[partidas.index(codigo)])
	if nic == admin[partidas.index(codigo)]:
		if len(balotas[partidas.index(codigo)])>0:          
			print('Balota para partida '+ partidas[partidas.index(codigo)])
			idbalota = random.choice(balotas[partidas.index(codigo)])
			#print(idbalota)
			#print(idcarton)
			balotas[partidas.index(codigo)].remove(idbalota) #Mirar error en cero 
			#print(balotas[partidas.index(codigo)])
			ubalota[partidas.index(codigo)]=idbalota
			print(ubalota[partidas.index(codigo)])
			
		else:
			print('no quedan balotas')
			balotaPartida = 0
	else:
		print("no admin")
		print(ubalota[partidas.index(codigo)])
		balotaPartida = ubalota[partidas.index(codigo)]
	myFile = open(balotasFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(balotas)
	myFile = open(ubalotaFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(ubalota)
	#print(len(balotas[partidas.index(codigo)]))
	balotaPartida = ubalota[partidas.index(codigo)]
	response = {'balota': balotaPartida}
	return response
#delete a match
def borrar(codigo):
	mensResp = 'temp'
	with open(partidasFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
				#partidas.append(row)
			else:
				row=str(row)
				row=row.replace(",", "")
				row=row.replace("'", "") 
				row=row.replace("[", "") 
				row=row.replace("]", "") 
				row=row.replace(" ", "") 
				#print(row)
				partidas.append(row)
	with open(ubalotaFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				row=str(row)
				row=row.replace(",", "")
				row=row.replace("'", "") 
				row=row.replace("[", "") 
				row=row.replace("]", "") 
				row=row.replace(" ", "")
				ubalota.append(row)
	with open(adminFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				row=str(row)
				row=row.replace(",", "")
				row=row.replace("'", "") 
				row=row.replace("[", "") 
				row=row.replace("]", "") 
				row=row.replace(" ", "")
				admin.append(row)
	with open(balotasFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
				#partidas.append(row)
			else:
				balotas.append(row)
				#print(balotas)
	with open(bingosFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
				#partidas.append(row)
			else:
				bingos.append(row)
				#print(bingos)
	with open(cartonesFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
				#partidas.append(row)
			else:
				cartones.append(row)
				#print(cartones)
	with open(nickFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
				#partidas.append(row)
			else:
				nickname.append(row)
				#print(nickname)
	#print(row)
	if codigo in partidas:

		print('Borrando partida '+ partidas[partidas.index(codigo)]) 
 
		del balotas[partidas.index(codigo)]
		del bingos[partidas.index(codigo)]
		del nickname[partidas.index(codigo)]  
		del admin[partidas.index(codigo)]
		del ubalota[partidas.index(codigo)]
		del partidas[partidas.index(codigo)]
		mensResp = 'partida borrada'
	else:
		print('No existe esta partida: '+ codigo)
		mensResp = 'No existe esta partida'
	
	myFile = open(partidasFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(partidas)
	myFile = open(adminFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(admin)
	myFile = open(ubalotaFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(ubalota)

	myFile = open(balotasFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(balotas)
	myFile = open(bingosFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(bingos)

	myFile = open(nickFile, 'w')
	with myFile:
		writer = csv.writer(myFile, dialect='myDialect')
		writer.writerows(nickname)
	response = {'message': mensResp}
	return response

def ganador(codigo, numero):
	mensResp = 'temp'
	with open(partidasFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
				#partidas.append(row)
			else:
				row=str(row)
				row=row.replace(",", "")
				row=row.replace("'", "") 
				row=row.replace("[", "") 
				row=row.replace("]", "") 
				row=row.replace(" ", "") 
				#print(row)
				partidas.append(row)
	with open(nickFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
		#partidas.append(row)
			else:
				nickname.append(row)

	if codigo in partidas:
	
		#print('Ganador partida '+ partidas[partidas.index(codigo)] +' '+numero) 
		#usuario=nickname[partidas.index(codigo)][int(numero)-1]
		#print(usuario)
		mensResp = 'Ganador partida'
	else:
		print('No existe esta partida: '+ entrada[8:12])
		mensResp = 'No existe esta partida'
	response = {'message': mensResp}
	return response
#returns bingo ambiental terms as dict
def terminos():
	with open(terminosFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			if len(row) == 0:
				z=1
			else:
				termi.append(row)
	res_dct = {i : termi[i] for i in range(0, len(termi))}
	return res_dct
#returns bingo ambiental definitions as dict
def defi():
	with open(defFile) as File:  
		reader = csv.reader(File)
		for row in reader:
			
			if len(row) == 0:
				z=1
			else:
				row=str(row)
				row=row.replace("Â\\xa0"," ")
				row=row.replace("-",",")
				#print(row)
				defin.append(row)
	res_dct = {i : defin[i] for i in range(0, len(defin))}
	return res_dct