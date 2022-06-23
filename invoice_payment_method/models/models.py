# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning


class Datos_facturas(models.Model):

	_inherit = 'account.move'

	tipo_factura=fields.Selection([('PUE','PUE - Pago en una sola exhibición'),
	                           ('PPD','PPD - Pago en parcialidades o diferido')])

@api.constrains('l10n_mx_edi_payment_policy')
def _validate_payment_policy(self):
    if self.l10n_mx_edi_payment_policy = 'PUE':
    	raise ValidationError("El método seleccionado es PUE")

