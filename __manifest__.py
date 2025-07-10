# -*- coding: utf-8 -*-
{
    'name': 'SD PowerBI',
    'version': '18.0.1.0.0',
    'description': '',
    'category': 'Services',
    'summary': """ Poser BI Connector """,
    'author': 'Arash Homayounfar',
    'company': 'Giladoo',
    'maintainer': 'Giladoo',
    'website': "https://www.giladoo.com/powerbi",
    'installable': True,
    'auto_install': False,
    'application': True,
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/powerbi_table.xml',

    ],
    'assets':{
        'web.assets_backend':[
          # 'sd_hr/static/src/components/**/*',
        ],
    },

    'license': 'LGPL-3',
}
