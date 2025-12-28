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
    "name": "Management System",
    "version": "19.0.1.0.0",
    "summary": "Support for management systems, such as ISO compliance.",
    "description": """
Provides the base structures and configuration helpers to support management systems
(e.g., ISO compliance frameworks) in Odoo. It defines the Management System model and
a settings entry point used by the management-system suite.
    """,
    "author": "Savoir-faire Linux, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": ["base"],
    "data": [
        "security/mgmtsystem_security.xml",
        "security/ir.model.access.csv",
        "views/menus.xml",
        "views/mgmtsystem_system.xml",
        "views/res_config.xml",
    ],
    "application": True,
}