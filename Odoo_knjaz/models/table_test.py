import time
from random import randrange

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    test = fields.Char(
        string='Test value',
    )

    @api.onchange('date_order', 'order_line')
    def _onchange_test(self):
        for rec in self:
            if not rec.partner_id:
                rec.test = str(randrange(100000000))
            else:
                date = rec.date_order.strftime('%m/%d/%Y %H:%M:%S')
                rec.test = f'{rec.amount_total} - {date}'

    @api.constrains('test')
    def check_len_field(self):
        for rec in self:
            if rec.test and len(rec.test) > 50:
                raise ValidationError(
                    'Длина текста должна быть меньше 50 символов!'
                )
