#!/usr/bin/python

#cleans the empty lines

def clean_empty(lista):    
    c = list()
    for a in lista:
        if a:
            c.append(a)
    return c
