from numpy import interp

class Progress:
    def __init__(self, value, end, title='Downloading',buffer=50):
        self.title = title
        self.end = end - 1
        self.buffer = buffer
        self.value = value
        self.progress()

    def progress(self):
        maped = int(interp(self.value, [0, self.end], [0, self.buffer]))
	print(f'{self.title}: [{"#"*maped}{"-"*(self.buffer - maped)}] {self.value}/{self.end} {((self.value/self.end)*100):.2f}%', end='\r')
