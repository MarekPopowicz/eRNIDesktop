class RestorationAgent:
    def __init__(self):
        self.data = []

    def pushValue(self, fieldValue):
        self.data.append(fieldValue)

    def getValues(self):
        return  self.data

    def clearValues(self):
        self.data.clear()
