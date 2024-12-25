import numpy as np
import pandas as pd
from faker import Faker
import random
import plotly.graph_objects as go
from itertools import combinations
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import plotly.express as px
import warnings
from tqdm import tqdm
warnings.filterwarnings("ignore",category=DeprecationWarning)
np.random.seed(52)
random.seed(52)  