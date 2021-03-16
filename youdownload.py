import subprocess


class YouDownload:

    def __init__(self, param):
        # Define command as string and then split() into list format
        # self.param = '--version'
        # param = 'https://www.youtube.com/watch?v=y8PR4lTAh5E'

        self.executable = 'youtube-dl'
        self.param = '--version'

        self.cmd = self.executable + ' ' + self.param    # used if shell=True
        self.cmd = self.cmd.split(' ')                   # used if shell=False

        # Set the download dir
        # @ToDo use '~/Downloads' as default and make it a property
        self.usedir = '/home/th/Downloads/'

        # Use shell to execute the command
        self.sp = subprocess.Popen(self.cmd,
                                   shell=False,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   cwd=self.usedir,
                                   universal_newlines=True)

        # Separate the output and error in 2 vars
        self.out, self.err = self.sp.communicate()

        # Store the return code in rc variable and
        # wait for process to terminate
        # Alternative is poll() for immediate check
        self.rc = self.sp.wait()

        # Returncode 0 is success
        # print('success') if rc == 0 else print('error')

    @property
    def output(self):
        return '{}'.format(self.out)

    @property
    def warning(self):
        return '{}'.format(self.err)

    @property
    def returncode(self):
        return '{}'.format(self.rc)


# Test
download = YouDownload('--version')
print('Output: ', download.output)
print('Warning error: ', download.warning)
print('Returncode: ', download.returncode)
