import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor



def pred_bowl(stats):


    df_Bo = pd.read_csv('Bowler_Clean.csv')
    df_Bo
    df_Bo.loc[df_Bo['Base Price']<=0,'Base Price']=2

    xb= df_Bo.drop(columns=['Cost','Player','TYPE','Nt'])
    yb= df_Bo['Cost']

  
  
    xb.shape
    yb.shape

    xb_test = np.array(stats)

    rfb = RandomForestRegressor()
    rfb.fit(xb, yb)

    yb_pred = rfb.predict(xb_test)
    return yb_pred 