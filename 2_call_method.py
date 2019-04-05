# -*- coding: utf-8 -*-
import xmlrpc.client

from _odoo_conf import get_odoo_config

# get odoo info from file to secure it
odoo_info = get_odoo_config()


login = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(odoo_info.get('server')))
uid = login.authenticate(odoo_info.get('dbname'), odoo_info.get('username'), odoo_info.get('pwd'), {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(odoo_info.get('server')))

# Call 'res.partner'.check_access_rights method

is_read_access = models.execute_kw(odoo_info.get('dbname'), uid, odoo_info.get('pwd'),
                                   'res.partner', 'check_access_rights',
                                   ['read'], {'raise_exception': False})

if is_read_access:
    print('User {} have access rights on {}'.format(uid, 'res.partner'))
