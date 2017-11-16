SWIG_INCLUDES=-I/home/john/opt/miniconda3/include/python3.6m


swig:
	swig -python -c++ interpolate.i
	g++ -fPIC -c interpolate.cc interpolate_wrap.cxx ${SWIG_INCLUDES}
	g++ -shared interpolate.o interpolate_wrap.o ${SWIG_INCLUDES} -o _interpolate.so


# Remove objects, module files, and exectables
clean:
	@rm -f *.o *.mod *-x *wrap.cxx *.so *.pyc

# Same, but leave the shared objects
neat:
	@rm -f *.o *.mod *-x *wrap.cxx *.pyc

#===============================================================================
# Rules
#===============================================================================

.SUFFIXES: .f90 .o
.PHONY: clean neat

%.o: %.f90
	$(F90) $(F90FLAGS) $(INCLUDE) -c $<
