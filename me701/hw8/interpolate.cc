#include <cmath>
#include <math.h>
#include "interpolate.hh"

// double interpolate(double x_new, double *x, double *y, int n, int order);

double interpolate(double x_new, double *x, double *y, int n, int order)
{
    int l=0;
    int ind[order+1];
    int i=0;
    int j=0;
    int s=0;
    int p=1;
    
    // find points directly to left of x_new
    for(i=0; i<n; i++)
    {
        if(x_new >= x[i])
        {
            l = i;
            break;
        }
    }
    
    // populate interpolation points
    for(j=l; j-l<order+1; j++)
    {
        ind[j-l] = j-((order+1)/2);
    }
    
    // shift interpolation points into existence if negative
    if(ind[0] < 0)
    {
        for(i=0; i<=order; i++)
        {
            ind[i] += 0 - ind[0];
        }
    }
    
    // shift interpolation points into existence if higher than n
    if(ind[order] > n-1)
    {
        for(i=0; i<=order; i++)
        {
            ind[i] += (n - 1) - ind[order];
        }
    }
    
    // calculate Lagrange polynomials
    for(i=0; i<=order; i++)
    {
        for(j=0; j<=order; j++)
        {
            if(j!=i)
            {
                p *= ((x_new - x[ind[j]]) / (x[ind[i]] - x[ind[j]]));
            }
        }
        s += (p * y[ind[i]]);
        p = 1;
    }
    return s;
}

