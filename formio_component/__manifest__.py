# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

{
    'name': 'Forms | Component',
    'summary': 'Saves Form Components as database records.',
    'version': '0.2',
    'license': 'LGPL-3',
    'author': 'Nova Code',
    'website': 'https://www.novacode.nl',
    'license': 'LGPL-3',
    'category': 'Extra Tools',
    'depends': ['formio', 'formio_data_api'],
    'data': [
        'security/ir.model.access.csv',
        'views/formio_builder_views.xml',
        'views/formio_component_views.xml',
        'views/formio_menu.xml',
    ],
    'application': False,
    'images': [
        'static/description/banner.gif',
    ],
    'description': """
Forms | Component
================
Saves Form Components as database records.
"""
}
