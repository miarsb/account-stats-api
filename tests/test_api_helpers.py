import unittest
from parameterized import parameterized
from api_helpers import ReadAccountData

class TestAccountCheck(unittest.TestCase):

	test_object = ReadAccountData('test')



	@parameterized.expand([
		("symbol test", test_object.pull_account_data('test'), '5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5'),
		("symbol test", test_object.pull_account_data('branden'), '10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10'),
	])
	def test_account_check(self, _, account, expected):
		self.assertEqual(account, expected)

	@parameterized.expand([
		("expected input", test_object.format_date('1'), '01'),
		("already in correct format", test_object.format_date('12'), '12'),
		("alternate correct format", test_object.format_date('05'), '05'),
	])
	def test_format_date(self, _, date, expected_date):
		self.assertEqual(date, expected_date)

	@parameterized.expand([
		("date test 20190118", test_object.format_log_file(['20190118']), 'account_score_20190118'),
		("date test 20190205", test_object.format_log_file(['20190205']), 'account_score_20190205'),
		("date test 20181225", test_object.format_log_file(['20181225']), 'account_score_20181225'),
	])
	def test_format_log_file(self, _, date, expected_format):
		self.assertEqual(date[0], expected_format)