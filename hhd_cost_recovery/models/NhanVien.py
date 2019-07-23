from odoo import  models, fields

class NhanVien(models.Model):
    _inherit = 'res.users'
    # _name = 'hhd_cost_recovery.nhanvien'
    nhanvien = fields.Boolean("nhanvien", default=False)

    chiphi_id = fields.One2many("hhd.chiphi", "user_id", String="Nhân Viên", readonly=True)