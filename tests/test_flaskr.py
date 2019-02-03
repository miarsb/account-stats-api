import unittest
from flask import request
from parameterized import parameterized
import os
import api

class MyAppCase(unittest.TestCase):
	
	def setUp(self):
		api.app.config['TESTING'] = True
		self.app = api.app.test_client()
		self.key = os.environ.get('ACCOUNT_API_SECRET')
	
	def test_api_auth_failure(self):
		response = self.app.get('/traffic/api/v1/test')
		data = response.status
		self.assertEqual(data, '401 UNAUTHORIZED')

	def test_api_missing_account(self):
		response = self.app.get('/traffic/api/v1/1111', headers={"Authorization":self.key})
		data = response.status
		self.assertEqual(data, '404 NOT FOUND')

	@parameterized.expand([
		('pull traffic data for test account', '/traffic/api/v1/test', '{"account":"test","account_traffic":"5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5"}'),
		('pull traffic data for branden account', '/traffic/api/v1/branden', '{"account":"branden","account_traffic":"10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10"}')
		])
	def test_api_return(self, _, api_path, expected_scores):
		

		response = self.app.get(api_path, headers={"Authorization":self.key})
		data = response.get_data(as_text=True)
		self.assertEqual(data.strip(), expected_scores)
