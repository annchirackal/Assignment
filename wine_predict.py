import  pandas as pd
import pyspark
from pyspark.sql.functions import col
import numpy as np
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from pyspark.mllib.tree import RandomForest, RandomForestModel
val=pd.read_csv("ValidationDataset.csv", sep=";")
for col_name in val.columns[1:-1] + ['""""quality"""""']:
    val = val.withColumn(col_name, col(col_name).cast('float'))
val = val.rename({'""""quality"""""': "label"},inplace=True)
RFModel = RandomForestModel.load("trainingmodel.model")
val.columns = val.iloc[0]

df = val[1:]

print(df.head())


