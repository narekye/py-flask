from flask import Flask

app = Flask(__name__, instance_relative_config=True)

from app import views # Important note, ordering of import statements

app.config.from_object('config')
