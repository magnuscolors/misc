# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013 Therp BV (<http://therp.nl>).
#            
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'IBAN Lookup (NL)',
    'version': '0.1',
    'category': 'Banking addons',
    'description': '''
Lookup IBAN account numbers through a paid web service
''',
    'author': 'Therp BV',
    'website': 'http://www.therp.nl',
    'depends': ['account_banking_iban_lookup'],
    'license': 'AGPL-3',
    'installable': True,
    'data': [
        'view/iban_lookup.xml',
        'view/res_partner_bank.xml',
        ],
    }
