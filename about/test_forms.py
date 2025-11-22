from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'james',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")


    def test_form_name_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="name not provided, but the form is valid")


    def test_form_email_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'james',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="email not provided, but the form is valid")


    def test_form_message_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'james',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Message not provided, but the form is valid")