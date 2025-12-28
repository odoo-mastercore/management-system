# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

{
    "name": "Management System - Survey",
    "summary": "Expose Surveys under Management System configuration.",
    "description": """
Adds a menu entry under Management System configuration to access Survey records.
This module does not add business logic; it only provides navigation for managers.
    """,
    "version": "19.0.1.0.0",
    "author": "Savoir-faire Linux, Odoo Community Association (OCA), Mastercore Sinapsys Global®",
    "website": "https://github.com/OCA/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": ["mgmtsystem", "survey"],
    "data": ["views/survey_survey.xml"],
    "installable": True,
    "development_status": "Beta",
    "maintainers": ["max3903"],
}