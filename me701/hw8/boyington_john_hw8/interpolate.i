// The syntax is %module module_name, i.e., the name
// you want to import.  All of the C++ includes you need
// should be included here.
%module interpolate
%{
#include "interpolate.hh"
%}


// this stuff is boiler plate:
%{
#define SWIG_FILE_WITH_INIT
%}
%include "numpy.i"
%init %{
  import_array();
%}

// The following are examples of a SWIG "typemap".  This is an advanced
// feature that I've only ever tinkered with seriously for one project, but 
// I've **used** the labor of others liberally.

// This is what we want for input arrays that should not get changed
%apply (double* INPLACE_ARRAY1, int DIM1) {(double* x, int xx)}
%apply (double* INPLACE_ARRAY1, int DIM1) {(double* y, int yy)}

// INCLUDE THE HEADER FILE WITH THE ACTUAL DECLARATIONS
%include "interpolate.hh"
