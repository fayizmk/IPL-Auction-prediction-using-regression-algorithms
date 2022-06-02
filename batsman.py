import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor



def pred_bat(stats):
   

    df_Ba = pd.read_csv('Batsman_Clean.csv')
    df_Ba.loc[df_Ba['Base Price']<=0,'Base Price']=2

    xba= df_Ba.drop(columns=['Cost','Player','TYPE','Nt'])
    yba= df_Ba['Cost']


    xba.shape
    yba.shape
    xba_test = np.array(stats)
    xba_test.reshape((1,-1))
    rf = RandomForestRegressor()
    rf.fit(xba, yba)

    yba_pred = rf.predict(xba_test)
    return yba_pred