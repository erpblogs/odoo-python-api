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

emp_skill_info = models.execute_kw(db, uid, password,
                                   'hr.employee.skill',
                                   'search_read',
                                   [[('id', 'in', employee_skill_ids)]],
                                   {
                                       'fields': [
                                           'skill_id',
                                           'level',
                                       ]
                                   })

print("\nSkill info", emp_skill_info)

emp_programming_info = models.execute_kw(db, uid, password,
                                         'hr.employee.skill',
                                         'search_read',
                                         [[('id', 'in', employee_skill_ids)]],
                                         {
                                             'fields': [
                                                 'skill_id',
                                                 'level',
                                             ]
                                         })
print("\nProgramming info", emp_programming_info)

emp_certificate_info = models.execute_kw(db, uid, password,
                                         'hr.employee.certificate',
                                         'search_read',
                                         [[('id', 'in', employee_certificate_ids)]],
                                         {
                                             'fields': [
                                                 'certificate_id',
                                                 'level',
                                             ]
                                         })
print("\nCertificate info", emp_certificate_info)

# get all skill
emp_skill = models.execute_kw(db, uid, password,
                              'hr.skill',
                              'search_read',
                              [[('type', '=', 'skill')]],
                              {
                                  'fields': [
                                      'id',
                                      'name',
                                  ]
                              })

print('\nemp skill', emp_skill)

# get programming skill
emp_programming = models.execute_kw(db, uid, password,
                                    'hr.skill',
                                    'search_read',
                                    [[('type', '=', 'programming')]],
                                    {
                                        'fields': [
                                            'id',
                                            'name',
                                        ]
                                    })

print('\nprogramming skill', emp_programming)

# get all certificate
emp_certificate = models.execute_kw(db, uid, password,
                                    'hr.certificate',
                                    'search_read', [],
                                    {
                                        'fields': [
                                            'id',
                                            'name',
                                        ]
                                    })

print('\nemp certificate', emp_certificate)
