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

# get employee info
employee_info = models.execute_kw(db, uid, password,
                                  'hr.employee',
                                  'search_read',
                                  [[('work_email', '=', 'quang.trinhvan@vti.com.vn')]],
                                  {
                                      'fields': [
                                          'id',  # - Employee_id
                                          'name',  # - Full_name
                                          'department_id',  # - Unit [id, name]
                                          # n/a - Employee_code
                                          'gender',  # - Sex (0 is female, 1 is male)
                                          'birthday',  # - Birthday
                                          'work_email',  # - Email
                                          'work_phone',  # - Phone_number
                                          # n/a - Post_code
                                          'address_home_id',  # - Address
                                          # n/a - Team
                                          'contract_id',  # - Contract_type
                                          'work_location',  # - Working_site
                                          'employee_skill_ids',
                                          'employee_programming_ids',
                                          'employee_certificate_ids',
                                          'image',
                                      ],
                                      'limit': 1
                                  })

if employee_info:
    employee_skill_ids = employee_info[0]['employee_skill_ids'] or []
    employee_programming_ids = employee_info[0]['employee_programming_ids'] or []
    employee_certificate_ids = employee_info[0]['employee_certificate_ids'] or []

# unlink employee skill:
employee_id = models.execute_kw(db, uid, password, 'hr.employee', 'search',
                                [[('work_email', '=', 'quang.trinhvan@vti.com.vn')]], {'limit': 1})
if len(employee_skill_ids) > 0:
    emp_skill_id = employee_skill_ids[0]
    print(employee_skill_ids)

    # unlink
    models.execute_kw(db, uid, password, 'hr.employee.skill', 'unlink', [[emp_skill_id]])
#
# unlink employee programming:
if len(employee_programming_ids) > 0:
    emp_programming_id = employee_programming_ids[0]
    print(employee_programming_ids)

    # unlink
    models.execute_kw(db, uid, password, 'hr.employee.skill', 'unlink', [[emp_programming_id]])

# unlink employee certificate:
if len(employee_certificate_ids) > 0:
    employee_certificate_id = employee_certificate_ids[0]
    print(employee_certificate_ids)

    # unlink
    models.execute_kw(db, uid, password, 'hr.employee.certificate', 'unlink', [[employee_certificate_id]])
