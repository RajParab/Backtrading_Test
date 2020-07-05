import backtrader as bt

class PCH(bt.Indicator):
    lines = ('PCH',)
    plotinfo = dict(subplot=False)
    params = (('value', 5),)

    def next(self):
        #self.lines.PCH[0] = max(self.data.high[0],self.lines.PCH[0])
        self.lines.PCH[0] = max(self.data.high[-1],self.lines.PCH[0])
        self.lines.PCH[0] = max(self.data.high[-2],self.lines.PCH[0])
        self.lines.PCH[0] = max(self.data.high[-3],self.lines.PCH[0])
        self.lines.PCH[0] = max(self.data.high[-4],self.lines.PCH[0])
        self.lines.PCH[0] = max(self.data.high[-5],self.lines.PCH[0])


class PCL(bt.Indicator):
    lines = ('PCL',)

    params = (('value', 5),)
    plotinfo = dict(subplot=False)
    def next(self):
        #self.lines.PCL[0] = min(self.data.low[0],self.lines.PCL[0])
        self.lines.PCL[0] = min(self.data.low[-1],self.lines.PCL[0])
        self.lines.PCL[0] = min(self.data.low[-2],self.lines.PCL[0])
        self.lines.PCL[0] = min(self.data.low[-3],self.lines.PCL[0])
        self.lines.PCL[0] = min(self.data.low[-4],self.lines.PCL[0])
        self.lines.PCL[0] = min(self.data.low[-5],self.lines.PCL[0])
