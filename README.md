# python-api-example
🔌 This is an example project on how to configure and wrap a python app into Flask to provide api services.

# You need to create a virtual environment after cloning the project:

1. Installing virtualenv
  - Linux/Mac
  ``python3 -m pip install --user virtualenv``

  - Windows
  ``py -m pip install --user virtualenv``

2. Create virtualenv
  - Linux/Mac
  ``python3 -m venv env  source env/bin/activate``
  
  - Windows
  ``py -m venv env  .\env\Scripts\activate``

# Deploy to Heroku

This is configured to run on heroku
1. ``heroku create``
2. ``git push heroku main``

Heroku with help from this blog post: ``https://geekyhumans.com/how-to-deploy-flask-api-on-heroku/``
