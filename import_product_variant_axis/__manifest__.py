# -*- coding: utf-8 -*-
{
    'name': 'Import Product Variant from CSV/Excel file for Advance Bulk Import Products Variant in odoo website',
    'category': 'Import Record',
    'version': '15.0.0.0.0',    
    'summary': "Import product variant from CSV Import product variant from Excel import bulk product variants data in odoo Data Import product variant import Data All in one import odoo v14 import product variant import in odoo v14 all import data in odoo using EXCEL or CSV",
    'description': "Import product variant from CSV or Excel file, import bulk product variants data in odoo this module is available in v15, v14, v13, v12 and v11",
    'depends': ['base', 'sale_management','purchase','stock',],
    'data': [
        'security/ir.model.access.csv',
        'security/product_variant_security.xml',
        'wizard/import_product_wizard_view.xml',
        'views/customer_menu.xml',
    ],
    'demo': [
    ],
    'price': 20,
    'currency': 'USD',
    'support': 'business@axistechnolabs.com',
    'author': 'Axis Technolabs',
    'website': 'https://www.axistechnolabs.com',
    'installable': True,
    'license': 'OPL-1',
    'images': ['static/description/images/Banner-Img.png'],
}
