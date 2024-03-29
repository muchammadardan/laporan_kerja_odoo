from odoo import api, fields, models, _


class Laporan(models.Model):
    _name = 'laporan'
    _description = 'Model Kimia Farma Laporan'
    _check_company_auto = True
    _rec_name = 'no_wo'
    _order = 'id desc'

    DONE_WITH = [
        ('teknisi', 'Teknisi'),
        ('vendor', 'Vendor'),
    ]

    no_wo = fields.Char(string='No. WO', require=True)

    date = fields.Date(string='Tanggal')

    done_with = fields.Selection(string='Dilakukan Oleh', selection=DONE_WITH)

    active = fields.Boolean(string='Active', default=True)

    area_id = fields.Many2one(comodel_name='area', string='Area')
    mesin_id = fields.Many2one(comodel_name='mesin', string='Mesin/Alat')
    nama_teknisi_id = fields.Many2many(comodel_name='nama_teknisi', string='Nama Teknisi/Vendor')
    known_by_id = fields.Many2one(comodel_name='known_by', string='Diketahui Oleh')
    received_by_id = fields.Many2one(comodel_name='received_by', string='Diterima Oleh')



    sparepart_ids = fields.One2many(
        comodel_name='laporan.sparepart', inverse_name='laporan_id', string='Spareparts')

    alat_ids = fields.One2many(
        comodel_name='laporan.alat', inverse_name='laporan_id', string='Alats')

    
    

    _sql_constraints = [
        ('unique_no_wo_company_id', 'unique(no_wo)',
         _('This No WO already exist!')),
    ]
