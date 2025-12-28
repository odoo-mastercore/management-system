# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

{
    "name": "Management System - Review",
    "summary": "Manage management system reviews and outcomes.",
    "description": """\
Supports management reviews for ISO-style management systems.

Key features:
- Review records with participants and meeting date
- Review lines linking actions and nonconformities
- Integration with surveys (answers) when mgmtsystem_survey is installed
- Reports and security groups
""",
    "version": "19.0.1.0.0",
    "author": "Savoir-faire Linux, Odoo Community Association (OCA), Mastercore Sinapsys Global®",
    "website": "https://github.com/OCA/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": ["mgmtsystem_nonconformity", "mgmtsystem_survey"],
    "data": [
        "security/ir.model.access.csv",
        "security/mgmtsystem_review_security.xml",
        "data/ir_sequence.xml",
        "views/mgmtsystem_review.xml",
        "views/res_users.xml",
        "reports/review.xml",
        "reports/report.xml",
    ],
    "installable": True,
}