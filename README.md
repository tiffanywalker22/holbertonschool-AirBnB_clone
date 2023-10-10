# AirBnb clone - The Console
![hbnb](https://github.com/tiffanywalker22/holbertonschool-AirBnB_clone/assets/121834519/5da96a1f-c059-45bd-b12e-f748fdaf5df6)
## Description


The AirBnB console implements a command-line interpreter for managing objects of various classes in a Python. This project comprises several classes, including a <b>BaseModel</b> class that provides fundamental functionalities such as object initialization, saving to JSON files, and conversion to dictionaries. Other classes, such as <b>Amenity</b>, <b>City</b>, <b>Place</b>, <b>Review</b>, <b>State</b>, and <b>User</b>, inherit from <b>BaseModel</b> and represent specific entities with their attributes. The <b>FileStorage</b> class manages the storage of objects in JSON files, facilitating object serialization and deserialization. The <b>Console</b> provides commands like creating, displaying, updating, and deleting objects of different classes. 

<hr>

## Flowchart

<hr>

## Files

<hr>

## Files Description

<hr>

## Installation

**Clone this repository:**
```
root@user$ git clone https://github.com/tiffanywalker22/holbertonschool-AirBnB_clone.git
```
**In terminal navigate to root directory and run this command:**
```
holbertonschool-AirBnB_clone$ ./console.py
```
**Interpreter will begin and prompt user:**
```
(hbnb)
```
<hr>

## Using Command Interpreter
---
| Commands  | Sample Usage                                  | Functionality                              |
| --------- | --------------------------------------------- | ------------------------------------------ |
| `help`    | `help`                                        | displays all commands available            |
| `create`  | `create <class>`                              | creates new object (ex. a new User, Place) |
| `update`  | `User.update('123', {'name' : 'tiffany_ez'})` | updates attribute of an object             |
| `destroy` | `User.destroy('123')`                         | destroys specified object                  |
| `show`    | `User.show('123')`                            | retrieve an object from a file, a database |
| `all`     | `User.all()`                                  | display all objects in class               |
| `quit`    | `quit`                                        | exits                                      |
<hr>

## Interactive and Non-Interactive
Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Testing
To test the files, classes, and functions in this project use the following commands:
```
python3 -m unittest discover tests
```
You can also test file by file by using this command: 
```
python3 -m unittest tests/test_models/test_base_model.py
```
<hr>

## Authors
<a href="https://github.com/tiffanywalker22">Tiffany Walker</a> <br>
<a href="https://github.com/Zal-atan">Ethan Zalta</a> <br>





![image](https://github.com/tiffanywalker22/test/assets/121834519/77aefda3-ca99-4e00-bca9-b2f390d9873f)
