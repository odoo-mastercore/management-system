# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

# Copyright (C) 2004-2012 OpenERP S.A. (<http://openerp.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, exceptions, fields, models


class MgmtsystemConfigSettings(models.TransientModel):
    """This class is used to activate management system Applications."""

    _inherit = "res.config.settings"

    # Systems
    module_mgmtsystem_quality = fields.Boolean(
        "Quality Tools",
        help="Provide quality management tools.\n"
        "- This installs the module mgmtsystem_quality.",
    )
    module_mgmtsystem_audit = fields.Boolean(
        "Audits",
        help="Provide audit management tools.\n" "- This installs the module mgmtsystem_audit.",
    )
    module_mgmtsystem_action = fields.Boolean(
        "Actions",
        help="Provide action management tools.\n"
        "- This installs the module mgmtsystem_action.",
    )
    module_mgmtsystem_review = fields.Boolean(
        "Reviews",
        help="Provide review management tools.\n"
        "- This installs the module mgmtsystem_review.",
    )
    module_mgmtsystem_nonconformity = fields.Boolean(
        "Nonconformities",
        help="Provide nonconformity management tools.\n"
        "- This installs the module mgmtsystem_nonconformity.",
    )
    module_mgmtsystem_claim = fields.Boolean(
        "Claims",
        help="Provide claim management tools.\n" "- This installs the module mgmtsystem_claim.",
    )
    module_mgmtsystem_hazard = fields.Boolean(
        "Hazards",
        help="Provide hazard management tools.\n"
        "- This installs the module mgmtsystem_hazard.",
    )
    module_mgmtsystem_document_page = fields.Boolean(
        "Document Pages",
        help="Provide document pages.\n"
        "- This installs the module mgmtsystem_document_page.",
    )
    module_mgmtsystem_manual = fields.Boolean(
        "Manuals",
        help="Provide manuals.\n" "- This installs the module mgmtsystem_manual.",
    )
    module_mgmtsystem_survey = fields.Boolean(
        "Surveys",
        help="Provide surveys.\n" "- This installs the module mgmtsystem_survey.",
    )

    def execute(self):
        """Avoid installing not migrated modules."""
        res = super().execute()
        to_install = []
        for k, v in self._fields.items():
            if k.startswith("module_") and getattr(self, k):
                to_install.append(k.replace("module_", ""))
        if not to_install:
            return res
        module = self.env["ir.module.module"].sudo()
        installed = module.search([("name", "in", to_install)])
        classified = installed._categorize()
        available = classified["module"].mapped("name")
        not_available = set(to_install) - set(available)
        if not_available:
            url = (
                "https://github.com/OCA/management-system/issues"
                "?q=is%3Aissue%20state%3Aopen%20migration%20to%20version"
            )
            msg = _(
                "The following modules are not available: %(addons)s"
                "\nLearn more on the corresponding Github issue"
                " and consider contributing:\n"
            ) % {"addons": ", ".join(not_available)}
            raise exceptions.UserError(msg + url)
        return res