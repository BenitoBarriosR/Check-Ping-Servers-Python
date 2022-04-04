#!/usr/bin/python3

import requests
import os
from datetime import datetime

def bot_send_text(bot_message):

    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response

Dia= datetime.now().strftime('%Y-%m-%d')

CrearArchivo = open("/root/scripts/linode.txt","w")
CrearArchivo.write("SUPENDIDOS DEL DATACENTER 1 " + Dia)
CrearArchivo.write("\n")
CrearArchivo.close()

CrearArchivo = open("/root/scripts/ionos.txt","w")
CrearArchivo.write("SUPENDIDOS DE DATACENTER 2 " + Dia)
CrearArchivo.write("\n")
CrearArchivo.close()

with open('/root/scripts/DATACENTER1.txt','r') as file:
  for host in file:
    response = os.system("ping -c 1 " + host)
    if response == 0:
      Resultado2 = "\n"
      Resultado = ("El Servidor se encuentra Encendido \n")
    else:
        ResultadoFinal = (host + "El Servidor se encuentra Apagado \n")
        with open ("/root/scripts/DATACENTER1.txt", "a") as f:
         f.write(Resultado2 + ResultadoFinal)

with open('/root/scripts/DATACENTER1.txt', 'r') as f2:
    data = f2.read()

bot_send_text(data)

with open('/root/scripts/DATACENTER2.txt','r') as file2:
  for host2 in file2:
    response = os.system("ping -c 1 " + host2)
    if response == 0:
      Resultado2 = "\n"
      Resultado = ("El Servidor se encuentra Encendido \n")
    else:
        ResultadoFinal = (host2 + "El Servidor se encuentra Apagado \n")
        with open ("/root/scripts/DATACENTER2.txt", "a") as f:
         f.write(Resultado2 + ResultadoFinal)

with open('/root/scripts/DATACENTER2.txt', 'r') as f3:
    dataDATACENTER2 = f3.read()

bot_send_text(dataDATACENTER2)


os.remove('/root/scripts/DATACENTER1.txt')
os.remove('/root/scripts/DATACENTER2.txt')
