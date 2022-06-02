import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor


def pred_wk(stats):
    
    df_W = pd.read_csv('WK_Clean.csv')
    df_W.loc[df_W['Base Price']<=0,'Base Price']=2
    df_W
    xw= df_W.drop(columns=['Coste','Player','TYPE','Nt'])
    yw= df_W['Coste']




    xw.shape
    yw.shape
    xw_test = np.array(stats)

    rfw = RandomForestRegressor()
    rfw.fit(xw, yw)

    yw_pred = rfw.predict(xw_test)
    return yw_pred