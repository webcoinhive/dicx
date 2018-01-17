# -*- coding: cp1252 -*-
# GENERADOR DE DICCIONARIOS DE CONTRASEÑAS CREADO POR @KvotheTankian (forum.xen0x.org)
# Dicx v1.0
# Falta leet mode, para la siguiente versión
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
p12 = raw_input("> Another word: ")
p13 = raw_input("> Another word: ")
p14 = raw_input("> Another word: ")
p15 = raw_input("> Another word: ")
p16 = raw_input("> Another word: ")
p17 = raw_input("> Another word: ")
print('\n\n\n\n')

allwords = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17]
words = []

for word in allwords:
    if len(word) > 0:
        words.append(word)

lmin = int(input('> Menor número de keywords en una contraseña: '))
lmax = int(input('> Mayor número de keywords en una contraseña: '))
lmax += 1

time = str(datetime.datetime.now().strftime("%y.%m.%d-%H.%M.%S"))
txtname = p1+'_'+time+'.txt'

print('\n\n')
print('[+] Creando diccionario y agregando contraseñas...')
n = 0
with open(txtname,'w') as dic:
    for i in range(lmin,lmax):
        for a in permutations(words,i):
            password = ''.join(a) + '\n'
            passwordcap = password.capitalize()
            dic.write(password)
            n += 1
            if password != passwordcap:
                dic.write(passwordcap)
                n += 1
print('[+] Diccionario creado exitosamente!')
print('[+] El diccionario contiene %s contraseñas')%n
print('\n\n\n')
print('(El diccionario se ha creado en la misma carpeta que la script)')




