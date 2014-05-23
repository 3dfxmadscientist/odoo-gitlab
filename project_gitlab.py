 #-*- coding: utf-8 -*-

from openerp.osv import fields, osv


class project_gitlab(osv.osv):

    _inherit = "project.project"
    _columns = {
        'url_base': fields.char('Base api url', size=200),
        'prj_id': fields.integer('Gitlab project id'),
        'private_token': fields.char('Access private token', size=21),
        'prj_group': fields.char('Gitlab repo group', size=30),
        'repo_exists': fields.boolean('repo_exists')
    }

    def _create_repo(self, cr, uid, context=None):
        self.write(cr, uid, context, {'private_token': 'new'})
        return True


project_gitlab()
