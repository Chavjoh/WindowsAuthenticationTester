WindowsAuthenticationTester
===========================

Test windows authentication of a user with multiple password given in a dictionary.

### Requirements

* Python 3.3
* Pywin32 build 218

### How to use

Launch the script with :
```
python WindowsAuthenticationTester.py domain username dictionary
```

Arguments : 
* **domain** : Domain in which test authentication. Generally computer name.
* **username** : Username used to test each password in given dictionary file.
* **dictionary** : Dictionary file path that contains all password to test.

### Dictionary

#### Content

Each line of the dictionary correspond to a password and is terminated by a newline character ```\n```.

For example :
```
a
b
c
...
aa
ab
ac
...
```

#### Generator

Have a look to the project [DictionaryGeneratorPHP](https://github.com/Chavjoh/DictionaryGeneratorPHP).

### Feedback

Don't hesitate to fork this project, improve it and make a pull request.

### License

This project is under Apache 2.0 License.
