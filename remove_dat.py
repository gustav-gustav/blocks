import glob, os, sys, time


class Remove:
    def __init__(self):
        self.path = sys.argv[-1]
        if self.confirmation():
            self.main()

    def confirmation(self):
        print(f'Are you sure you want to run remove_dat.py on {self.path}?')
        c = input('Type the bool:')
        return eval(c)

    def main(self):
        os.chdir(self.path)
        files = glob.glob(os.path.join(os.getcwd(), '**', '*dat'), recursive=True)
        for f in files:
            print(f'removing {f}...')
            os.remove(f)
            time.sleep(0.1)

if __name__ == '__main__':
    Remove()
