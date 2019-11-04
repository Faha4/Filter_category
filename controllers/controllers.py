# -*- coding: utf-8 -*-
from odoo import http

# class ModuleUn(http.Controller):
#     @http.route('/module_un/module_un/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_un/module_un/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_un.listing', {
#             'root': '/module_un/module_un',
#             'objects': http.request.env['module_un.module_un'].search([]),
#         })

#     @http.route('/module_un/module_un/objects/<model("module_un.module_un"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_un.object', {
#             'object': obj
#         })