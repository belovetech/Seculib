#!/usr/bin/env python3
from datetime import datetime, timedelta

def return_date():
    """Return date for borrowed book"""
    return datetime.now() + timedelta(days=14)
