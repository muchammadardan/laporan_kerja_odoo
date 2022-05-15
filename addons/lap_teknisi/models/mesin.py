from odoo import api, fields, models, _


class Mesin(models.Model):
    _name = 'mesin'
    _description = 'Model Kimia Farma Mesin'
    _check_company_auto = True
    _rec_name = 'name'
    _order = 'name asc'

    name = fields.Char(string='Name', required=True)

    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('unique_cname_company_id', 'unique(name)',
         _('This Name already exist!')),
    ]
