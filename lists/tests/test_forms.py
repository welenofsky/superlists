from django.test import TestCase

from lists.forms import EMPTY_LIST_ERROR, ItemForm


class ItemFormTest(TestCase):

	def test_form_renders_item_text_input(self):
		form = ItemForm()
		self.assertIn('placeholder="Enter a to-do item"', form.as_p())
		self.assertIn('class="form-control input-lg"', form.as_p())

	def test_form_validation_for_blank_items(self):
		form = ItemForm(data={'text': ''})
		# Calling form.is_valid() returns True or False, 
		# but it also has the side effect of validating the input data, 
		# and populating the errors attribute
		self.assertFalse(form.is_valid())
		self.assertEqual(
			form.errors['text'],
			[EMPTY_LIST_ERROR]
		)