
import unittest
import datetime
import uuid
# Assuming your code is in a module named 'your_module'
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        obj = BaseModel()
        self.assertTrue(isinstance(obj.id, uuid.UUID))
        self.assertTrue(isinstance(obj.created_at, datetime.datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime.datetime))
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_save(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)
        self.assertTrue(isinstance(obj.updated_at, datetime.datetime))

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in obj_dict)
        # Assuming you want ID as string in dictionary
        self.assertTrue(isinstance(obj_dict['id'], str))
        self.assertTrue('created_at' in obj_dict)
        # Assuming you want datetime as string
        self.assertTrue(isinstance(obj_dict['created_at'], str))
        self.assertTrue('updated_at' in obj_dict)
        # Assuming you want datetime as string
        self.assertTrue(isinstance(obj_dict['updated_at'], str))

    def test_str(self):
        obj = BaseModel()
        self.assertTrue(isinstance(str(obj), str))
        self.assertTrue(obj.__class__.__name__ in str(obj))
        self.assertTrue(obj.id in str(obj))
        self.assertTrue('created_at' in str(obj))
        self.assertTrue('updated_at' in str(obj))


if __name__ == '__main__':
    unittest.main()
