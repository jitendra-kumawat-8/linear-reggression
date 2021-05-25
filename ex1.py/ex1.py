import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import log_loss
from sklearn import preprocessing 
import matplotlib.pyplot as plt

df=pd.read_excel(r'C:\Users\Da Awesomeness\Desktop\ML\Data set\insurance_claims.xlsx')
df1=pd.DataFrame(df)
X=np.array(df1.drop(['total_claim_amount','incident_state','incident_city','auto_model','policy_state','incident_type','collision_type','incident_severity','authorities_contacted','property_damage','police_report_available','fraud_reported','auto_make'],1))
y=np.array(df1['total_claim_amount'])
df.replace(nan,0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
np.isnan(X_train)
np.nan_to_num(X_train)
np.isnan(X_test)
np.nan_to_num(X_test)

print(X_train)