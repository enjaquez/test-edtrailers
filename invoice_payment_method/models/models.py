# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning


class Datos_facturas(models.Model):

	_inherit = 'account.move'

	tipo_factura=fields.Selection([('PUE','PUE - Pago en una sola exhibición'),
	                           ('PPD','PPD - Pago en parcialidades o diferido')])

#realizar las validaciones al momento de guardar
@api.constrains('tipo_factura')
def _validate(self):
    if self.tipo_factura:
    	raise UserError(_("Seleccione el Metodo de Pago"
                        	"e intente nuevamente."))

