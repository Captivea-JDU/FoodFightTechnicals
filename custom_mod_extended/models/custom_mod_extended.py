# -*- coding: utf-8 -*-

from odoo import api, models, fields
import logging
_logger = logging.getLogger(__name__)

class CustomModExtended(models.Model):

    _inherit = 'sale.order'
    cust_number = env['res.partner'].phone

    
   # return 
    #'cust_number': cust_number,


    
    

