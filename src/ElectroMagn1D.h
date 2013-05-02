#ifndef ELECTROMAGN1D_H
#define ELECTROMAGN1D_H

#include "ElectroMagn.h"


class PicParams;

//! class ElectroMagn1D containing all information on the electromagnetic fields & currents for 1d3v simulations
class ElectroMagn1D : public ElectroMagn
{
    
public:
    //! Constructor for ElectroMagn1D
	ElectroMagn1D(PicParams* params);
    
    //! Destructor for ElectroMagn1D
	~ElectroMagn1D();
		
    //! Method used for initializing Maxwell solver
	void solvePoisson();
    
    //! Method used to calculate the longitudinal current using the time-variation of the total charge density
	void chargeConserving();
    
    //! Method used to initialize the total charge densities and currents
    void initRhoJ();
    
    //! Method used to solve Maxwell's equations
	void solveMaxwell(double time_dual, double dt);
	
    //! Constant used for the Silver-Mueller boundary conditions
	double A_;
	
    //! Constant used for the Silver-Mueller boundary conditions
	double B_;
	
    //! Constant used for the Silver-Mueller boundary conditions
	double C_;
	
    //! \todo Create properties the laser time-profile (MG & TV)

    //! Number of nodes on the primal grid
    unsigned int nx_p;
    
    //! Number of nodes on the dual grid
    unsigned int nx_d;
    
    //! Spatial step dx for 1d3v cartesian simulations
    double dx;
    
    //! Ratio of the time-step by the spatial-step dt/dx for 1d3v cartesian simulations
    double dt_ov_dx;
    
    //! Ratio of the spatial-step by the time-step dx/dt for 1d3v cartesian simulations
    double dx_ov_dt;
    
private:
};

#endif
