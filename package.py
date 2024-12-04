name = "alembic"

version = "1.8.5"

authors = [
    "Sony Pictures Imageworks"
]

description = \
    """
    Alembic is an open framework for storing and sharing scene data that includes a C++ library, a file format,
    and client plugins and applications.
    """

requires = [
    "boost",
    "cmake",
    "gcc",
    "ilmbase",
    "pyilmbase",
    "python"
]

variants = [
    ["platform-linux","arch-x86_64"]
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
    env.PYTHONPATH.prepend("{root}/lib/python" + str(env.REZ_PYTHON_MAJOR_VERSION) + "." + str(env.REZ_PYTHON_MINOR_VERSION) + "/site-packages")
    env.CMAKE_MODULE_PATH.prepend("{root}/lib/cmake/Alembic")

    # Helper environment variables.
    env.ALEMBIC_BINARY_PATH.set("{root}/bin")
    env.ALEMBIC_INCLUDE_PATH.set("{root}/include")
    env.ALEMBIC_LIBRARY_PATH.set("{root}/lib")
