import os
from os.path import normpath, join, splitdrive
from pathlib import PureWindowsPath

print(normpath(join(os.getcwd(), "cd")))
print(os.getcwd())
print(os.chdir('..'))
print(splitdrive(os.getcwd()))
print(os.path.abspath(os.curdir))
print(os.getcwd())
p = PureWindowsPath('c:/Program Files/PSF')
print(p.parts)
