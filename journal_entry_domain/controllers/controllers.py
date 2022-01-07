# -*- coding: utf-8 -*-
# from odoo import http


# class JournalEntryDomain(http.Controller):
#     @http.route('/journal_entry_domain/journal_entry_domain/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/journal_entry_domain/journal_entry_domain/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('journal_entry_domain.listing', {
#             'root': '/journal_entry_domain/journal_entry_domain',
#             'objects': http.request.env['journal_entry_domain.journal_entry_domain'].search([]),
#         })

#     @http.route('/journal_entry_domain/journal_entry_domain/objects/<model("journal_entry_domain.journal_entry_domain"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('journal_entry_domain.object', {
#             'object': obj
#         })
