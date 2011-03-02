from unittest import TestCase
import simplejson as json

class SchemaTestCase(TestCase):
    
    def setUp(self):
        """docstring for setUp"""
        pass
    
    def tearDown(self):
        """docstring for tearDown"""
        pass
    
    def test_schema_loading(self):
        for schema in ['data_record','base_record', 'entity_record']:
            json.load(open('json/%s.json' % schema, 'r'))
        
    