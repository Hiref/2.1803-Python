class DateTest():
	def __init__(self,year,month,day):
		self.year = year
		self.month = month
		self.day = day
	def outDate(self):
		print("%s年%s月%s日"%(self.year,self.month,self.day))
	@classmethod
	def handleDate(cls,date):
		a,b,c = date.split("-")
		Date = cls(a,b,c)
		return Date
DateTest.handleDate("2018-05-04").outDate()





