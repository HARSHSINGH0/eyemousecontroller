from PyQt5 import QtCore, QtGui, QtWidgets
import eyetracking
from PyQt5 import sip
import cv2 as cv
cv2=cv
import dlib
import mousecontrol_eye
import eyemouseinterface2
from win32.win32api import GetSystemMetrics
from pynput.mouse import Listener,Button,Controller
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Freeze
# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    cx_Freeze.Executable('eyemouseinterface2.py', base=base, target_name = 'eyemouseinterface2.py')
]

cx_Freeze.setup(name='Eye Mouse Controller',
      version = '1',
      description = 'Handle Mouse Control with your face',
      options = {'build_exe': {"packages":["zmq","cv2","PyQt5","dlib","win32","pynput","sys"],"include_files":["icon.ico","eyemouseinterface2.py","eyetracking.py","mousecontrol_eye.py","instruction.png","shape_predictor_68_face_landmarks.dat"]}},
      executables = executables)
