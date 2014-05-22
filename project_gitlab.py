 #-*- coding: utf-8 -*-

from openerp.osv import fields, osv


class project_gitlab(osv.osv):

    _inherit = "project.project"
    
    _columns = {
        'url_base': fields.text('url_base'),
        'prj_id': fields.integer('prj_id'),
        'private_token': fields.char('private_token', size=21)
    }

project_gitlab()
