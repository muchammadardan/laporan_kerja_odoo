{
    'name': 'Kimia Farma - Laporan Teknisi',
    'version': '1.0',
    'summary': 'Laporan Teknisi',
    'category': 'teknisi',
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
        'views/zmenu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
