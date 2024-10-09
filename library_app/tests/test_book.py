# noinspection PyUnresolvedReferences
from odoo.tests.common import TransactionCase


class TestBook(TransactionCase):

	def setUp(self, *args, **kwargs):
		super().setUp(*args, **kwargs)
		user_admin = self.env.ref("base.user_admin") # finds the admin user record, using its XML ID.
		self.env = self.env(user=user_admin) # modifies the environment used to run the tests, self.env, changing the active user to the admin user
		self.Book = self.env["library.book"]
		self.book1 = self.Book.create({
			"name": "Odoo Development Essentials",
			"isbn": "879-1-78439-279-6"
		})
	def test_book_create(self):
		"New Books are active ny default"
		self.assertEqual(
			self.book1.active, True
		)

	def test_check_isbn(self):
		"Check valid ISBN"
		self.assertTrue(self.book1._check_isbn)

