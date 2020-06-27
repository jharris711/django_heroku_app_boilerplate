# Django-Heroku App Boilerplate

Quick start for those that plan on deploying their Django app on Heroku. Gunicorn is the production server that will be installed. Cloudinary is installed/set-up for easy image/video hosting. Sign up for a Cloudinary account here: https://cloudinary.com/. On using Cloudinary with Django: https://cloudinary.com/documentation/django_integration

Pre-reqs: Virtualenv

To use:

-> Open your terminal and navigate to the ` django_heroku_app_boilerplate ` directory

-> Set up a new Virtualenv environment: ` $ virtualenv env `

-> Activate the virtual environment: ` $ source env/bin/activate `

-> Install dependencies from the requirements.txt file: ` $ pip install -r requirements.txt `

-> Set .env variables. Choose between SQLite3 and PostgreSQL setup.

-> Configure your .gitignore

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

This boilerplate comes with rename and makesuper commands:

*To create a super user with name & pw as 'admin:*

`$ ./manage.py makesuper`

*To change the name of your app:*

`$ ./manage.py rename OLD_APP_NAME NEW_APP_NAME`
