"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import doctest

from django.test import TestCase

import helpers

def suite():
    return doctest.DocTestSuite(helpers)
