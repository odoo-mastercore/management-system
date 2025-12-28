# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

{
    "name": "Management System - Nonconformity HR",
    "summary": "Link nonconformities with employees.",
    "description": """
Extends Management System Nonconformities to associate employees.
    """,
    "version": "19.0.1.0.0",
    "author": "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": [
        "mgmtsystem_nonconformity",
        "hr",
    ],
    "data": [
        "views/mgmtsystem_nonconformity.xml",
    ],
    "installable": True,
}