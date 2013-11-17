__author__ = 'reyoung'

import unittest
from slidegen2.document_formatters.yaml_formatter import YAMLFormatter


class TestYamlFormatter(unittest.TestCase):
    def test_yaml_formatter(self):
        test_data = """
list_group:
  id: id
  content:
    - one
    - two
    - three
---
list_group:
  id: id2
  content:
    - 1
    - 2
    - 3
"""
        fmt = YAMLFormatter(content=test_data)
        for k, v in fmt.get_command_iterator():
            self.assertEqual(k, "list_group")
            self.assertIsInstance(v, dict)
            self.assertIn("id", v)
            self.assertIn("content", v)


if __name__ == '__main__':
    unittest.main()
