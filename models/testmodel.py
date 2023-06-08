from odoo import models, fields, api


class TestModel(models.Model):
    _name = 'testapp.testmodel'
    _description = "TestModel"

    name = fields.Char(string="Title", required=True)
    partner_id = fields.Many2one('res.partner', string="Partner")
    submodel_ids = fields.One2many("testapp.testsubmodel", 'testmodel_id', String="Submodels")
    employee_ids = fields.Many2many('hr.employee', String="Darbuotojai")
