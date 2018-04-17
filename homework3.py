# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 19:02:12 2018

@author: Vishnu Nandakumar
"""

import pandas as pd
import sqlite3
import os

#Create and return the query result as a dataframe.
def create_dataframe(path):
    if os.path.exists(path):
        con = sqlite3.connect(path)
        query = "SELECT video_id, category_id, 'us' AS language FROM USvideos \
        			UNION ALL \
        			SELECT video_id, category_id, 'gb' AS language FROM GBvideos   \
        			UNION ALL  \
        			SELECT video_id, category_id, 'ca' AS language FROM CAvideos   \
        			UNION ALL   \
        			SELECT video_id, category_id, 'de' AS language FROM DEvideos    \
        			UNION ALL    \
        			SELECT video_id, category_id, 'fr' AS language FROM FRvideos;"
        df = pd.read_sql(query,con=con)
        return df
    else:
        raise ValueError('Error: Database does not exist! Please check the path provided.')
    
