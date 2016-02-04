export BIN_PATH=/usr/
libtoolize
autoreconf -ivf
./configure --prefix ${BIN_PATH}
