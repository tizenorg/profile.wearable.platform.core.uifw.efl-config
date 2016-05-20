MAINTAINERCLEANFILES = Makefile.in Makefile

bin_PROGRAMS = efl_config
efl_config_SOURCES = efl_config.c

efl_config_CFLAGS = $(ELEMENTARY_CFLAGS) $(ECOREWAYLAND_CFLAGS) -ggdb -I../lib -I../ -fPIE
efl_config_LDADD = $(ELEMENTARY_LIBS) $(ECOREWAYLAND_LIBS) -lutil -ldl
efl_config_LDFLAGS = -pie
