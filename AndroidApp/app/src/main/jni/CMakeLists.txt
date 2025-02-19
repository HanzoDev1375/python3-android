cmake_minimum_required(VERSION 3.4.1)
project(pythonthread)

set(CMAKE_ANDROID_STL_TYPE gnustl_shared)
set(CMAKE_SYSTEM_VERSION 23)

# configure directory variables for use throughout this file
set(distribution_dir ${CMAKE_SOURCE_DIR}/../jniLibs)
set(jni_src_dir ${CMAKE_SOURCE_DIR}/../jni)

if (${CMAKE_SYSTEM_PROCESSOR} STREQUAL "x86_64")
    include_directories(${jni_src_dir}/Pythonx86_64)
else()
    include_directories(${jni_src_dir}/Python64)
endif()

# set all our include directories (header locations)
include_directories(${jni_src_dir}/python
        ${jni_src_dir}/pdd
        ${jni_src_dir}/pdd/os
        ${jni_src_dir}
)

# define the 3rd party libraries to include in this project
add_library(python312 SHARED IMPORTED)
set_target_properties(python312 PROPERTIES IMPORTED_LOCATION ${distribution_dir}/${ANDROID_ABI}/libpython3.12.so IMPORTED_NO_SONAME TRUE)

# set various C and CXX(++) flags
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -DNDEBUG")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++11")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fexceptions")

# recursive wildcard search to find all the right cpp and c source files to compile
file(GLOB_RECURSE source_files ${jni_src_dir}/pdd/*.cpp
        ${jni_src_dir}/pdd/os/*.cpp
        ${jni_src_dir}/*.cpp)
SET( python_source ${source_files})

# finally, set up our python library and attach the source files above (this causes cmake to compile the sources)
add_library(pythonthread SHARED ${python_source})
# set our python library to be C++
SET_TARGET_PROPERTIES (pythonthread PROPERTIES LINKER_LANGUAGE CXX)

# lastly, set to link against the 3rd party libs above
target_link_libraries(pythonthread
                      python312
                      log
                      atomic
                      android)
