from peewee import *

db = PostgresqlDatabase('contactbook', user='tonywu', password='',
                        host='localhost', port=5432)

def Connect():
  db.connect()
  print("Connecting to psql")
  return 0

Connect()

class BaseModel(Model):
  class Meta:
    database = db

class contactForm(BaseModel):
    name = CharField()
    phoneNumber = CharField()
    note = CharField()

db.create_tables([contactForm])

def inputContactForm(InputtedName, InputtedPhoneNumber, InputtedNote):
  newContact = contactForm(name = InputtedName, phoneNumber = InputtedPhoneNumber, note = InputtedNote)
  newContact.save()
  print("Saving contact to book, returning...")
  return 0

status = "running"
while  status == "running":
  toEnter = input("Would you like to enter a details to a contact book? (y/n) : ")
  if toEnter == "n":
    status = "notRunning"
    changeStatus = input("To start application, type in (start): ")
    if changeStatus == "start":
      status = "running"
  elif toEnter == "y":
    name = input("Enter full name: ")
    phoneNumber = input("Enter person phone number: ")
    note = input("Enter note about contact person: ")
    inputContactForm(name,phoneNumber,note)
