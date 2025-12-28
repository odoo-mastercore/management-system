# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Quality Manual",
    "summary": "Quality manual as document pages.",
    "description": """
Provides a predefined Quality Manual category using document_page templates.
It is used as a base manual structure for management systems (ISO-style).
    """,
    "version": "19.0.1.0.0",
    "category": "Management System",
    "author": "OpenERP SA, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/management-system",
    "license": "AGPL-3",
    "depends": ["mgmtsystem_manual"],
    "data": ["data/document_page.xml"],
    "installable": True,
    "auto_install": False,
    "images": ["static/description/icon.png"],
}