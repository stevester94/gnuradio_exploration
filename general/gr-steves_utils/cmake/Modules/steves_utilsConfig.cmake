INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_STEVES_UTILS steves_utils)

FIND_PATH(
    STEVES_UTILS_INCLUDE_DIRS
    NAMES steves_utils/api.h
    HINTS $ENV{STEVES_UTILS_DIR}/include
        ${PC_STEVES_UTILS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    STEVES_UTILS_LIBRARIES
    NAMES gnuradio-steves_utils
    HINTS $ENV{STEVES_UTILS_DIR}/lib
        ${PC_STEVES_UTILS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/steves_utilsTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(STEVES_UTILS DEFAULT_MSG STEVES_UTILS_LIBRARIES STEVES_UTILS_INCLUDE_DIRS)
MARK_AS_ADVANCED(STEVES_UTILS_LIBRARIES STEVES_UTILS_INCLUDE_DIRS)
