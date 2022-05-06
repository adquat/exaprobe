# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.tools.safe_eval import wrap_module

requests = wrap_module(__import__('requests'), ['get', 'post'])

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