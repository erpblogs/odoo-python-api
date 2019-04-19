# -*- coding: utf-8 -*-
import xmlrpc.client

from _odoo_conf import get_odoo_config

# get odoo info from file to secure it
odoo_info = get_odoo_config()

url = odoo_info.get('server')
db = odoo_info.get('dbname')
username = odoo_info.get('username')
password = odoo_info.get('pwd')

login = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = login.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

recored_id = models.execute_kw(db, uid, password, 'hr.employee', 'search', [[]], {'offset': 0, 'limit': 10})
print(recored_id)

"""
Pagination
By default a search will return the ids of all records matching the condition, which may be a huge number. offset and 
limit parameters are available to only retrieve a subset of all matched records.
"""

recored_id = models.execute_kw(db, uid, password, 'hr.employee', 'search',
                               [[['work_email', '=', 'quang.trinhvan@vti.com.vn']]], {'offset': 0, 'limit': 10})

print(recored_id)

recored_info = models.execute_kw(db, uid, password, 'hr.employee', 'read', [recored_id])

print(recored_info)
