Implemented in Python 3.5, HTML, Javascript, CSS
Tested on Chrome


Python libraries used:
flask
flask-mail
sqlalchemy
flask-sqlalchemy
flask-bootstrap
flask-migrate
sqlalchemy_continuum

all can be installed with 'pip install ...'



default libraries used:
os
random
urllib



run instructions:

in csssecretsanta   run 'python run.py'


Features:
emailing participants
private pools
ability to login and add a wishlist

Design Comments:
used sqlite database for convenience and I believe an SQL database will be better for larger scale usage
used flask backend for convenience and functionality


Project structure:
in csssecretsanta/
   run.py launches webapp
   create_db.py creates the sqlite database if it doesn't exist
   ssapp/ holds the rest of the files
   

in ssapp/
   config.db is the sqlite database
   __init__.py creates the app and gets settings
   settings.py  has the settings for database
   models.py   creates ORM mapping for sqlite tables
   views.py creates backend for urls
   templates/ contains html templates
   static/ contains css file  



Online resources used:
css styling for forms from https://pythonspot.com/en/login-authentication-with-flask/
backgrounds:
http://www.publicdomainpictures.net/pictures/140000/velka/christmas-santa.jpg
https://hdwallsource.com/img/2014/2/green-holiday-backgrounds-18367-18832-hd-wallpapers.jpg
http://eskipaper.com/images/holiday-backgrounds-9.jpg


estimate spent 6 hours


