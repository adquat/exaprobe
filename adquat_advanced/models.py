# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from werkzeug import urls

from odoo import api, fields, models
import requests

class ServerAction(models.Model):
    """ Add website option in server actions. """

    _name = 'ir.actions.server'
    _inherit = 'ir.actions.server'

    @api.model
    def _get_eval_context(self, action):
        """ Override to add the request object in eval_context. """
        eval_context = super(ServerAction, self)._get_eval_context(action)
        if action.state == 'code':
            eval_context['requests'] = requests

        return eval_context

    # def run(self):
    #     import requests
    #     return super(ServerAction, self).run()