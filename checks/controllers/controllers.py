# -*- coding: utf-8 -*-
# from odoo import http


# class Checks(http.Controller):
#     @http.route('/checks/checks', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/checks/checks/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('checks.listing', {
#             'root': '/checks/checks',
#             'objects': http.request.env['checks.checks'].search([]),
#         })

#     @http.route('/checks/checks/objects/<model("checks.checks"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('checks.object', {
#             'object': obj
#         })

