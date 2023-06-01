#!/usr/bin/python3

"""
The test module for base_model
"""
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittestt.Testcase):
    """ define the  TestCaseModel class"""

    def setup(self):
        """create an instance"""
        self.base_model = BaseModel()

    def tearDown(self):
        """delete the instance"""
        del self.base_model

    def test_type(self):
        """test if the the tyoe of BaseModel is a class"""
        self.assertEqual(str(type(self.base_model)),
                            "<class 'models.base_model.BaseModel'>")
    def test_id(self):
        """test if the class has a unique id"""
        base_model2 = BaseModel()
        self.assertNotEqual(self.base_model.id, base_model2.id)

    def test_created_at(self):
        """test if it contains the created_at attribute"""
        self.assertTrue(hasattr(self.base_model, "created_at"))

    def test_updated_at(self):
        """test if it contains the updated_at attribute"""
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_str(self):
        """test for the __str__ method"""
        expected_output = f"[{type(self.base_model).__name__}] "\
            f"({self.base_model.id}) "\
            f"{self.base_model.__dict__}"

        self.assertEqual(expected_output, str(self.base_model))

    def test_save(self):
        """test for the save method"""
        self.base_model.save()
        self.assertNotEqual(self.base_model.created_at,
                            self.base_model.updated_at)

    def test_to_dict(self):
        """test the to_dict method"""
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict["id"], self.base_model.id)
        self.assertEqual(base_model_dict["created_at"],
                        self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict["updated_at"],
                        self.base_model.updated_at.isoformat())
        self.assertEqual(base_model_dict["__class__"],
                        type(self.base_model).__name__)

    def test_new(self):
        """test the new method of FileStorage"""
        storage = FileStorage()
        storage.reload()
        base_model = BaseModel()
        storage.new(base_model)
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        self.assertIn(key, storage.all())

    def test_reload(self):
        """test the reload method"""
        storage = FileStorage()
        base_model = BaseModel()
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        storage.new(base_model)
        storage.save()
        os.remove("file.json")
        self.assertFalse(os.path.exists("file.json"))
        storage.reload()
        self.assertTrue(os.path.exists("file.json"))
        self.assertIn(key, storage.all())

if __name__ == '__main__':
    unittest.main()


