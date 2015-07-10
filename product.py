# -*- encoding: utf-8 -*-

##############################################################################
import time
from osv import osv, fields
from tools.translate import _
from openerp.tools.float_utils import float_compare
import pdb


# To add new fields in product

class product_product(osv.osv):

    _inherit = "product.product"

# Function to take Priority for Amount field
    def write(self, cr, uid, ids, vals, context=None): 
    
	if 'default_code' in vals:
	    default_code = vals['default_code']
	
	    default_search = self.pool.get('product.product').search(cr, uid, [('default_code', '=', default_code),('id','!=',ids[0])])
            if default_search:
		raise osv.except_osv(_('Warning!'),_("Item number already exists"))	
		

		
	return super(product_product,self).write(cr, uid, ids, vals, context)

    def onchange_default_code(self, cr, uid, ids, default_code):
        
	if default_code:
	    default_search = self.pool.get('product.product').search(cr, uid, [('default_code', '=', default_code),('id','!=',ids[0])])
            if default_search:
		raise osv.except_osv(_('Warning!'),_("Item number already exists"))	
		return {'value': {'default_code': False}}
        return {}
   

    _columns = {
           # 'default_code': fields.char('Reference', size=80, select=True, required=True),
           }
           
    #_sql_constraints = [
     #   ('default_code_uniq', 'unique(default_code)', 'The code of the account must be unique per company !')
    #]

product_product()

class supplier_class(osv.osv):

    _inherit = "res.partner"
   
    _columns = {
            'pincode': fields.char('Pincode', size=150 , requried=True),
           }
   
supplier_class()
