# -*- coding: utf-8 -*-
import json

from odoo import models, fields, api, _
import uuid

class SdPowerbiRecords(models.Model):
    _name = 'sd_powerbi.records'
    _description = 'Power Bi'
    _inherit = ['mail.thread']

    name = fields.Char(requried=True)
    users = fields.Many2many('res.users')
    code = fields.Text()

# TODO: name must be unique

    def tables(self):
        thead = ['AAAA', 'BBBB', 'CCCC']
        tbody = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        return json.dumps({'thead': thead, 'tbody': tbody})
