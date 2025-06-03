# data ingestion is apart f model by reading data from source like database or API
import os
import sys
from src.exception import CustomException
from src.logger import logging 
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
import dataclasses import dataclasses