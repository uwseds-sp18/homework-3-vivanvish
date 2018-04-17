# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 19:20:40 2018

@author: vivan
"""
import unittest
import homework3

class TestCreateDataframe(unittest.TestCase):
    
    def test_column_names(self):
        df = homework3.create_dataframe('class.db')
        req_columns = set(['video_id', 'category_id', 'language'])
        self.assertEqual(set(df.columns),req_columns)
        
    def test_num_rows(self):
        df = homework3.create_dataframe('class.db')
        self.assertEqual(df.shape[0],75005)
    
    def test_keys(self):
        df = homework3.create_dataframe('class.db')
        self.assertNotEqual(len(df.groupby(['video_id','language'])),df.shape[0])
        self.assertNotEqual(len(df.groupby(['category_id','language'])),df.shape[0])
        self.assertNotEqual(len(df.groupby(['video_id','category_id'])),df.shape[0])
        self.assertNotEqual(len(df.groupby(['video_id','category_id','language'])),df.shape[0])

    def test_error_raised(self):
        with self.assertRaises(ValueError):
            homework3.create_dataframe('data/class.db')
            
suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateDataframe)
_ = unittest.TextTestRunner().run(suite)
    