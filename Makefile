######################################################################
#
# DESCRIPTION: Verilator Example: Small Makefile
#
# This calls the object directory makefile.  That allows the objects to
# be placed in the "current directory" which simplifies the Makefile.
#
# Copyright 2003-2018 by Wilson Snyder. This program is free software; you can
# redistribute it and/or modify it under the terms of either the GNU
# Lesser General Public License Version 3 or the Perl Artistic License
# Version 2.0.
#
######################################################################
# Check for sanity to avoid later confusion

ifneq ($(words $(CURDIR)),1)
 $(error Unsupported: GNU Make cannot build in directories containing spaces, build elsewhere: '$(CURDIR)')
endif


TB := sim_top.cpp
TOP := top




OPT_FLAGS ?= -O3 --trace --trace-max-array 128 

VERILATOR_OPTS ?= \
	$(OPT_FLAGS) 		\
	-Wall 					\
	-Wno-WIDTH 			\
	-Wno-UNUSED 		\
	-Wno-BLKSEQ 		\
	-Wno-fatal 			\
	--Wno-lint 			\
	--cc 						\
	--autoflush     


#




######################################################################

# This is intended to be a minimal example.  Before copying this to start a
# real project, it is better to start with a more complete example,
# e.g. examples/tracing_c.

# If $VERILATOR_ROOT isn't in the environment, we assume it is part of a
# package inatall, and verilator is in your path. Otherwise find the
# binary relative to $VERILATOR_ROOT (such as when inside the git sources).

	#perf stat -e L1-icache-misses,L1-icache-loads,instructions,l2_cache_req_stat.ic_fill_miss,ic_cache_fill_l2  obj_dir/V$(TOP)
export VERILATOR_ROOT =  /localhome/jconnolly/verilator
VERILATOR = $(VERILATOR_ROOT)/bin/verilator

orig:
	@echo "-- VERILATING --"
	$(VERILATOR) $(VERILATOR_OPTS) --exe $(TOP).sv $(TB)
	@echo "-- COMPILING --"
	$(MAKE) -j 4 -C obj_dir -f V$(TOP).mk
	@echo "-- RUNNING --"
	time obj_dir/V$(TOP)
	@echo "-- DONE --------------------"



modified:
	@echo "-- VERILATING --"
	$(VERILATOR) $(VERILATOR_OPTS) --Mdir mod_dir --exe $(TOP).sv $(TB)
	python3 modify_outputs.py
	@echo "-- COMPILING --"
	$(MAKE) -j 4 -C mod_dir -f V$(TOP).mk
	@echo "-- RUNNING --"
	perf stat -e L1-icache-misses,L1-icache-loads,instructions,l2_cache_req_stat.ic_fill_miss,ic_cache_fill_l2  mod_dir/V$(TOP)
	@echo "-- DONE --"




######################################################################

maintainer-copy::
clean mostlyclean distclean maintainer-clean::
	-rm -rf obj_dir *.log *.dmp *.vpd core
