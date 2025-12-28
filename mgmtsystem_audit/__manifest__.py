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
    "name": "Management System - Audit",
    "version": "19.0.1.0.0",
    "summary": "Audit management for ISO-style management systems.",
    "description": """
Audit management for management systems (ISO-like):
- Audits and verification lines
- Automated actions (base_automation)
- Reports and pivot views
- Wizards to copy verification lines
    """,
    "author": "Savoir-faire Linux, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": ["mgmtsystem_nonconformity", "base_automation"],
    "data": [
        "security/ir.model.access.csv",
        "security/mgmtsystem_audit_security.xml",
        "data/audit_sequence.xml",
        "data/audit_automated_actions.xml",
        "views/mgmtsystem_audit.xml",
        "views/res_users.xml",
        "reports/audit.xml",
        "reports/verification.xml",
        "reports/report.xml",
        "reports/mgmtsystem_audit_pivot.xml",
        "wizard/copy_verification_lines.xml",
    ],
    "demo": [],
    "installable": True,
    "application": False,
}