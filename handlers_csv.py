#!/usr/bin/python

import csv
#Used for files that has empty lines at the begining
def clean_empty(lista):    
    c = list()
    for a in lista:
        if a:
            c.append(a)
    return c

def read_file(file,delimit=";"):

    open_csv_file= open(file,"r")
    csv_file=list(csv.reader(open_csv_file,delimiter=delimit))
    open_csv_file.close()
    return clean_cell_space(clean_empty(csv_file))

#checks all the chars in the list, if a \n is found it deletes it
def clean_cell_space(file):
    c=list(file)
    d=""
    for i in range(len(file)):
        for j in range(len(file[0])):
            a=get_value(file,i,j)
            if "\n" in a:
                
                for char in a:
                    if char!="\n":
                        d +=char
                write_cell(c,d,j,i)
                d=""

    return(c)

#Return number of columns with header

def max_column(file):    
    return len(file[0])

#Return number of rows

def max_row(file):
    return len(file)

#Inserts a new column in a specific position. If the position is not specified it's added at the beginning.

def insert_col(file,name,pos=0):      
    for i in range(len(file)):
        if i==0:
            file[0].insert(pos,name)
        else:
            file[i].insert(pos,"")

def get_col(file, col):
    c=[]
    for row in file:
        c.append(row[col])
    return c


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

#Writes a CSV file from a list with format [["NAME;SURNAME;AGE"],["DLA;CODING;LOS ANGELES"]]



def write_text_file(new_file_name,list):

    text_file = open(new_file_name,"w")
    for i in range(len(list)):
        for j in range(len(list[i])):
            text_file.write(list[i][j]+";")
        text_file.write("\n")
    text_file.close()

def write_cell(list,value,col,row):

    list[row][col]=value







