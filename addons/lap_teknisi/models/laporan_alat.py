import string
from odoo import api, fields, models, _


class LaporanAlat(models.Model):
    _name = 'laporan.alat'
    _description = 'Model Kimia Farma Laporan Alat'
    _check_company_auto = True
    _rec_name = 'alat_id'
    _order = 'alat_id asc'

    jumlah_masuk = fields.Integer(string='Masuk')
    jumlah_keluar = fields.Integer(string='Keluar')
    masalah_kerusakan = fields.Char(string='Masalah Kerusakan')

    active = fields.Boolean(string='Active', default=True)

    laporan_id = fields.Many2one(comodel_name='laporan', string='Laporan')
    mesin_id = fields.Many2one(
        comodel_name='mesin', string='Mesin', related='laporan_id.mesin_id', store=True)
    area_id = fields.Many2one(
        comodel_name='area', string='Area', related='laporan_id.area_id', store=True)

    sparepart_id = fields.Many2one(
        comodel_name='sparepart', string='Nama Sparepart')
    
    alat_id = fields.Many2one(
        comodel_name='alat', string='Nama Alat yang dibawa'
    )

    _sql_constraints = [
        ('unique_code_company_id', 'unique(code,company_id)',
         _('This Code already exist!')),
    ]
