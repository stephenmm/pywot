''' Query a player's vehicle stats '''

from api import API

class Vehicle(API):

	def vehicle_stats(self, lang='en', fields='', account_id=''):

		endpoint = '/tanks/stats/'

		if type(fields) is list:
			fields = self._format_fields(fields)		

		return self._api_call(endpoint=endpoint, fields=fields, language=lang, account_id=account_id)

	def vehicle_achievements(self, lang='en', fields='', account_id=''):

		endpoint = '/tanks/achievements/'

		if type(fields) is list:
			fields = self._format_fields(fields)		

		return self._api_call(endpoint=endpoint, fields=fields, language=lang, account_id=account_id)