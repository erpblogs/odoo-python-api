# -*- coding: utf-8 -*-
import xmlrpc.client

from _odoo_conf import get_odoo_config

odoo_info = get_odoo_config()

url = odoo_info.get('server')
db = odoo_info.get('dbname')
username = odoo_info.get('username')
password = odoo_info.get('pwd')

login = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = login.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# search_read all
all_notify = models.execute_kw(db, uid, password, 'vti.notification', 'search_read',
                               [], {
                                   'fields': [
                                       'title',
                                       'push_time',
                                       'content'
                                   ]
                               })

# search_read by notify id
notify_by_id = models.execute_kw(db, uid, password, 'vti.notification', 'search_read',
                                 [[('id', '=', 89)]], {
                                     'fields': [
                                         'title',
                                         'push_time',
                                         'content'
                                     ]
                                 })

# get department id
department_id = models.execute_kw(db, uid, password, 'hr.department', 'search', [[('name', '=', 'VTI.D4')]])

# get departments ids
department_ids = models.execute_kw(db, uid, password, 'hr.department', 'search',
                                   [[('name', 'in', ['VTI.D4', 'VTI.D5'])]])

# search_read notify by departments ids and status sent
notify_by_departments = models.execute_kw(db, uid, password, 'vti.notification', 'search_read',
                                          [[
                                              '|',
                                              ('department_ids', 'in', department_ids),
                                              ('department_ids', '=', False),
                                              ('state', '=', 'sent')
                                          ]], {
                                              'fields': [
                                                  'title',
                                                  'push_time',
                                                  'content'],
                                              'limit': 20, 'order': 'id desc'
                                          })

print(notify_by_id)
