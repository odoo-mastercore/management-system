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
    "name": "Management System - Nonconformity",
    "version": "19.0.1.0.0",
    "summary": "Manage nonconformities within management systems.",
    "description": """
Provides management of nonconformities for management systems:
- Nonconformity records
- Root cause analysis
- Corrective and preventive actions
- Wizards and reporting

Commonly used in ISO 9001 / ISO 14001 contexts.
    """,
    "author": "Savoir-faire Linux, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": [
        "mgmtsystem",
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/mgmtsystem_nonconformity_security.xml",
        "views/mgmtsystem_nonconformity.xml",
        "views/mgmtsystem_origin.xml",
        "views/mgmtsystem_cause.xml",
        "views/mgmtsystem_severity.xml",
        "views/mgmtsystem_action.xml",
        "views/mgmtsystem_nonconformity_stage.xml",
        "data/sequence.xml",
        "data/mgmtsystem_nonconformity_severity.xml",
        "data/mgmtsystem_nonconformity_origin.xml",
        "data/mgmtsystem_nonconformity_cause.xml",
        "data/mgmtsystem_nonconformity_stage.xml",
        "data/mail_message_subtype.xml",
        "reports/mgmtsystem_nonconformity_report.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "mgmtsystem_nonconformity/static/src/**/*.js",
            "mgmtsystem_nonconformity/static/src/**/*.xml",
        ],
    },
    "demo": [],
    "installable": True,
}