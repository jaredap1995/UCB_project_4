import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import psycopg2
from sklearn.preprocessing import OrdinalEncoder
from sqlalchemy import create_engine
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle
import warnings
warnings.filterwarnings('ignore')

