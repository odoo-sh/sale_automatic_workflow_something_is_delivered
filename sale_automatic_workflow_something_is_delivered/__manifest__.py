# -*- coding: utf-8 -*-
# Copyright 2020 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    'name': "Sale Automatic Workflow Something Is Delivered",
    'summary': """
        This module adds a Boolean on the SO as "Something is delivered" and 
        so invoices are created for a partial delivery.""",
    'version': '13.0.1.0.0',
    'category': 'Uncategorized',
    'website': "http://sodexis.com/",
    'author': "Sodexis",
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'depends': ['base',
                'sale',
                'sod_sale_payment_method',
                'sale_automatic_workflow',
    ],
    'data': [
        'views/sale_view.xml',
    ],
}