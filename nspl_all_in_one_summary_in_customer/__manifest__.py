{
    'name': 'All in one summary in customer',
    'version': '19.0.1',
    'sequence': 3,
    'author': 'Namah Softech Private Limited',
    'contributors': 'Mohit Nare',
    'maintainer': 'Namah Softech Private Limited',
    'website': 'http://namahsoftech.com/',
    'support': 'support@namahsoftech.com',
    'price': 14.90,
    'currency': 'USD',
    'license': 'OPL-1',
    'category': 'Contacts',
    'summary': 'Limit the number of summary records shown in company or partner views.',
    'description': """
Company Summary Limit

This module allows you to restrict or customize the number of summary items displayed in the company or partner form views. Useful when you want to reduce visual clutter and control what related records (like Sale Orders, Purchase Orders, Tasks) are shown in tabs.

Key Features:
- Limit task, sale order, and purchase order display for partners.
- Show only computed or relevant records.
- Read-only display without 'Add a line' option.

Compatible with: Sales, Purchase, Project, Stock, and CRM modules.
""",
    'depends': ['base', 'contacts', 'sale_management', 'purchase', 'stock', 'account', 'calendar', 'project'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
