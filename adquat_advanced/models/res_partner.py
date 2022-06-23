# -*- coding: utf-8 -*-
from odoo import api, fields, models

class x_fournisseurs(models.Model):
    _name = 'x_fournisseurs'
    _description = "Fournisseurs"

    x_name = fields.Char('Name', copy=False)

class x_tiers_sage(models.Model):
    _name = 'x_tiers_sage'
    _description = "Tiers Sage"

    x_name = fields.Char('Name', required=True, copy=False)
    x_CT_Adresse = fields.Char('CT_Adresse', copy=False)
    x_CT_Ape = fields.Char('CT_Ape', copy=False)
    x_CT_CodePostal = fields.Char('CT_CodePostal', copy=False)
    x_CT_Complement = fields.Char('CT_Complement', copy=False)
    x_CT_EMail = fields.Char('CT_EMail', copy=False)
    x_CT_Identifiant = fields.Char('CT_Identifiant', copy=False)
    x_CT_Intitule = fields.Char('CT_Intitule', copy=False)
    x_CT_Num = fields.Char('CT_Num', copy=False)
    x_CT_Pays = fields.Char('CT_Pays', copy=False)
    x_CT_Siret = fields.Char('CT_Siret', copy=False)
    x_CT_Telephone = fields.Char('CT_Telephone', copy=False)
    x_CT_Ville = fields.Char('CT_Ville', copy=False)
    x_Commentaires = fields.Char('Commentaires')
    x_Siren = fields.Char('Siren', copy=False)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # FIELDS BOOLEAN
    x_locked = fields.Boolean('Verrouillé')

    # FIELDS CHAR
    x_SIREN = fields.Char('SIREN')
    x_cisco_smartaccount = fields.Char('Cisco Smart Account')
    x_numero_client = fields.Char('Numéro de client', index=True, copy=False)

    # FIELDS M2M
    x_tiers_sage = fields.Many2many('x_tiers_sage', 'x_res_partner_x_tiers_sage_rel', 'res_partner_id',
                                   'x_tiers_sage_id', string='Tiers Sage')

    # FIELDS M2O
    x_sale_specialist = fields.Many2one('res.users', string='Vendeur spécialisé', ondelete='set null')

    # FIELDS SELECTION
    x_categorie = fields.Selection([('Prospect', 'Prospect'), ('Client', 'Client'),('Abandonné', 'Abandonné'),
                                    ('Bloqué', 'Bloqué'), ('Autre', 'Autre')], 'Catégorie')
    x_priority = fields.Selection([('0', 'Faible'), ('1', 'Moyen'),
                                   ('2', 'Elevé'), ('3', 'Très haut')], 'Priorité', index=True)
