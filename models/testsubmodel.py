from odoo import models, fields, api


class TestSubModel(models.Model):
    _name = 'testapp.testsubmodel'
    _description = "TestModel"

    name = fields.Char(string="Title", required=True)
    testmodel_id = fields.Many2one('testapp.testmodel', string="Test Model")
