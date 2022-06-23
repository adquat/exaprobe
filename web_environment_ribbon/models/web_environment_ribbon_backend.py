# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models
from odoo.http import request

class WebEnvironmentRibbonBackend(models.AbstractModel):

    _name = "web.environment.ribbon.backend"
    _description = "Web Environment Ribbon Backend"

    @api.model
    def _prepare_ribbon_format_vals(self):
        company_id = request and request.httprequest.cookies.get('cids') or '1'
        company_id = int(company_id[0])
        company_name = self.env['res.company'].browse(company_id).name
        return {"db_name": self.env.cr.dbname,
                "company": company_name,}

    @api.model
    def _prepare_ribbon_name(self):
        name_tmpl = self.env["ir.config_parameter"].sudo().get_param("ribbon.name")
        vals = self._prepare_ribbon_format_vals()
        return name_tmpl and name_tmpl.format(**vals) or name_tmpl

    @api.model
    def get_environment_ribbon(self):
        """
        This method returns the ribbon data from ir config parameters
        :return: dictionary
        """
        ir_config_model = self.env["ir.config_parameter"]
        name = self._prepare_ribbon_name()

        current_company = request and request.httprequest.cookies.get('cids') or '1'
        back_color = ir_config_model.sudo().get_param("ribbon.background.color_%s" % current_company[0]) \
                     or ir_config_model.sudo().get_param("ribbon.background.color")
        color = ir_config_model.sudo().get_param("ribbon.color_%s" % current_company[0]) \
                     or ir_config_model.sudo().get_param("ribbon.color")

        return {
            "name": name,
            "color": color,
            "background_color": back_color,
        }
