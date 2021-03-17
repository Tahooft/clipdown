from subproc import SubProc

middleclip = SubProc('xclip', '-o')
clipped = middleclip.runner()
print('clipped:\n', clipped)
