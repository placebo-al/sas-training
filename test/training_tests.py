from nose.tools import *
from app import app 

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)


def intermediate():
    rv = web.get('/intermediate', follow_redirects=True)
    assert_equal(rv.status_code, 200)


def advanced():
    rv = web.get('/advanced', follow_redirects=True)
    assert_equal(rv.status_code, 200)


