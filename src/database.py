"""Database read/write wrappers"""

from urllib import parse
from flask import Flask, request, redirect
import psycopg2

def db_connect(raw_url):
    url = parse.urlparse(raw_url)
    """Returns a database connection object."""
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    return conn


def get_cursor(db_access):
    """To get cursor for interacting with database."""
    if db_access['conn'].closed:
        db_access['conn'] = db_connect(db_access['url'])
        db_access['cur'] = db_access['conn'].cursor()
    return db_access['cur']


def get_creds(cursor, handle):
    cur.execute(
        "SELECT access_token, access_secret FROM users WHERE handle = '%s'" % handle
        )
    return cur.fetchone()


def init_user_db(cur, handle):
    """CUR.execute("CREATE DATABASE %s" % handle)
    url = 
    conn = db_connect(url)"""
    pass
