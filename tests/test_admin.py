# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase


class FormFieldStashAdminTests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
