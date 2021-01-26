#!/bin/bash

#postgres -D 'C:\Program Files\PostgreSQL\12\data' &
createdb -U postgres todo
#dropdb -U postgres todo

#psql -U  postgres todo # to connect

#copy from windows as normal, fn+delete/insert to paste in bash.exe
#https://dba.stackexchange.com/questions/83164/remove-password-requirement-for-user-postgres#83233