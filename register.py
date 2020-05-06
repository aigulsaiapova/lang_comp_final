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
type=data['type'].value
usernme=data['username'].value
password=data['password'].value
email=data['email'].value
fullname=data['firstname'].value

filea=open('userdata.txt','a')

line=type+':'+user+':'+email+':'+password+':'+first_name+':'+last_name+'\n'

fila.write(line)
filea.close()

print (</body/html>)
