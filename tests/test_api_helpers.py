import unittest
from parameterized import parameterized
import api_helpers

class TestAccountCheck(unittest.TestCase):
	@parameterized.expand([
		("fake account", '1111', 'Account Not Found'),
		("symbol test", '!$@#@$', 'Account Not Found'),
	])
	def test_account_check(self, _, account, expected):
		self.assertEqual(api_helpers.pull_account_traffic(account), expected)

	@parameterized.expand([
		("expected input", '1', '01'),
		("already in correct format", '12', '12'),
		("alternate correct format", '05', '05'),
	])
	def test_format_date(self, _, date, expected_date):
		self.assertEqual(api_helpers.format_date(date), expected_date)

	@parameterized.expand([
		("date test 20190118", ['20190118'], 'account_score_20190118'),
		("date test 20190205", ['20190205'], 'account_score_20190205'),
		("date test 20181225", ['20181225'], 'account_score_20181225'),
	])
	def test_format_log_file(self, _, date, expected_format):
		self.assertEqual(api_helpers.format_log_file(date)[0], expected_format)