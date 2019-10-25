from django.test import TestCase
from report.models import ErrorReport

class ErrorReportTest(TestCase):

	def test_string_representation_of_object(self):
		"""
		Test string representation of error report object.
		Every django.db.models object returns an unfriendly 
		representation for objects, this test is to check that
		such is not the case for ErrorReport object.

		Actual:
		object_representation = unfriendly_string
		
		Expected:
		object_representation = humanly_readable_string
		"""
		errorOne = ErrorReport(
			name="ModuleNotFound: no module named coverage_report")
		self.assertEquals(
			errorOne.__str__(), 
			"ModuleNotFound: no module named coverage_report")