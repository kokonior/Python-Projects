import string
from odoo import models, fields, api

class Anggota(models.Model):
    _name = 'bima.anggota'
    _description = 'Menyimpan Data Anggota'

    no_anggota = fields.Char()
    name = fields.Char()
    alamat = fields.Char()
    agama_ids = fields.Many2one(string="Nama Agama",comodel_name="bima.agama",ondelete="restrict")
