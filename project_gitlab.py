 #-*- coding: utf-8 -*-

from openerp.osv import fields, osv


class project_gitlab(osv.osv):

    _inherit = "project.project"
    
    _columns = {
        'url_base': fields.text('gitlab_url_base'),
        'prj_id': fields.integer('gitlab_prj_id'),
        'private_token': fields.char('gitlab_private_token', size=21)
    }

project_gitlab()
