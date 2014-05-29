#!/usr/bin/env python

from flask import render_template
from . import auth  # this actually imports the blueprint

@auth.route('/login')
def login():
    return render_template('auth/login.html')