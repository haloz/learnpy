import unittest

from bytes import bytestr


class ByteStrTestCase(unittest.TestCase):
    def test_to_str(self):
        """
        Test for the to_str function in bytestr
        Assumes the to_str function always returns a str if passed a str or a
        byte sequence.
        """
        result = "test"
        self.assertEqual(result, bytestr.to_str("test"))
        self.assertEqual(result, bytestr.to_str(bytes("test", "utf-8")))

    def test_to_bytes(self):
        """
        Test for the to_bytes function in bytestr
        Assumes the to_bytes function always returns a byte sequence if passed a
        str or a byte sequence.
        """
        result = bytes("test", "utf-8")
        self.assertEqual(result, bytestr.to_bytes(bytes("test", "utf-8")))
        self.assertEqual(result, bytestr.to_bytes("test"))


if __name__ == '__main__':
    unittest.main()
