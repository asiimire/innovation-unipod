from email.policy import default

from odoo import models, fields


class Book(models.Model):
	_name = "library.book" #declares the new library.book model
	_description ="Book"
	# model fields
	name = fields.Char("Title", required=True)
	isbn = fields.Char("ISBN")
	active = fields.Boolean("Active?", default=True) #The active field is used for active records. By default, only active records are shown, and inactive records are automatically hidden.
	date_published = fields.Date()
	image = fields.Binary("Cover")
	publisher_id = fields.Many2one("res.partner", string="Publisher")
	author_ids = fields.Many2many("res.partner", string="Authors")