# -*- coding: utf-8 -*-
############################################################################################
#
#    ADQUAT
#
############################################################################################


{
    'name': 'Adquat Advanced',
    'version': '0.2',
    'category': 'Tools',
    'description': """
    Ajouts vues personnalisées EXAPROBE et divers
""",
    'author': 'Adquat-solutions',
    'website': 'http://www.adquat.com',
    'depends': ['base','crm'],
    'data': [],
    'demo': [],
    'update_xml': [
        #'security/ir.model.access.csv',
        'views/crm_view.xml',
        'views/partner_view.xml',
        'views/user_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'adquat_advanced/static/src/scss/disable_discussion.scss'
        ],
    },
    'test':[],
    'installable': True,
    'images': [],
}