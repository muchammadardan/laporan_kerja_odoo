from odoo import api, fields, models, _

class NamaTeknisi(models.Model):
    _name = 'nama_teknisi'
    _description = 'Model Laporan Name Teknisi'
    _check_company_auto = True
    _rec_name = 'name'
    _order = 'name asc'


    name = fields.Char(string='Name', required=True)

    active = fields.Boolean(string='Active', default=True)


    _sql_constraints = [
        ('unique_code_company_id', 'unique(code,company_id)',
        ('This Code already exist!')),
    ]

