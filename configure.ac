AC_PREREQ([2.68])
AC_INIT([efl-config], [0.1], [jae.hwan.kim@samsung.com])
AC_CONFIG_SRCDIR([src/efl_config.c])
#AC_CONFIG_HEADERS([efl_config.h])

AC_CONFIG_AUX_DIR([.])
AM_INIT_AUTOMAKE([foreign])
# Checks for programs.
AC_PROG_CC
AC_CONFIG_MACRO_DIR([m4])
# Checks for libraries.
DESKTOP=0
AC_CHECK_LIB([elementary])
# Checks for header files.
# Checks for typedefs, structures, and compiler characteristics.
AC_LIBTOOL_DLOPEN
LT_INIT
AC_PROG_LIBTOOL
# Checks for library functions.
PKG_CHECK_MODULES([ELEMENTARY],[elementary])
PKG_CHECK_MODULES([ECOREWAYLAND],[ecore-wayland])

AC_SUBST([DESKTOP])
AC_DEFINE_UNQUOTED([DESKTOP],[${DESKTOP}],["Desktop build is enabled"])
AC_SUBST(TZ_SYS_BIN)
AC_CONFIG_FILES([Makefile
            src/Makefile
            packaging/efl-config.service
            ])
AC_OUTPUT
