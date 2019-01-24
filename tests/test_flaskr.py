import unittest
from flask import request
from parameterized import parameterized
import os
import api

class MyAppCase(unittest.TestCase):
	
	def setUp(self):
		api.app.config['TESTING'] = True
		self.app = api.app.test_client()
	
	def test_api_auth_failure(self):
		response = self.app.get('/traffic/api/v1/test')
		data = response.status
		self.assertEqual(data, '401 UNAUTHORIZED')

		
	@parameterized.expand([
		
		('pull traffic data for branden account', '/traffic/api/v1/branden', '{"account":"branden","account_traffic":"10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10"}')
		])
	def test_api_return(self, _, api_path, expected_scores):
		key = os.environ.get('ACCOUNT_API_SECRET')

		response = self.app.get(api_path, headers={"Authorization":key})
		data = response.get_data(as_text=True)
		self.assertEqual(data.strip(), expected_scores)
