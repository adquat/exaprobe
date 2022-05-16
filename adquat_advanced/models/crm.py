# -*- coding: utf-8 -*-
from odoo import api, fields, models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    #FIELDS FLOAT
    x_tdp_nb_jours_CT = fields.Float('Nombre de jours CT', copy=False)
    x_tdp_nb_jours_CDP = fields.Float('Nombre de jours CDP', copy=False)
    x_tdp_nb_jours = fields.Float('Nombre de jours')
    x_nb_jours = fields.Float('Nombre de jours', help='Nombre de jours vendus')
    x_adv_nb_jours_CT = fields.Float('Nombre de jours CT', copy=False)
    x_adv_nb_jours_CDP = fields.Float('Nombre de jours CDP', copy=False)
    x_adv_nb_jours = fields.Float('Nombre de jours', copy=False)

    #FIELDS MONETARY
    x_tdp_ca = fields.Monetary(string='CA')
    x_tdp_marge = fields.Monetary(string='Marge')
    x_tdp_achats = fields.Monetary(string='Achats', copy=False)
    x_tdp_ca_servinteg = fields.Monetary(string='CA services intégration', copy=False)
    x_tdp_ca_renew = fields.Monetary(string='Coûts récurrents')
    x_renew_montant = fields.Monetary(string='Montant du renouvellement')
    x_adv_marge = fields.Monetary(string='Montant marge', copy=False)
    x_adv_ca_servinteg = fields.Monetary(string='CA service integration HT', copy=False)
    x_adv_ca = fields.Monetary(string='Total CA HT', copy=False)
    x_adv_achats = fields.Monetary(string='Total achats HT', copy=False)
    x_achats_UGAP = fields.Monetary(string='Achats Cisco $ (hors maintenance)', help='Montant des achats Cisco en $')

    #FIELDS NOTES
    x_tdp_notes = fields.Text(string='Notes', copy=False)
    x_adv_verif_details = fields.Text(string='Vérification de la commande - détails', copy=False)
    x_adv_remarques = fields.Text(string='Remarques', copy=False)
    x_adv_commentaire_adv = fields.Text(string='Commentaire ADV', copy=False)

    # FIELDS SELECTION
    # CONSEIL NE PAS METTRE LIBELLE EN VALEUR
    x_adv_pack_exa_date = fields.Selection([('Date licence', 'Date de la licence'), ('Date P.V.', 'Date du P.V.'),
                                            ('Date ferme', 'Date ferme')], 'Date de démarrage du Pack Exa', copy=False)
    x_adv_bu = fields.Selection([('RESSEC', 'Réseau et sécurité'), ('SMO', 'Smart office'),
                                 ('GSP', 'Global Service Providers')], 'BU', copy=False)

    # FIELDS M2O
    x_sous_traitant_id = fields.Many2one('res.partner', string='En sous-traitance de', ondelete='set null',
                     help="En cas de sous-traitance, renseigner le nom de l'entité dont Exaprobe est le sous-traitant")
    x_sale_specialist = fields.Many2one('res.users', string='Vendeur spécialisé', ondelete='set null')
    x_renewed_opp = fields.Many2one('crm.lead', string='Opportunité renouvelée', ondelete='set null')
    x_renew_opp = fields.Many2one('crm.lead', string='Opportunité du renouvellement à venir', ondelete='set null')
    x_currency_id = fields.Many2one('res.currency', string='Currency', ondelete='set null')

    # FIELDS M2M
    x_fournisseurs = fields.Many2many('x_fournisseurs', 'x_crm_lead_x_fournisseurs_rel', 'crm_lead_id',
                                   'x_fournisseurs_id', string='Fournisseurs')

    # FIELDS INTEGER
    x_tdp_duree = fields.Integer('Durée en mois')
    x_renew_duree = fields.Integer("Durée de l'affaire en mois")

    # FIELDS BINARY
    x_adv_achat_file = fields.Binary('Devis achats', copy=False)
    x_adv_achat_file2 = fields.Binary('Devis achats 2', copy=False)
    x_adv_achat_file3 = fields.Binary('Devis achats 3', copy=False)
    x_adv_achat_file4 = fields.Binary('Devis achats 4', copy=False)
    x_adv_achat_file5 = fields.Binary('Devis achats 5', copy=False)
    x_adv_commande_file = fields.Binary('Commande client', copy=False)
    x_adv_commande2_file = fields.Binary('Commande client 2', copy=False)
    x_adv_commande3_file = fields.Binary('Commande client 3', copy=False)
    x_adv_fiche_client_file = fields.Binary('Fiche création client', copy=False)
    x_adv_fiche_livraison_file = fields.Binary('Fiche livraison', copy=False)
    x_adv_fiche_nouveau_fournisseur_file = fields.Binary('Fiche création fournisseur', copy=False)
    x_adv_fichier1_file = fields.Binary('Autre fichier', copy=False)
    x_adv_fichier2_file = fields.Binary('Autre fichier 2', copy=False)
    x_adv_fichier3_file = fields.Binary('Autre fichier 3', copy=False)
    x_adv_justificatif_file = fields.Binary('Justificatif 1', copy=False)
    x_adv_justificatif2_file = fields.Binary('Justificatif 2', copy=False)
    x_adv_justificatif3_file = fields.Binary('Justificatif 3', copy=False)
    x_adv_nouv_client_kbis_file = fields.Binary('Kbis nouveau client', copy=False)
    x_adv_nouv_client_rib_file = fields.Binary('RIB nouveau client', copy=False)
    x_adv_offre_commerciale_file = fields.Binary('Offre commerciale', copy=False)
    x_tdp_file = fields.Binary('Fichier TDP', copy=False)

    #FIELDS BOOLEAN
    x_UGAP_install = fields.Boolean('Installation sur site')
    x_adv_BDJ = fields.Boolean('Banque de jours')
    x_adv_TAM_SDM = fields.Boolean('Jours TAM / SDM')
    x_adv_derogation_anticipation = fields.Boolean('Dérogation anticipation de commande', copy=False)
    x_adv_derogation_crea_fournisseur = fields.Boolean('Dérogation création de nouveau fournisseur')
    x_adv_derogation_marge = fields.Boolean('Dérogation Marge', copy=False)
    x_adv_derogation_politique_achat = fields.Boolean('Dérogation politique achat', copy=False)
    x_adv_force_commande = fields.Boolean('Forcer la commande')
    x_adv_hno = fields.Boolean('HNO', copy=False)
    x_adv_nouveau_client = fields.Boolean('Nouveau client')
    x_adv_nouveau_fournisseur = fields.Boolean('Nouveau fournisseur', copy=False)
    x_adv_pack_exa = fields.Boolean('Pack Exa', copy=False)
    x_adv_pack_exa_247 = fields.Boolean('Pack 24/7', copy=False)
    x_adv_pack_exa_gtr = fields.Boolean('Pack GTR', copy=False)
    x_adv_reassurance = fields.Boolean('Reassurance', copy=False)
    x_adv_servmng = fields.Boolean('Services managés', copy=False)
    x_adv_urgent = fields.Boolean('Urgent', copy=False)
    x_tdp_BDJ = fields.Boolean('Banque de jours')
    x_tdp_TAM_SDM = fields.Boolean('Jours TAM / SDM')
    x_tdp_hno = fields.Boolean('HNO', copy=False)
    x_tdp_pack_exa = fields.Boolean('Pack Exa', copy=False)
    x_tdp_pack_exa_247 = fields.Boolean('Pack 24/7')
    x_tdp_pack_exa_gtr = fields.Boolean('Pack GTR')
    x_tdp_reassurance = fields.Boolean('Reassurance', copy=False)
    x_tdp_servmng = fields.Boolean('Service managés')

    #FIELDS DATE
    x_adv_date_demarrage = fields.Date('Date butoir de livraison', copy=False)
    x_adv_date_validite_conditions = fields.Date('Date de validité des conditions', copy=False)
    x_adv_pack_exa_date_specifique = fields.Date('Pack Exa - Date ferme', copy=False)

    #FIELDS CHAR
    x_adv_achat_filename = fields.Char('Nom du fichier devis achats', copy=False)
    x_adv_achat_filename2 = fields.Char('Nom du fichier devis achats 2', copy=False)
    x_adv_achat_filename3 = fields.Char('Nom du fichier devis achats 3', copy=False)
    x_adv_achat_filename4 = fields.Char('Nom du fichier devis achats 4', copy=False)
    x_adv_achat_filename5 = fields.Char('Nom du fichier devis achats 5', copy=False)
    x_adv_caff_lie = fields.Char('Caff lié', copy=False)
    x_adv_cdp = fields.Char('Chef de projet', copy=False)
    x_adv_cisco_smartaccount = fields.Char('Cisco Smart Account', copy=False)
    x_adv_code_affaire = fields.Char('Code affaire', copy=False)
    x_adv_code_affaire_2 = fields.Char('Code affaire 2', copy=False)
    x_adv_commande_filename = fields.Char('Nom de fichier de la commande client', copy=False)
    x_adv_commande2_filename = fields.Char('Nom du fichier commande client 2', copy=False)
    x_adv_commande3_filename = fields.Char('Nom du fichier commande client 3', copy=False)
    x_adv_equipe = fields.Char('Equipe commerciale', copy=False)
    x_adv_etat_commande = fields.Char('Etat de la commande', copy=False)
    x_adv_fiche_client_filename = fields.Char('Nom du fichier de création client', copy=False)
    x_adv_fiche_livraison_filename = fields.Char('Nom du fichier de la fiche livraison', copy=False)
    x_adv_fiche_nouveau_fournisseur_filename = fields.Char('Nom du fichier fiche création fournisseur', copy=False)
    x_adv_fichier1_filename = fields.Char('Nom du fichier 1', copy=False)
    x_adv_fichier2_filename = fields.Char('Nom du fichier 2', copy=False)
    x_adv_fichier3_filename = fields.Char('Nom du fichier 3', copy=False)
    x_adv_ic = fields.Char('Commercial', copy=False)
    x_adv_ic2 = fields.Char('Commercial 2', copy=False)
    x_adv_ic_trig = fields.Char('Trigramme commercial', copy=False)
    x_adv_ic2_trig = fields.Char('Trigramme commercial 2', copy=False)
    x_adv_id_tache_wrike = fields.Char('ID de la tâche Wrike', copy=False)
    x_adv_justificatif_filename = fields.Char('Nom du fichier justificatif 1', copy=False)
    x_adv_justificatif2_filename = fields.Char('Nom du fichier justificatif 2', copy=False)
    x_adv_justificatif3_filename = fields.Char('Nom du fichier justificatif 3', copy=False)
    x_adv_lien_srv_avv = fields.Char('Lien dossier avant-vente', copy=False)
    x_adv_lien_wrike = fields.Char('Lien Wrike ADV', copy=False)
    x_adv_nom = fields.Char("Nom de l'ADV", copy=False)
    x_adv_nom_client = fields.Char('Nom client', copy=False)
    x_adv_nom_projet = fields.Char('Nom du projet', copy=False)
    x_adv_nouv_client_kbis_filename = fields.Char('Nouveau client Kbis nom de fichier', copy=False)
    x_adv_nouv_client_rib_filename = fields.Char('RIB nouveau client nom de fichier', copy=False)
    x_adv_offre_commerciale_filename = fields.Char('Nom du fichier offre commerciale', copy=False)
    x_adv_partenaires = fields.Char('Partenaires', copy=False)
    x_adv_tache_wrike = fields.Char('Nom de la tâche Wrike', copy=False)
    x_adv_verif = fields.Char('Vérification de la commande')
    x_cisco_smartaccount = fields.Char('Cisco Smart Account')
    x_numero_client = fields.Char('Numéro de client', readonly=True, copy=False)
    x_numero_opportunite = fields.Char("Numéro d'opportunité", index=True, copy=False)
    x_partner_address_email = fields.Char('Courriel de contact du partenaire', readonly=True, copy=False)
    x_renew_caff = fields.Char('Courriel de contact du partenaire')
    x_tdp_bu = fields.Char('BU', copy=False)
    x_tdp_caff_lie = fields.Char('Caff lié', copy=False)
    x_tdp_filename = fields.Char('Nom du fichier TDP')
    x_tdp_ic_trig = fields.Char('Trigramme commercial', copy=False)
    x_tdp_import_date = fields.Char("Date d'import du TDP")
    x_tdp_lien_srv_avv = fields.Char('Lien serveur AVV', copy=False)
    x_tdp_nom_client = fields.Char('Nom de client')
    x_tdp_nom_projet = fields.Char('Nom projet')
    x_tdp_numero_client = fields.Char('Numéro de client')
    x_tdp_partenaires = fields.Char('Partenaires', copy=False)
    x_tdp_status = fields.Char('Statut du TDP')
    x_tdp_version = fields.Char("Version de l'offre")
    x_tdp_version_tdp = fields.Char('Version de TDP', copy=False)

    #FIELDS COMPUTED
    x_margin_rate = fields.Float(string='Taux de Marge', compute='_compute_x_margin_rate_new', store=True, tracking=102)
    x_margin = fields.Monetary(string='Marge', compute='_compute_x_margin_new', store=True, tracking=102)

    #FIELDS FUNTIONS
    #CONSEIL : INCOHERENCES ICI, LES 2 CHAMPS CALCULES SE CALCULENT AVEC L'AUTRE. CERTAIN DU COMPORTEMENT SOUHAITE OU REMPLI PAR ACTION ?
    @api.depends('expected_revenue', 'x_margin')
    def _compute_x_margin_rate_new(self):
        for record in self:
            if record.x_margin_rate != 0:
                record.x_margin = record.expected_revenue * record.x_margin_rate / 100

    @api.depends('expected_revenue', 'x_margin_rate')
    def _compute_x_margin_new(self):
        for record in self:
            if record.expected_revenue != 0:
                record.x_margin_rate = record.x_margin / record.expected_revenue * 100