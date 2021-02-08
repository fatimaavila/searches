from flask import Flask, request, redirect, url_for, render_template
from jinja2 import Template, Environment, FileSystemLoader
import random


environment="development"

#file_loader = FileSystemLoader('templates')
#env = Environment(loader=file_loader)

app = Flask(__name__, static_url_path='/static')

def generarlista(p_len):
    randomlist = []
    for i in range(0, p_len): #largo de la lista
        n = random.randint(0,99) #valores que habrán en lista
        randomlist.append(n)
    return randomlist


def linear_search(p_list, p_value):
    for i in range(len(p_list)): 
        if p_list[i] == p_value: 
            return i 
    return -1

def binary_search(p_list, p_value):
    begin_index = 0
    end_index = len(p_list) - 1
    contador = 0

    while begin_index <= end_index:
        #contador = contador+1
        #print(contador)
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = p_list[midpoint]
        if midpoint_value == p_value:
            return midpoint

        elif p_value < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return -1

@app.route('/')
def index():
	return 'root /'

@app.route('/linear')
def linear():
    n=int(request.args.get("n"))
    value=int(request.args.get("value"))
    lista = generarlista(n)
    print(lista)
    resultado = linear_search(lista,value)
    return 'Linear search N=' + str(n)  + ' La lista es: ' +str(lista)+' y buscando el valor ' + str(value)  + ' Resultado = ' + str(resultado) 

@app.route('/binary')
def binary():
    n=int(request.args.get("n"))
    value=int(request.args.get("value"))
    lista = generarlista(n)
    print(lista)
    lista.sort()
    resultado = binary_search(lista, value)
    #print(resultado)
    return 'Binary search N=' + str(n)  + ' La lista es: ' +str(lista)+' y buscando el valor ' + str(value)  + ' Resultado = ' + str(resultado) 


if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    print("Local change")
    app.run(host="0.0.0.0", debug=True)
