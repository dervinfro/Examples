#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 23:41:25 2021

@author: user
"""

import pandas as pd
import censusdata

census_dir = censusdata.printtable(censusdata.censustable('acs5','2018','B02001'))

states = censusdata.geographies(censusdata.censusgeo([('state','17'),('county','031')]), 'acs5',2018)

print(states)

# cook_census = censusdata.download('acs5',2018,censusdata.censusgeo([('state','17'),('county','031')]),
# ['B02001_001E','B02001_002E','B02001_003E','B02001_004E','B02001_005E','B02001_006E','B02001_007E'])


# cook_describe = cook_census.describe()
# cook_census['cook_white'] = cook_census.B02001_002E
