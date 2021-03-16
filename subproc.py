import subprocess


class SubProc:
    '''
    Example: 'youtube-dl', '--version'
    xclip
    '''

    def __init__(self, executable, param):

        self.executable = executable
        self.param = param
        self.cmd = [self.executable, self.param]

    @property
    def parameters(self):
        return '{}'.format(self.param)

    def run(self):
        '''
        Use shell to execute the command
        '''
        self.sp = subprocess.Popen(self.cmd,
                                   shell=False,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   cwd=None,
                                   universal_newlines=True)

        # Separate the output and error in 2 vars
        self.out, self.err = self.sp.communicate()

        # Store the return code in rc and wait for process to terminate
        self.rc = self.sp.wait()

        resultlist = [self.out, self. err, self.rc]
        return resultlist


# Test
download = SubProc('youtube-dl', '--version')
print(download.parameters)

results = download.run()
print(results)
