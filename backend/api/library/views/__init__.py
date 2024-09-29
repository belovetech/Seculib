#!/usr/bin/env python3
"""Init file for /api/v1/users"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")


if app_views:
    from api.library.views.student import *
    from api.library.views.book import *
    from api.library.views.ddos import *
