import sys
import os
from  dataclasses import dataclasses

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer  # to create pipeline
from sklearn.impute import SimpleImputer  # missing data
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging

@dataclasses
class DataTranformationConfig:    # this will give any path we require for datatransforming
    preprocess_obj_file_path=os.path.join('artifacts','preprocessor.pkl') 