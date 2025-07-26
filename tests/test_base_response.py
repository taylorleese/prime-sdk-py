import unittest
from dataclasses import dataclass
from typing import List, Optional
from prime_sdk.base_response import BaseResponse

# Create a test response class that inherits from BaseResponse
@dataclass
class TestResponse(BaseResponse):
    field1: Optional[str] = None
    field2: Optional[int] = None
    field3: Optional[dict] = None
    field4: Optional[List[dict]] = None

class TestBaseResponse(unittest.TestCase):
    def test_initialization(self):
        # Test that BaseResponse subclasses can be initialized with fields
        test_response = TestResponse(
            field1='value1',
            field2=123,
            field3={'nested_field': 'nested_value'},
            field4=[{'list_field': 'list_value'}]
        )

        self.assertEqual(test_response.field1, 'value1')
        self.assertEqual(test_response.field2, 123)
        self.assertEqual(test_response.field3['nested_field'], 'nested_value')
        self.assertEqual(test_response.field4[0]['list_field'], 'list_value')

    def test_str_representation(self):
        # Test the JSON string representation
        test_response = TestResponse(field1='value1')
        # The output will be indented JSON
        expected = '''{
  "field1": "value1",
  "field2": null,
  "field3": null,
  "field4": null
}'''
        self.assertEqual(str(test_response), expected)

    def test_nested_dataclass_conversion(self):
        # Test that nested dictionaries are converted to dataclasses
        from dataclasses import dataclass
        from typing import List
        
        @dataclass
        class NestedModel:
            name: str
            
        @dataclass
        class TestNestedResponse(BaseResponse):
            # BaseResponse only converts non-Optional dataclass fields
            nested: NestedModel = None
            # And lists of dataclasses
            nested_list: List[NestedModel] = None
            
        # When initialized with a dict, it should convert to NestedModel
        response = TestNestedResponse(nested={'name': 'test'})
        self.assertIsInstance(response.nested, NestedModel)
        self.assertEqual(response.nested.name, 'test')
        
        # Test list conversion
        response2 = TestNestedResponse(nested_list=[{'name': 'item1'}, {'name': 'item2'}])
        self.assertIsInstance(response2.nested_list, list)
        self.assertEqual(len(response2.nested_list), 2)
        self.assertIsInstance(response2.nested_list[0], NestedModel)
        self.assertEqual(response2.nested_list[0].name, 'item1')

if __name__ == '__main__':
    unittest.main() 