import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor

def pred_ar(stats):

    df_Ar = pd.read_csv('AR_Clean.csv')

    df_Ar.loc[df_Ar['Base Price']<=0,'Base Price']=2

    x= df_Ar.drop(columns=['Cost','Player','TYPE','Nt'])
    y= df_Ar['Cost']


    x.shape
    y.shape

    rf = RandomForestRegressor()

    rf.fit(x, y)
 
    x_test = np.array(stats)
    x_test.reshape((1,-1))
    y_pred = rf.predict(x_test)
    return y_pred