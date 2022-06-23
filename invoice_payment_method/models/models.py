# -*- coding: utf-8 -*-
from odoo import models, exceptions, fields, api, _
from odoo.exceptions import UserError, ValidationError

class Datos_facturas(models.Model):

	_inherit = 'account.move'
	tipo_factura=fields.Selection([('PUE','PUE - Pago en una sola exhibición'),
	                           ('PPD','PPD - Pago en parcialidades o diferido')])

	@api.constrains('tipo_factura','l10n_mx_edi_payment_method_id')
	def _validate_tipo_factura(self):
		for record in self:
			print (ecord.l10n_mx_edi_payment_method_id)
			if record.tipo_factura == 'PUE' and record.l10n_mx_edi_payment_method_id == '99':
				raise ValidationError(_('Si el método de pago es PUE, entonces la forma de pago debe ser diferente a 99 - Por definir - Selecciona otras opciones'))


