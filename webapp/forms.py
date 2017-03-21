#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Copyright 2013 Alexandre Bulté <alexandre[at]bulte[dot]net>
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from flask_wtf import FlaskForm
from flask_mongoengine.wtf import model_form

from .models import DummyContent

DummyContentForm = model_form(DummyContent)

class LoginForm(FlaskForm.Form):
    email = FlaskForm.TextField(validators=[FlaskForm.required(), FlaskForm.validators.Email()])
    password = FlaskForm.PasswordField(validators=[FlaskForm.required()])
