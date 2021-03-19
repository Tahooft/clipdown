import time
from regulars import isValidURL
from subproc import SubProc


def deloop():

    clipboard = 'go'

    while clipboard != 'Stop':

        middleclip = SubProc('xclip', '-o')
        clipped = middleclip.runner()

        out = clipped[0]
        # err = clipped[1]
        # rc = clipped[2]

        if out != clipboard:
            clipboard = out
            print('Changed!')

            if isValidURL(clipboard):
                print('Valid')

                download = SubProc('youtube-dl', clipboard)
                downloaded = download.runner()
                print('0 is success! : ', downloaded[2])

        print('\nout:', out, '\n')
        print('\ncbd:', clipboard, '\n')

        # print('er:', err, '\n')
        # print('rc:', rc, '\n')

        time.sleep(5)


deloop()
