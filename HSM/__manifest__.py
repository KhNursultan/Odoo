# -*- coding: utf-8 -*-
{
    'name': "HMS",

    'description': """
        Hospital Management System
    """,

    'author': "Nursultan Khamzabek",
    'website': "http://www.nurscompany.com",
    #
    # # Categories can be used to filter modules in modules listing
    # # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views\hms_patient.xml',
        'views\hms_department.xml',
        'views\hms_doctor.xml',
        'views\log_history.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}