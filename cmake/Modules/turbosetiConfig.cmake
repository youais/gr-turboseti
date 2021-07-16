INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_TURBOSETI turboseti)

FIND_PATH(
    TURBOSETI_INCLUDE_DIRS
    NAMES turboseti/api.h
    HINTS $ENV{TURBOSETI_DIR}/include
        ${PC_TURBOSETI_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /Applications/GNURadio.app/Contents/MacOS//usr/local/include
          /Applications/GNURadio.app/Contents/MacOS/usr/include
)

FIND_LIBRARY(
    TURBOSETI_LIBRARIES
    NAMES gnuradio-turboseti
    HINTS $ENV{TURBOSETI_DIR}/lib
        ${PC_TURBOSETI_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /Applications/GNURadio.app/Contents/MacOS/usr/local/lib
          /Applications/GNURadio.app/Contents/MacOS/usr/local/lib64
          /Applications/GNURadio.app/Contents/MacOS/usr/lib
          /Applications/GNURadio.app/Contents/MacOS/usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/turbosetiTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(TURBOSETI DEFAULT_MSG TURBOSETI_LIBRARIES TURBOSETI_INCLUDE_DIRS)
MARK_AS_ADVANCED(TURBOSETI_LIBRARIES TURBOSETI_INCLUDE_DIRS)
