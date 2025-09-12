# AirBnB_clone - Console


## Project Description
This is the first step towards building the **AirBnB clone**.  
The goal of this project is to create a command-line interpreter that manages AirBnB objects such as Users, Places, and other future classes.  

The console allows users to:
- Create new objects
- Retrieve objects from storage
- Perform operations on objects
- Destroy objects  

This forms the foundation for the larger AirBnB project where we will implement a full web application with database storage, RESTful API, and front-end integration

---

## Command Interpreter Description

### How to Start
Clone this repository and navigate into the project folder:
```bash
git clone https://github.com/<Kellia855>/alu-AirBnB_clone.git
cd alu-AirBnB_clone

---

### How to Use
Start the console:
```bash
./console.py

You will see the prompt (hbnb).
Type commands and press Enter:

scss
Copy code
(hbnb) help
(hbnb) create User
(hbnb) show User <id>
(hbnb) quit

---

### Examples

Start the console:

./console.py


Example session:

(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit  create  show  destroy  all  update

(hbnb) create User
c1d1f1b1-8e8c-4d1a-92e3-123456789abc

(hbnb) show User c1d1f1b1-8e8c-4d1a-92e3-123456789abc
[User] (c1d1f1b1-8e8c-4d1a-92e3-123456789abc) {'id': 'c1d1f1b1-8e8c-4d1a-92e3-123456789abc'}

(hbnb) all User
["[User] (c1d1f1b1-8e8c-4d1a-92e3-123456789abc) {'id': 'c1d1f1b1-8e8c-4d1a-92e3-123456789abc'}"]

(hbnb) quit


---

## Authors
**Kellia Kamikazi** - k.kamikazi@alustudent.com
**Yusuf Nabide** - y.nabide@alustudent.com

