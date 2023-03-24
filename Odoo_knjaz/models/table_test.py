import time
from random import randrange

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    test = fields.Char(
        string='Test value',
    )

    @api.onchange('date_order', 'amount_total')
    def _change_test_field(self):
        for rec in self:
            rec.test = f'{rec.amount_total} - {rec.date_order}'

    @api.constrains('test')
    def check_len_field(self):
        for rec in self:
            if rec.test and len(rec.test) > 50:
                raise ValidationError(
                    'Длина текста должна быть меньше 50 символов!'
                )
    
    @api.model
    def create(self, vals):
        if not vals.get('test'):
            vals['test'] = str(randrange(100000000))
        return super().create(vals)
