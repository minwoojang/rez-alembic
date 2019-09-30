name = "alembic"

version = "1.7.11"

authors = [
    "Sony Pictures Imageworks"
]

description = \
    """
    Alembic is an open framework for storing and sharing scene data that includes a C++ library, a file format,
    and client plugins and applications.
    """

requires = [
    "gcc-6",
    "cmake-3",
    "ilmbase-2.2.1",
    "openexr-2.2.1"
]

variants = [
    ["platform-linux"]
]

tools = [
    "abcdiff",
    "abcecho",
    "abcechobounds",
    "abcls",
    "abcstitcher",
    "abctree"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

#TODO: Use the SHA1 of the archive instead.
uuid = "alembic-1.7.11"

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
