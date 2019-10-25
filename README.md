# coverage_report
This project is a dummy one just to help the coverage community resolve an issue with coverage pre-release version 5.0a7


## how to use this project

To use this project please follow the steps below

* clone this repo 
	
	**command**: git clone https://github.com/spaceofmiah/coverage_report.git

* activate virtual environment within project base dir ( to separate project package from system wide packages )
	

	to use the below command, please make sure to install **pipenv** first

	**command**: pipenv shell

* install all packages needed by project

	**command**: pipenv install


* make migrations and migrate db 

	**migration_command**: python manage.py makemigrations

	**migrate_command**: python manage.py migrate


* run coverage test
	
	**command**: coverage run manage.py test



## project package table

```
Package    Version
---------- -------
asgiref    3.2.3
coverage   5.0a8
Django     3.0b1
pip        19.2.3
pytz       2019.3
setuptools 41.2.0
sqlparse   0.3.0
wheel      0.33.6
```