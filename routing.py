from flask import Flask
from flask import render_template
from flask import request
from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/get')
def get_info():
    return 'Yoooo'

@app.route('/add')
def get_info():
    return 'add'

app.run()