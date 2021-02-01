# -*- coding: utf-8 -*-

from odoo import models, fields


class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course Info'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    level = fields.Selection([('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advance', 'Advance')])
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed')])

    def action_confirm(self):
        self.write({'state': 'Confirmed'})