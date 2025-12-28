# -*- coding: utf-8 -*-
##############################################################################
# Author: Mastercore Sinapsys Global®
# Copyright: 2019-Present.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
#
###############################################################################

from odoo import fields, models

class MgmtsystemActionTag(models.Model):
    _name = "mgmtsystem.action.tag"
    _description = "Action Tags"

    name = fields.Char(required=True)
    color = fields.Integer(string="Color Index", default=10)

    _sql_constraints = [("name_uniq", "unique (name)", "Tag name already exists !")]