# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    amount_paid = fields.Float(
        compute='_get_amount_paid',
    )
    amount_due = fields.Float(
        compute='_get_amount_due',
    )

    @api.depends('invoice_ids')
    def _get_amount_paid(self):
        for record in self:
            record.amount_paid = sum(invoice.amount_total for invoice in record.invoice_ids)  # TODO

    @api.depends('amount_paid', 'amount_total')
    def _get_amount_due(self):
        for record in self:
            record.amount_due = record.amount_total - record.amount_paid