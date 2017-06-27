#!/usr/bin/python

#cleans the empty lines

def clean_empty(lista):    
    c = list()
    for a in lista:
        if a:
            c.append(a)
    return c

#Delete the "comma" and makes the file accesible. By default if the char is not specified ";" is what deletes. 

def fix_file(lista,sep=";"):
    c = list()
    for a in lista:
        b = a[0].split(sep)
        c.append(b)
    return c    

#WITH THE FILE FIX AND FIRST LINE IS THE HEADERS....

#Return number of columns with header

def max_column(file):    
    return len(file[0])

#Return number of rows

def max_row(file):
    return len(file)

#Inserts a new column in a specific position. If the position is not specified it's added at the beginning.

def insert_col(file,data,pos=0):    
    file[0].insert(pos,data)

#Returns the value of the coords. Note that starts with 0 instead of 1

def get_value(file,col,row):
    return file[col][row]

#Finds for a value, if its in any place returns the coords

def find_value(file,value):
    d = list()
    
    for c in range(max_column(file)-1):
        for l in range(max_row(file)-1):
            if get_value(file,c,l)==value:
                d.append(c)
                d.append(l)
    if d:
        return d
    else:
        return False
