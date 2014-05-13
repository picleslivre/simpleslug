import unittest


class simpleslugTests(unittest.TestCase):

    def test_jsonschema_must_be_present(self):
        self.assertRaises(TypeError, lambda: JsonProbe(json_schema))
