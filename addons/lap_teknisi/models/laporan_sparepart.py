from odoo import api, fields, models, _


class LaporanSparepart(models.Model):
    _name = 'laporan.sparepart'
    _description = 'Model Kimia Farma Laporan Sparepart'
    _check_company_auto = True
    _rec_name = 'sparepart_id'
    _order = 'sparepart_id asc'

    masuk = fields.Integer(string='Masuk')
    digunakan = fields.Integer(string='Digunakan')
    sisa = fields.Integer(string='Sisa')
    bekas = fields.Integer(string='Bekas')

    keterangan = fields.Char(string='Keterangan')

    active = fields.Boolean(string='Active', default=True)

    laporan_id = fields.Many2one(comodel_name='laporan', string='Laporan')
    mesin_id = fields.Many2one(
        comodel_name='mesin', string='Mesin', related='laporan_id.mesin_id', store=True)
    area_id = fields.Many2one(
        comodel_name='area', string='Area', related='laporan_id.area_id', store=True)

    sparepart_id = fields.Many2one(
        comodel_name='sparepart', string='Nama Sparepart')

    _sql_constraints = [
        ('unique_code_company_id', 'unique(code,company_id)',
         _('This Code already exist!')),
    ]
