class Athlete:
    def __init__(self, a_name, a_DOB = None , a_times = []):
        self.name = a_name
        self.DOB = a_DOB
        self.times = a_times
    def getLen(self):
        return (len(self.times))
Sarah = Athlete("Sarah Sweeney","2002-6-17",['2:58','2.58','2:39'])
print(A.getLen())