#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

user = input("Insert the username ")
pw = input("Enter the password ")
IP = input("Enter IP address ")
## where to connect to
t = paramiko.Transport( IP, 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
t.connect(username= user, password= pw)

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
sftp.close() # close the connection

