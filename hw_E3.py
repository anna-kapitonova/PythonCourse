import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_boston
boston = load_boston()
boston_df = pd.DataFrame(boston['data'], columns=boston['feature_names'])
boston_df['PRICE'] = boston.target
print ("Columns: " + " ".join (boston_df.columns))

plt.scatter (boston_df["AGE"], boston_df["PRICE"])
plt.xlabel ("Proportion of owner-occupied units built prior to 1940")
plt.ylabel ("Price")
plt.show ()

plt.scatter (boston_df["PTRATIO"], boston_df["PRICE"])
plt.xlabel ("Pupil-teacher ratio by town")
plt.ylabel ("Price")
plt.show ()

plt.scatter (boston_df["DIS"], boston_df["PRICE"])
plt.xlabel ("Weighted distances to five Boston employment centres")
plt.ylabel ("Price")
plt.show ()
