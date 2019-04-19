# # -*- coding: utf-8 -*-
# import xmlrpc.client
#
# from _odoo_conf import get_odoo_config
#
# # get odoo info from file to secure it
# odoo_info = get_odoo_config()
#
# url = odoo_info.get('server')
# db = odoo_info.get('dbname')
# username = odoo_info.get('username')
# password = odoo_info.get('pwd')
#
# login = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
# uid = login.authenticate(db, username, password, {})
# models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
#
#
# recored_info = models.execute_kw(db, uid, password,
#                                  'hr.employee',
#                                  'search_read',
#                                  [[('work_email', '=', 'quang.trinhvan@vti.com.vn')]],
#                                  {
#                                      'fields': [
#                                          'id',  # - Employee_id
#                                          'name',  # - Full_name
#                                          'department_id',  # - Unit [id, name]
#                                          # n/a - Employee_code
#                                          'gender',  # - Sex (0 is female, 1 is male)
#                                          'birthday',  # - Birthday
#                                          'work_email',  # - Email
#                                          'work_phone',  # - Phone_number
#                                          # n/a - Post_code
#                                          'address_home_id',  # - Address
#                                          # n/a - Team
#                                          'contract_id',  # - Contract_type
#                                          'work_location',  # - Working_site
#                                          # - Skills
#                                          # - Certificates
#                                          'image', # - Avatar_path (base64)
#                                      ],
#                                      'limit': 1
#                                  })
#
# print(recored_info)
