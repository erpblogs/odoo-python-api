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

# create employee skill:
employee_id = models.execute_kw(db, uid, password, 'hr.employee', 'search',
                                [[('work_email', '=', 'quang.trinhvan@vti.com.vn')]], {'limit': 1})

skill_id = [2]  # get skill id from emp_skill
level = [1]  # level 0-3

create_skill_info = {
    'employee_id': employee_id[0],
    'skill_id': skill_id[0],
    'level': '1', #[('0', 'Junior')],
    'type': 'skill'
}

# create
models.execute_kw(db, uid, password, 'hr.employee.skill', 'create', [create_skill_info])

# create emp programming:
employee_id = models.execute_kw(db, uid, password, 'hr.employee', 'search',
                                [[('work_email', '=', 'quang.trinhvan@vti.com.vn')]], {'limit': 1})

programming_id = [2]  # get skill id from emp_programming
level = [1]  # level 0-3

create_programming_info = {
    'employee_id': employee_id[0],
    'skill_id': programming_id[0],
    'level': '1', #[('0', 'Junior')],
    'type': 'programming'
}

# create
models.execute_kw(db, uid, password, 'hr.employee.skill', 'create', [create_programming_info])

# create emp certificate:
employee_id = models.execute_kw(db, uid, password, 'hr.employee', 'search',
                                [[('work_email', '=', 'quang.trinhvan@vti.com.vn')]], {'limit': 1})


certificate_id = [2]  # get skill id from emp_certificate
file_save = ""
firle_name = 'chung chi aws'
create_certificate_info = {
    'employee_id': employee_id[0],
    'certificate_id': certificate_id[0],
    'file_name': firle_name,
    'file_save': file_save
}

# update
models.execute_kw(db, uid, password, 'hr.employee.certificate', 'create', [create_certificate_info])
