import backtrader as bt
import backtrader.indicators as btind
from indicator import PCH,PCL

class MyStrategy(bt.Strategy):

	def __init__(self):
		self.PCH = PCH()
		self.PCL = PCL()


	def next(self):
		if self.data.high[0] > self.PCH:
			self.LLPC=self.PCL
			self.buy()

		elif self.data.low[0] < self.PCL:
		# Do something else
			self.HHPC=self.PCH
			self.sell()