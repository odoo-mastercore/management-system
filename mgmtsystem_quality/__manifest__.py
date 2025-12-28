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
    "name": "Quality Management System",
    "summary": "Manage your quality management system",
    "description": """
Glue module that assembles the Quality Management System suite by depending on:
- Manuals
- Audits
- Quality Manual pages
- Reviews

It also creates a 'Quality' Management System record and links it to the Quality Manual page.
    """,
    "version": "19.0.1.0.0",
    "author": "Savoir-faire Linux, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": [
        "mgmtsystem_manual",
        "mgmtsystem_audit",
        "document_page_quality_manual",
        "mgmtsystem_review",
    ],
    "data": ["data/mgmtsystem_system.xml"],
    "installable": True,
}