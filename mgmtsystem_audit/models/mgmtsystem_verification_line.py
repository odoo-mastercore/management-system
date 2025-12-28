# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################
# Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MgmtsystemVerificationLine(models.Model):
    """Class to manage verification's Line."""

    _name = "mgmtsystem.verification.line"
    _description = "Verification Line"
    _order = "seq"

    name = fields.Char("Question", required=True)
    audit_id = fields.Many2one(
        "mgmtsystem.audit", "Audit", ondelete="cascade", index=True
    )
    procedure_id = fields.Many2one(
        "document.page", "Procedure", ondelete="restrict", index=True
    )
    is_conformed = fields.Boolean(default=False)
    comments = fields.Text()
    seq = fields.Integer("Sequence")
    company_id = fields.Many2one(
        "res.company", "Company", default=lambda self: self.env.company
    )