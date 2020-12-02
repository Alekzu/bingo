from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . import bingogame as bg
import pymysql #Libreria para conectar con mysql
import json
import random 
import string 
import time
import csv
import numpy as np
import pandas as pd
#arrays for temporal storage

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
	return HttpResponse("Hello world. You're at the wrong place")

def newgame(request):
	response = bg.crearp()
	return JsonResponse(response)
	#return HttpResponse(response)
@csrf_exempt #POST without logein creds
def enter(request):
	succes = 0
	if request.method=='POST':
		#received_json_data = json.loads(request.body.decode("utf-8"))
		received_json_data = json.loads(request.body)
		nic = received_json_data['nickname']
		idgame = received_json_data['idgame']
		response = bg.entrar(idgame,nic)
		return JsonResponse(response)
	else:
		return HttpResponse("wrong request")
@csrf_exempt #POST without logein creds	
def balot(request):
	if request.method=='POST':
		received_json_data = json.loads(request.body.decode("utf-8"))
		idGame = received_json_data['idgame']
		nickname = received_json_data['nickname']
		mess = bg.balota(idGame,nickname)
		return JsonResponse(mess)
	else:
		return HttpResponse("wrong request")
@csrf_exempt #POST without logein creds
def deletegame(request):
	if request.method=='POST':
		received_json_data = json.loads(request.body.decode("utf-8"))
		idgame = received_json_data['idgame']
		response = bg.borrar(idgame)
		return JsonResponse(response)
	else:
		return HttpResponse("wrong request")
@csrf_exempt #POST without logein creds
def winner(request):
	if request.method=='POST':
		received_json_data = json.loads(request.body.decode("utf-8"))
		idgame = received_json_data['idgame']
		idboard = received_json_data['idboard']
		mess = bg.ganador(idgame,idboard)
		return JsonResponse(mess)
	else:
		return HttpResponse("wrong request")

def definitions(request):
	if request.method=='GET':
		#received_json_data = json.loads(request.body.decode("utf-8"))
		#defNum = received_json_data['id']
		#with open('/mnt/c/Unal/TPI/V3/def.csv') as File:
		response = bg.defi()
		return JsonResponse(response)
	else:
		return HttpResponse("Nope")
def terms(request):
	if request.method=='GET':
		#received_json_data = json.loads(request.body.decode("utf-8"))
		#defNum = received_json_data['id']
		#with open('/mnt/c/Unal/TPI/V3/def.csv') as File:
		response = bg.terminos()
		return JsonResponse(response)
	else:
		return HttpResponse("Wrong request")
def boards(request):
	cartones=[]
	db_Bingo = pymysql.connect("open-db.c7zw6t80m5e9.us-east-1.rds.amazonaws.com","opadmin","opendb123","bingo") # Conector (direccion, usuario, contraseña, nombre_BD)
	cu = db_Bingo.cursor() # Declaracion del cursor
	#cu.execute("INSERT INTO prueba VALUES ('Jz', 30);") # Se extraen los valores del id y los numeros del carton
	cu.execute("SELECT * FROM cartones") # Se extraen los valores del id y los numeros del carton
	db_Bingo.commit() 
	cartones = cu.fetchall()
	data = {}                                           #se crea el diccionario para guardar datos necesarios a pasar
	data['cartones'] = []                               #se crea un elemento de diccionario vacio donde se guardaron los cartones
	list_num_char=[]
	list_num_int=[]
	#data_cartones=[]
	#se recorre carton por carton para agregarlos al elemento del diccionario 'cartones' 
	for carton in cartones:
		list_num_char=carton[1].split(";")
		list_num_int = [ 0 if char== "C" else int(char) for char in list_num_char]
		data['cartones'].append({
		'num_carton': carton[0],                        #se asigna el numero de carton 
		'numeros': list_num_int})                          #se asigna los numeros de carton
	#with open('data.json', 'w') as file:
	#   json.dump(data, file, indent=4)
	return JsonResponse(data)

	##
#@csrf_exempt