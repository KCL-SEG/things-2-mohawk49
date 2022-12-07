from django.test import TestCase
from things.forms import ThingForm


class ThingsFormTestCase(TestCase):

    def setUp(self):
        self.form_input = {
            'name': 'Name',
            'description': 'Orange and small',
            'quantity': 5,
        }
    #Accept valid input data
    def test_valid_data_sign_up_form(self):
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_reject_quantity_too_small(self):
        self.form_input['quantity'] = -3
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_reject_quantity_too_big(self):
        self.form_input['quantity'] = 300
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_reject_quantity_right_amount(self):
        self.form_input['quantity'] = 30
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_name_field_too_long(self):
        self.form_input['name'] = 'a'*36
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_name_field_right_length(self):
        self.form_input['name'] = 'a'*35
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_description_field_too_long(self):
        self.form_input['description'] = 'a'*121
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_description_field_right_length(self):
        self.form_input['description'] = 'a'*120
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())
