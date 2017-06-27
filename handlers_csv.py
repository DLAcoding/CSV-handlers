#!/usr/bin/python

#cleans the empty lines

def clean_empty(lista):    
    c = list()
    for a in lista:
        if a:
            c.append(a)
    return c

#Delete the ";" and makes the file accesible

def fix_file(lista):
    c = list()
    for a in lista:
        b = a[0].split(";")
        c.append(b)
    return c


