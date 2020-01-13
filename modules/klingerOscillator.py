def klinger_oscillator(df, period):
    """
        Formula for the Klinger Oscillator
        ​	  
        KO = (34 Period EMA of VF)−(55 Period EMA of VF)
        df['ema34'] = df['price'] * (2/(34 + 1)) + df['ema'].shift(periods=1) x (1 - (2/(34 + 1)))
        df['ema55'] = df['price'] * (2/(55 + 1)) + df['ema'].shift(periods=1) x (1 - (2/(55 + 1)))
        #TODO:df['ema'] shift is being called in same function; need to fix
        #TODO: figure out how to call ema for both 34 and 55(nested function) 
        ]
        df['ko'] = df[']
        where:
        KO = Klinger Oscillator
        VF = Volume Force
        Volume Force = V×[2×((dm/cm)−1)]×T×100
        df['vf'] = df['volume'] * (2 * ((df['dm']/df['cm']) -1)) * df['trend'] * 100
        V= Volume df['volume']
        T= Trend
        df['trendpt1'] = df['high']-df['low']-df['close']
        df['trendpt2'] =  df['high'].shift(periods=1) - df['low'].shift(periods=1) - df['close'].shift(periods=1)
        df['trend'] = (df['trendpt1']-df['trendpt2])/abs((df['trendpt1']-df['trendpt2])) 
        Trend=+1 if 
        (H+L+C)>(Hlast+Llast+Clast)]
        Trend=−1 if Above is < or =
        dm=H−L
        df['dm'] = df['high']-df['low']
        
        cm=cm 
        −1
        ​	 +dm if Trend = Trend 
        −1
        ​	 
        cm=dm 
        −1
        ​	 +dm if Trend =/= Trend 
        −1
        ​df.loc[df['dm'] = 0, 'cm'] = df['dm']
        ​df.loc[df['trend'] == df['trend'].shift(periods=1), 'cm'] = df['cm'].shift(periods=1) + df['dm']
        df.loc[df['trend'] != df['trend'].shift(periods=1), 'cm'] = df['dm'].shift(periods=1) + df['dm']
​	"""