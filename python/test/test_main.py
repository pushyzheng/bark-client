from bark_client import BarkClient, utils
import os
import requests
import unittest

key = os.environ.get('BARK_CLIENT_KEY')
if not key:
    raise Exception('cannot found key')
client = BarkClient(domain='api.day.app', key_list=[key])


class MyTestCase(unittest.TestCase):

    def test_request_get(self):
        content = 'HelloWorld'
        sound = ''
        params = {
            'group': 'test',
            'sound': None if utils.is_blank(sound) else sound
        }
        the_key = client.key_list[0]
        url = 'https://api.day.app/{}/{}'.format(the_key, content)
        resp = requests.get(url, params=params)
        print(resp.url)
        self.assertEqual(resp.url, 'https://api.day.app/{}/{}?group=test'.format(the_key, content))

    def test_get_request_url(self):
        url, params = client.get_request_url(
            content='Hello',
            key=key,
            group='test'
        )
        resp = requests.get(url, params=params)
        self.assertEqual(resp.url, 'https://api.day.app/{}/Hello?group=test'.format(key))


if __name__ == '__main__':
    unittest.main()
