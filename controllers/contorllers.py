# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
from odoo.modules.module import get_module_resource
# from odoo.addons.http_routing.models.ir_http import url_for
from odoo.tools import ustr
from datetime import datetime, timedelta
# import datetime
import jdatetime
from werkzeug.wrappers import Response

from icecream import ic
import logging
import json
import base64

class SdPowerbiData(http.Controller):
    @http.route('/powerbi/<string:name>', type='http', auth='none')
    @http.route('/powerbi/<string:name>/<int:count>', type='http', auth='public')
    def get_html_table(self, name='', count=0):
        auth = request.httprequest.authorization
        # ic(request.httprequest.environ)
        if not auth:
            return Response(
                "Unauthorized",
                status=401,
                headers={"WWW-Authenticate": 'Basic realm="PowerBI"'}
            )
        else:
            powerbi_records = request.env['sd_powerbi.records'].sudo().search([('name', '=', name)])
            if powerbi_records:
                data = powerbi_records.tables()
                # ic(data)
                return request.render('sd_powerbi.powerbi_table', json.loads(data))
            else:

                thead = ['Power', 'Bi', 'Sandbox']
                tbody = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                return request.render('sd_powerbi.powerbi_table', {'thead': thead, 'tbody': tbody})

    @http.route('/powerbi/', type='http', auth='none')
    # It is useful to test and setup powerbi to read data from this module without any authentication overhead
    def get_sandbox_table(self,):
        thead = ['Power', 'Bi', 'Sandbox']
        tbody = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        return request.render('sd_powerbi.powerbi_table', {'thead': thead, 'tbody': tbody})