# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

# Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Management System - Manual",
    "summary": "Link management systems to document page manuals.",
    "description": """
Extends Management System to associate a manual (document.page) to each management system record.
It also provides menus/actions to access manuals and categories through Document Pages.
    """,
    "version": "19.0.1.0.0",
    "author": "Savoir-faire Linux, Odoo Community Association (OCA), Mastercore Sinapsys Global®",
    "website": "https://github.com/OCA/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": ["document_page", "mgmtsystem"],
    "data": [
        "data/mgmtsystem_manual.xml",
        "views/mgmtsystem_manual.xml",
        "views/document_page.xml",
    ],
    "installable": True,
    "application": False,
}