import subprocess


class SubProc:
    '''
    Example: 'youtube-dl', '--version'
    xclip
    '''

    def __init__(self, executable, param, shell=False, cwd=None):

        self.executable = executable
        self.param = param
        self.shell = shell
        self.cwd = cwd

        if shell is False:
            self.cmd = [self.executable, self.param]
        else:
            self.cmd = executable + ' ' + param

    @property
    def parameters(self):
        return '{}'.format(self.param)

    def runner(self):
        '''
        Use shell to execute the command
        '''
        self.sp = subprocess.Popen(self.cmd,
                                   shell=self.shell,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   cwd=self.cwd,
                                   universal_newlines=True)

        # Separate the output and error in 2 vars
        self.out, self.err = self.sp.communicate()

        # Store the return code in rc and wait for process to terminate
        self.rc = self.sp.wait()
        resultlist = [self.out, self. err, self.rc]
        return resultlist


# Test
if __name__ == '__main__':

    download = SubProc('youtube-dl', 'https://www.youtube.com/watch?v=iw-L8IC2Y8w', shell=True, cwd='/home/th/Downloads/')
    download2 = SubProc('youtube-dl', 'https://www.youtube.com/watch?v=tP6G2wDrUUU', shell=True, cwd='/home/th/Downloads/')

    results = download.runner()
    results2 = download2.runner()

    # print(results)
    # print(results2)
