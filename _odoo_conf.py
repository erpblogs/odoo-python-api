# -*- coding: utf-8 -*-
import os.path
import inspect

def get_odoo_config_path():
    directory_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    return os.path.join(directory_path, 'odoo_config_local.txt')

def get_odoo_config():
    open_file = open(get_odoo_config_path(), 'r')
    config = open_file.read().splitlines()
    res = dict()
    for line in config:
        data = line.split('=')
        res[data[0]] = data[1]
    open_file.close()

    return res