# Copyright 2020 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    something_is_delivered = fields.Boolean(compute='_compute_something_is_delivered')

    @api.depends('state', 'order_line', 'order_line.qty_delivered')
    def _compute_something_is_delivered(self):
        for order in self:
            order.something_is_delivered = False
            if order.order_line:
                order.something_is_delivered = any([x.qty_delivered for x in order.order_line])
