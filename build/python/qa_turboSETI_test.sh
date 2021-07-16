#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir="/Users/mychai/gr-turboseti/python"
export GR_CONF_CONTROLPORT_ON=False
export PATH="/Users/mychai/gr-turboseti/build/python":$PATH
export DYLD_LIBRARY_PATH="":$DYLD_LIBRARY_PATH
export PYTHONPATH=/Users/mychai/gr-turboseti/build/swig:$PYTHONPATH
/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python /Users/mychai/gr-turboseti/python/qa_turboSETI.py 
