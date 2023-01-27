<<<<<<< HEAD
### The code is not fully done, but I implement to structure of Vending machine and product

There are 3 important component in this implementation

#### model.py
a table in the database

#### views.py
contain all the logic for the backend (got problem about JSON serializable)

#### urls.py
url of each api

### forms.py
use for verify the input

### To run the server
 ❯ python3 manage.py runserver    
 

### Postman simple tutorial
to do POST:
1. select "POST"
2. In the "URL" field, enter the endpoint URL for your vending_machine_create view, which is likely to be "http://127.0.0.1:8000/machine/create"
3. In the "Body" section, select form-data
4. example of valid input 
KEY: name  VALUE: vending_machine 1 
KEY: location VALUE: canteen

### Problem
error when try to edit both vending machine and product in machines
=======
# VendingMachine
HW1 of the software engineering class
>>>>>>> a1bdb4836bcb628d5574d8bcd70dc075084e3e2d
