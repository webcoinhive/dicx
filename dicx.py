# -*- coding: cp1252 -*-
# GENERADOR DE DICCIONARIOS DE CONTRASEÑAS CREADO POR @KvotheTankian (forum.xen0x.org)
# Dicx v1.1 (añadidos leet mode y pequeños detalles)

import datetime
from itertools import permutations

print('@KvotheTankian')
print('forum.xen0x.org')
print('\n\n\n                SI NO QUIERES INTRODUCIR UNA PALABRA, SIMPLEMENTE DALE A ENTER \n')
print('                           (Introduce las keywords en minúsculas)\n')

p1 = raw_input("> Nombre: ")
p2 = raw_input("> Apellido: ")
p3 = raw_input("> Segundo apellido: ")
p4 = raw_input("> Apodo, otro nombre: ")
p5 = raw_input("> Día: ")
p6 = raw_input("> Mes: ")
p7 = raw_input("> Año: ")
p8 = raw_input("> 2 últimas cifras del año: ")
p9 = raw_input("> Inicial 1: ")
p10 = raw_input("> Inicial 2: ")
p11 = raw_input("> Inicial 3: ")
p12 = raw_input("> Otra keyword: ")
p13 = raw_input("> Otra keyword: ")
p14 = raw_input("> Otra keyword: ")
p15 = raw_input("> Otra keyword: ")
p16 = raw_input("> Otra keyword: ")
p17 = raw_input("> Otra keyword: ")
print('\n\n\n\n')

allwords = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17]
words = []
for word in allwords:
    if len(word) > 0:
        words.append(word)

kmin = int(input('> Menor número de keywords en una contraseña: '))
kmax = int(input('> Mayor número de keywords en una contraseña: '))
kmax += 1
lenmax = int(input('> Máxima longitud de una contraseña (caracteres): '))
             
time = str(datetime.datetime.now().strftime("%y.%m.%d-%H.%M.%S"))
txtname = p1.capitalize()+'-'+time+'.txt'
dic = open(txtname,'w')

#leetmode
def leet(pw):
    pw = pw.replace('e','3')
    pw = pw.replace('E','3')
    pw = pw.replace('i','1')
    pw = pw.replace('I','1')
    pw = pw.replace('o','0')
    pw = pw.replace('O','0')
    pw = pw.replace('a','4')
    pw = pw.replace('A','4')
    pw = pw.replace('s','5')
    pw = pw.replace('S','5')
    pw = pw.replace('t','7')
    pw = pw.replace('T','7')
    dic.write(pw)


#crear diccionario sin leet mode
def noleet():
    for i in range(kmin,kmax):
        for a in permutations(words,i):
            password = ''.join(a) + '\n'
            passwordcap = password.capitalize()
            if len(password) <= lenmax:
                dic.write(password)
                if password != passwordcap:
                    dic.write(passwordcap)

#crear diccionario con leet mode
def leetmode():
    for i in range(kmin,kmax):
        for a in permutations(words,i):
            password = ''.join(a) + '\n'
            passwordcap = password.capitalize()
            if len(password) <= lenmax:
                dic.write(password)
                leet(password)
                if password != passwordcap:
                    dic.write(passwordcap)
                    leet(passwordcap)
                            

mode = raw_input('''> Activar leet mode? [S/N] (se crearian contraseñas cambiando letras
  por números, por ejemplo: hola = h0l4): ''')

print('\n\n')
print('[+] Creando diccionario y agregando contraseñas...')

if mode == 'no' or mode == 'n' or mode == 'N' or mode == 'NO' or mode == 'No' or mode == '':
    noleet()
elif mode == 'si' or mode == 's' or mode == 'SI' or mode == 'S' or mode == 'Si':
    leetmode()
dic.close()

print('[+] Diccionario creado exitosamente!')
print('(El diccionario se ha creado en la misma carpeta que la script)\n\n')

#contar contraseñas creadas
def contar():
    with open(txtname,'r') as pwlist:
        n = 0
        for i in pwlist:
            n += 1
        print('[+] El diccionario creado contiene %s contraseñas')%n

contarpw = raw_input('> Desea contar las contraseñas que se han generado? [escribe s si quieres, y dale a enter si no]: ')
if contarpw == 's' or contarpw == 'S':
    contar()

print('\n\n')
print('Feliz cracking! :)')






