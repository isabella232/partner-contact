# Copyright 2017 LasLabs Inc.
# Copyright 2017 Camptocamp
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models, tools
import os

testing = tools.config.get('test_enable') or os.environ.get('ODOO_TEST_ENABLE')

if testing:
    class ResPartner(models.Model):
        _inherit = 'res.partner'

        social_security = fields.Char(
            compute=lambda s: s._compute_identification(
                'social_security', 'SSN',
            ),
            inverse=lambda s: s._inverse_identification(
                'social_security', 'SSN',
            ),
            search=lambda s, *a: s._search_identification(
                'SSN', *a
            ),
        )
