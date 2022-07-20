# -*- coding: utf-8 -*-

from odoo import api, models, fields
import logging
_logger = logging.getLogger(__name__)

class CustomModExtended(models.Model):

    _inherit = 'sale.order'
    cust_number = 25
    actual_num = 23
    sum_num = 0

    def addone(cust_number):
        if cust_number = 25:
            sum_num = actual_num + cust_number

            return sum_num



    
   # return 
    #'cust_number': cust_number,


    
    

