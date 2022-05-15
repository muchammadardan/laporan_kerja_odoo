{
    'name': 'Laporan Kerja Teknisi',
    'version': '1.0',
    'summary': 'website_laporan_teknisi',
    'category': 'Kimia Farma',
    'author': 'Muchammad Ardan',
    'maintainer': 'Muchammad Ardan',
    'website': 'google.com',
    'license': 'Other proprietary',
    'contributors': [
        'Muchammad Ardan',
    ],
    'depends': [
        'web_responsive',
    ],
    # 'external_dependencies': {
    #     'python': [
    #         '',
    #     ],
    # },
    'data': [
         # Security
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',

        # Views
        'views/alat.xml',
        'views/area.xml',
        'views/laporan.xml',
        'views/mesin.xml',
        'views/sparepart.xml',
        'views/nama_teknisi.xml',
        'views/known_by.xml',
        'views/received_by.xml',
        'views/zmenu.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
