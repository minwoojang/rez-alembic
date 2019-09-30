#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

EXTRACT_PATH=$1
BUILD_PATH=$2
INSTALL_PATH=${REZ_BUILD_INSTALL_PATH}
ALEMBIC_VERSION=${REZ_BUILD_PROJECT_VERSION}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "================="
echo -e "=== CONFIGURE ==="
echo -e "================="
echo -e "\n"

echo -e "[CONFIGURE][ARGS] EXTRACT PATH: ${EXTRACT_PATH}"
echo -e "[CONFIGURE][ARGS] BUILD PATH: ${BUILD_PATH}"
echo -e "[CONFIGURE][ARGS] INSTALL PATH: ${INSTALL_PATH}"
echo -e "[CONFIGURE][ARGS] ALEMBIC VERSION: ${ALEMBIC_VERSION}"

# We run the configuration script of Alembic.
echo -e "\n"
echo -e "[CONFIGURE] Running the configuration script from Alembic-${ALEMBIC_VERSION}..."
echo -e "\n"

if [ -d ${BUILD_PATH} ]; then
    cd ${BUILD_PATH}
else
    mkdir -p ${BUILD_PATH}
    cd ${BUILD_PATH}

    cmake ${BUILD_PATH}/.. -DCMAKE_INSTALL_PREFIX=${INSTALL_PATH} -DCMAKE_C_FLAGS=-fPIC -DCMAKE_CXX_FLAGS=-fPIC -DILMBASE_ROOT=${REZ_ILMBASE_ROOT} -DOPENEXR_ROOT=${REZ_OPENEXR_ROOT}
fi

echo -e "\n"
echo -e "[CONFIGURE] Finished configuring Alembic-${ALEMBIC_VERSION}!"
echo -e "\n"
