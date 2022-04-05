# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import Flask
from flask_bootstrap import Bootstrap4
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap4(app)
moment = Moment(app)
# DebugToolbarExtension 一般用不到，在此不进行实例化处理
# toolbar = DebugToolbarExtension(app)

from sayhello import views, errors, commands
