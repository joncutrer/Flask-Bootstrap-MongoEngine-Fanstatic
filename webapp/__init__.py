#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Copyright 2013 Alexandre Bulté <alexandre[at]bulte[dot]net>
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
from flask import Flask
from flask_fanstatic import Fanstatic
from flask_mongoengine import MongoEngine
from flask_login import LoginManager


##- Init and configure -##

def get_config():
    if os.environ.get('FLASK_ENV', '') == 'PROD':
        return 'webapp.settings.ProductionConfig'
    elif os.environ.get('FLASK_ENV', '') == 'DOTCLOUD':
        return 'webapp.settings.DotcloudConfig'
    else:
        return 'webapp.settings.DevelopmentConfig'

app = Flask(__name__)
app.config.from_object(get_config())
db = MongoEngine(app)

##- Login -##

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

##- Resources -##

fanstatic = Fanstatic(app)
fanstatic.resource('js/app.js', name='app_js', bottom=True)

##- Imports -##

import views
import admin
