import backtrader as bt
import datetime
#from indicator import DummyInd
from startegy import MyStrategy

data = bt.feeds.YahooFinanceCSVData(
	dataname=r'D:\Raj\clearmind consultancy\HDFC.NS.csv',
	fromdate=datetime.datetime(2002, 7, 1),
    todate=datetime.datetime(2019, 12, 31),

    nullvalue=0.0,

    dtformat=('%Y-%m-%d'),

    datetime=0,
    high=1,
    low=2,
    open=3,
    close=4,
    volume=5,
    openinterest=-1
	)

cerebro = bt.Cerebro()
print('Portfolio value at start: %s' %(cerebro.broker.getvalue()))
cerebro.adddata(data) 
cerebro.addstrategy(MyStrategy)
cerebro.run() 
print('Portfolio value at end: %s' %(cerebro.broker.getvalue()))
cerebro.plot(style='candestick')