class Frame:
    def __init__(self, name='', size=60, separator='='):
        self.name = name
        self.size = size
        self.separator = separator
        self.grid = self.separator * self.size
        self.frame()

    def frame(self):
        print(f'\n{self.grid}', f'\n{self.name.center(self.size)}', f'\n{self.grid}\n')
