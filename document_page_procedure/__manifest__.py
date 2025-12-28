# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

{
    "name": "Document Management - Wiki - Procedures",
    "summary": "Procedures section for Management System wiki.",
    "description": """
Adds a Procedures category and menu entry under the Management System manuals,
using document_page (wiki) pages as procedure documents.
    """,
    "version": "19.0.1.0.0",
    "author": "Savoir-faire Linux, Odoo Community Association (OCA), Mastercore Sinapsys Global®",
    "website": "https://github.com/OCA/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": ["document_page", "mgmtsystem"],
    "data": [
        "data/document_page_procedure.xml",
        "views/document_page_procedure.xml",
    ],
    "installable": True,
}