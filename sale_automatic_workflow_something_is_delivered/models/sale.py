# Copyright 2020 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    something_is_delivered = fields.Boolean(compute='_compute_something_is_delivered',search="_search_something_is_delivered")

    
    def _search_something_is_delivered(self, operator, value):
        order = False
        if operator == '=':
            orders = self.search([]).filtered(lambda x : x.something_is_delivered == value )
        else:
            orders = self.search([]).filtered(lambda x : x.something_is_delivered == False )
        return [('id', 'in', [x.id for x in orders] if orders else False )]

    @api.depends('state', 'order_line', 'order_line.qty_delivered')
    def _compute_something_is_delivered(self):
        for order in self:
            order.something_is_delivered = False
            for line in order.order_line:
                if line.qty_delivered:
                    order.something_is_delivered = True
                    break
