# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ResUsers(models.Model):
    _inherit = 'res.users'

    x_nom_sage = fields.Char('Nom dans SAGE')
    x_trigramme = fields.Char('Trigramme')