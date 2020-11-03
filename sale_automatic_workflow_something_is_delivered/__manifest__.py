# Copyright 2020 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    'name': "Sale Automatic Workflow Something Is Delivered",
    'summary': """
        This module adds a Boolean on the SO as "Something is delivered" and
        so invoices are created for a partial delivery.""",
    'version': "14.0.1.0.0",
    'category': 'Uncategorized',
    'website': "http://sodexis.com/",
    'author': "Sodexis",
    'license': 'OPL-1',
    'installable': False,
    'application': False,
    'depends': [
        'sale_automatic_workflow',
    ],
    'data': [
        'views/sale_view.xml',
    ],
}
