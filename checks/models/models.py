# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Checks(models.Model):
    # create metadata
    _name = "module.checks"
    _description = "module to make checks"

    # create fields
    bank_name = fields.Many2one('account.journal', string="Nombre del banco", required=True)
    account_number = fields.Float(string="Numero de Cuenta", required=True)
    client_name = fields.Many2one('res.partner', string="Nombre de Cliente", required=True)
    amount = fields.Float(string="Amount", required=True)
    amount_in_words = fields.Many2one('account.payment', string="Monto en numeros", required=True)

    def print_check(self):
        print("Imprimiendo cheque...")
