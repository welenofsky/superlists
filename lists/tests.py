from django.test import TestCase
# Here lies all my unit tests for the lists app
# Create your tests here.

class SmokeTest(TestCase):
	def test_bad_maths(self):
		self.assertEqual(1 + 1, 3)