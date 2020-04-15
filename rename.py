import os, glob, re


class Rename:
    def __init__(self, path, extension, expression):
        self.main_path = path
        self.extension = extension
        self.files = glob.glob(os.path.join(self.main_path, f'*.{self.extension}'))
        # print(self.files)
        self.expression = expression
        # self.rename()
        # self.replace_white_to_underline()

    def replace_white_to_underline(self):
        for f in self.files:
            print(f)
            f_list = f.split("\\")
            name = f_list[-1]
            try:
                new = name.replace(" ", "_")
                new_path = os.path.join(self.main_path, new)
                os.rename(f, new_path)
            except Exception as e:
                print(str(e))

    def rename(self, optional=''):
        for i, f in enumerate(self.files):
            f_list = f.split("\\")
            name = f_list[-1]
            _, ext = os.path.splitext(name)
            try:
                new_name = f'{self.expression}{str(i+1).zfill(2)}{optional[i]}{ext}'
            except IndexError:
                new_name = f'{self.expression}{str(i+1).zfill(2)}{ext}'
            new_path = os.path.join(self.main_path, new_name)
            try:
                os.rename(f, new_path)
            except Exception as e:
                print(str(e))

    def strip_ep_name(self):
        optional = []
        for i, f in enumerate(self.files):
            f_list = f.split("\\")
            name, ext = os.path.splitext(f_list[-1])
            ep_name = name.strip((r'"Mr.Robot."(.*?)".720p.WEB-DL.x264-[MULVAcoded]"'))
            ep_name = re.sub(r'^r.', '', ep_name)
            ep_name = re.sub(r"eps2.\d{1,2}(.|_)", "", ep_name)
            episode = ep_name.split('.')[3]
            optional.append(f".{episode}")
        self.rename(optional)


if __name__ == "__main__":
    Rename(input('Path: \n'), input('File extension: \n'), input('Expression to rename batch to: \n'))