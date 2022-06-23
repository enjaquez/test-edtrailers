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
			#raise ValidationError (record.l10n_mx_edi_usage)
			if record.tipo_factura == 'PUE' and record.l10n_mx_edi_payment_method_id.name == 'Por definir':
				raise ValidationError(_('Si el método de pago es PUE, entonces la forma de pago debe ser diferente a 99 - Por definir - Selecciona otras opciones'))

			if record.tipo_factura == 'PPD' and record.l10n_mx_edi_payment_method_id.name != 'Por definir':
				raise ValidationError(_('Si el método de pago es PPD, entonces la forma de pago debe ser  99 - Por definir'))

			if record.partner_id.vat != 'XAXX010101000' and record.partner_id.vat != 'XEXX010101000' and record.l10n_mx_edi_usage == 'P01':
				raise ValidationError(_('El Uso debe ser diferente a Por Definir, selecciona otra opción'))

			if ( record.partner_id.vat == 'XAXX010101000' or record.partner_id.vat == 'XEXX010101000' ) and record.l10n_mx_edi_usage != 'P01':
				raise ValidationError(_('El Uso debe ser Por Definir, selecciona la opción correctamente'))

