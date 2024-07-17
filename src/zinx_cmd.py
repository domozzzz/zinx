from downloader import download_thread

__all__ = ('run_cmd')

class Cmd():
    def __init__(self, prefix='', suffix='', length=50):
        self.total = 0
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
    
    def download(self, site, loc):
        download_thread(self, site, loc) 

    def set_total(self, total):
        self.total = total   

    def print_progress(self, iteration):
        percent = ("{0:.1f}").format(100 * (iteration / float(self.total))) 
        filled_length = int(self.length * iteration // self.total) 
        bar = '█' * filled_length + '-' * (self.length - filled_length)
        print(f'\r{self.prefix} |{bar}| {percent}% {self.suffix}', end="\r")
        if self.total == iteration:
            print()

def run_cmd(argv):
    cmd = Cmd(prefix='Progress', suffix="Complete", length=50)
    cmd.download(argv[0], argv[1])
