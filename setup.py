import cx_Freeze
import os
# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    cx_Freeze.Executable('eyemouseinterface2.py', base=base, target_name = 'eyemouseinterface.py')
]
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
include_files = [(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), os.path.join('lib', 'tk86t.dll')),
                 (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'), os.path.join('lib', 'tcl86t.dll'))]
cx_Freeze.setup(name='Eye Mouse Controller',
      version = '1',
      description = 'Handle Mouse Control with your face',
      options = {'build_exe': {"packages":["zmq","cv2","PyQt5","dlib","win32","pynput","sys","tkinter"],"include_files":include_files}},
      executables = executables)
