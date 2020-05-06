#!/usr/bin/python3

import cgi

print ("Content-Type: text/html \n\n")

print( '''

<!DOCTYPE HTML>
<html>
<head>
<title> Registration </title>
<link rel="stylesheet" type="text/css" href="style.css">
<body>
''')

data=cgi.FieldStorage()

type_user=data['type'].value
password=data['password'].value
email=data['email'].value
first_name=data['firstname'].value
last_name=data['last_name'].value

filea=open('userdata.txt','a')

line=type_user+':'+email+':'+password+':'+first_name+':'+last_name+'\n'

fila.write(line)
filea.close()

print (</body/html>)
