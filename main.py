import yfinance as yf
import plotly as plt
import pandas as pd
import datetime as dt
import plotly.graph_objects as go
import os
import talib as tb

try:
  tkr = input()
  start = dt.datetime.now() - dt.timedelta(days = 730)
  end = dt.datetime.now()
  data = yf.download(tkr , start = start, end = end)
except:
  print('Invalid ticker Rerun program')
   



spinning_top = tb.CDLSPINNINGTOP(data['Open'], data['High'], data['Low'], data['Close'])

green_marubozu = tb.CDLCLOSINGMARUBOZU(data['Open'], data['High'], data['Low'], data['Close'])

doji = tb.CDLDOJI(data['Open'], data['High'], data['Low'], data['Close'])

hammer = tb.CDLHAMMER(data['Open'], data['High'], data['Low'], data['Close'])

inverted_hammer = tb.CDLINVERTEDHAMMER(data['Open'], data['High'], data['Low'], data['Close'])

hanging_man = tb.CDLHANGINGMAN(data['Open'], data['High'], data['Low'], data['Close'])

shooting_star = tb.CDLSHOOTINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

engulfing = tb.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])

harami = tb.CDLHARAMI(data['Open'], data['High'], data['Low'], data['Close'])

harami_cross = tb.CDLHARAMICROSS(data['Open'], data['High'], data['Low'], data['Close'])

homing_piegon = tb.CDLHOMINGPIGEON(data['Open'], data['High'], data['Low'], data['Close'])

morning_star = tb.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

evening_star = tb.CDLEVENINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

white_soldiers = tb.CDL3WHITESOLDIERS(data['Open'], data['High'], data['Low'], data['Close'])

black_crows = tb.CDL3BLACKCROWS(data['Open'], data['High'], data['Low'], data['Close'])

three_inside = tb.CDL3INSIDE(data['Open'], data['High'], data['Low'], data['Close'])

rising_falling_three = tb.CDLRISEFALL3METHODS(data['Open'], data['High'], data['Low'], data['Close'])


data['Spinning Top'] = spinning_top
data['Green Marubozu'] = green_marubozu
data['Doji'] = doji
data['Hammer'] = hammer
data['Inverted Hammer'] = inverted_hammer
data['Hangin Man'] = hanging_man
data['Shooting Star'] = shooting_star
data['Engulfing'] = engulfing
data['Harami'] = harami
data['Harami Cross'] = harami_cross
data['Homing Piegeon'] = homing_piegon
data['Morning Star'] = morning_star
data['Evening Star'] = evening_star
data['White Soldier'] = white_soldiers
data['Black Crows'] = black_crows
data['Three Inside'] = three_inside
data['Rising Falling Three'] = rising_falling_three


with pd.ExcelWriter('pattern_recoginzer.xlsx') as writer:
  data.to_excel(writer)