# Install script for directory: /home/steven/CSC500/gnuradio_exploration/gr-howto/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
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

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/howto" TYPE FILE FILES
    "/home/steven/CSC500/gnuradio_exploration/gr-howto/python/__init__.py"
    "/home/steven/CSC500/gnuradio_exploration/gr-howto/python/am_modulator.py"
    "/home/steven/CSC500/gnuradio_exploration/gr-howto/python/basic.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/howto" TYPE FILE FILES
    "/home/steven/CSC500/gnuradio_exploration/gr-howto/build/python/__init__.pyc"
    "/home/steven/CSC500/gnuradio_exploration/gr-howto/build/python/am_modulator.pyc"
    "/home/steven/CSC500/gnuradio_exploration/gr-howto/build/python/basic.pyc"
    "/home/steven/CSC500/gnuradio_exploration/gr-howto/build/python/__init__.pyo"
    "/home/steven/CSC500/gnuradio_exploration/gr-howto/build/python/am_modulator.pyo"
    "/home/steven/CSC500/gnuradio_exploration/gr-howto/build/python/basic.pyo"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/steven/CSC500/gnuradio_exploration/gr-howto/build/python/bindings/cmake_install.cmake")

endif()

