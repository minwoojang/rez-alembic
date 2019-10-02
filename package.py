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
    "gcc-6+",
    "cmake-3+",
    "ilmbase-2.2.1<2.4",
    "openexr-2.2.1<2.4"
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

uuid = "alembic-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    # Helper environment variables.
    env.ALEMBIC_BINARY_PATH.set("{root}/bin")
    env.ALEMBIC_INCLUDE_PATH.set("{root}/include")
    env.ALEMBIC_LIBRARY_PATH.set("{root}/lib")
