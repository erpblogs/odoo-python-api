# -*- coding: utf-8 -*-
import xmlrpc.client

from _odoo_conf import get_odoo_config

# get odoo info from file to secure it
odoo_info = get_odoo_config()


common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(odoo_info.get('server')))

uid = common.authenticate(odoo_info.get('dbname'), odoo_info.get('username'), odoo_info.get('pwd'), {})

if(not uid):
    print('Login failed!')
else:
    print('Login success uid={}'.format(uid))