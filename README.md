# contactbook-api-python-flask-peewee

Super simple contactbook, function runs repeatedly, simple reply, y/n/start to initate editting the database with peewee.



to use:

requirements:
python3
peewee
psql

install:
pip3 install pipenv
pipenv install peewee flask psycopg2-binary


In psql:

\i settings.sql 

to create database

In terminal:
python3 contactbook.py

Runs repeatedly until user enters CNTRL + C

-Tony
