import json
import unittest

from google.appengine.ext import ndb
from google.appengine.ext import testbed

from app import main


class MainTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.app_client = main.app.test_client(self)

        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

    def test_hello_endpoint_responds_with_hello_world(self):
        response = self.app_client.get('/hello')

        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.content_type)
        self.assertEqual('hello, world!', json.loads(response.data))
