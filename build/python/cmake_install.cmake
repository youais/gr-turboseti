# Install script for directory: /Users/mychai/gr-turboseti/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/Applications/GNURadio.app/Contents/MacOS/usr")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti/__init__.py;/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti/turboSETI.py;/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti/find_et.py;/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti/find_et_sync.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti" TYPE FILE FILES
    "/Users/mychai/gr-turboseti/python/__init__.py"
    "/Users/mychai/gr-turboseti/python/turboSETI.py"
    "/Users/mychai/gr-turboseti/python/find_et.py"
    "/Users/mychai/gr-turboseti/python/find_et_sync.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti/__init__.pyc;/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti/turboSETI.pyc;/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti/find_et.pyc;/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti/find_et_sync.pyc;/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti/__init__.pyo;/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti/turboSETI.pyo;/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti/find_et.pyo;/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti/find_et_sync.pyo")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/Applications/GNURadio.app/Contents/MacOS/usr/share/gnuradio/python/site-packages/turboseti" TYPE FILE FILES
    "/Users/mychai/gr-turboseti/build/python/__init__.pyc"
    "/Users/mychai/gr-turboseti/build/python/turboSETI.pyc"
    "/Users/mychai/gr-turboseti/build/python/find_et.pyc"
    "/Users/mychai/gr-turboseti/build/python/find_et_sync.pyc"
    "/Users/mychai/gr-turboseti/build/python/__init__.pyo"
    "/Users/mychai/gr-turboseti/build/python/turboSETI.pyo"
    "/Users/mychai/gr-turboseti/build/python/find_et.pyo"
    "/Users/mychai/gr-turboseti/build/python/find_et_sync.pyo"
    )
endif()

