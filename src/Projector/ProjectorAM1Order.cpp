#include "ProjectorAM1Order.h"

#include <cmath>
#include <iostream>
#include <complex>
#include "dcomplex.h"
#include "ElectroMagnAM.h"
#include "cField2D.h"
#include "Particles.h"
#include "Tools.h"
#include "Patch.h"
#include "PatchAM.h"

using namespace std;


// ---------------------------------------------------------------------------------------------------------------------
// Constructor for ProjectorAM1Order
// ---------------------------------------------------------------------------------------------------------------------
ProjectorAM1Order::ProjectorAM1Order( Params &params, Patch *patch ) : ProjectorAM( params, patch )
{
    dt = params.timestep;
    dr = params.cell_length[1];
    dl_inv_   = 1.0/params.cell_length[0];
    dl_ov_dt  = params.cell_length[0] / params.timestep;
    dr_ov_dt  = params.cell_length[1] / params.timestep;
    dr_inv_   = 1.0 / dr;
    one_ov_dt  = 1.0 / params.timestep;
    Nmode=params.nmodes;
    i_domain_begin = patch->getCellStartingGlobalIndex( 0 );
    j_domain_begin = patch->getCellStartingGlobalIndex( 1 );

    oversizeR = params.oversize[1]; 
    nprimr = params.n_space[1] + 2*params.oversize[1] + 1;
    npriml = params.n_space[0] + 2*params.oversize[0] + 1;

    invR = &((static_cast<PatchAM *>( patch )->invR)[0]);
    invRd = &((static_cast<PatchAM *>( patch )->invRd)[0]);
}


// ---------------------------------------------------------------------------------------------------------------------
// Destructor for ProjectorAM1Order
// ---------------------------------------------------------------------------------------------------------------------
ProjectorAM1Order::~ProjectorAM1Order()
{
}

// ---------------------------------------------------------------------------------------------------------------------
//! Non charge conserving projector for diags, frozen species or spectral solver - mode >= 0
// ---------------------------------------------------------------------------------------------------------------------
void ProjectorAM1Order::basicForComplex( complex<double> *rhoj, Particles &particles, unsigned int ipart, unsigned int type, int imode )
{
    // -------------------------------------
    // Variable declaration & initialization
    // -------------------------------------
    
    int iloc, nr( nprimr );
    double charge_weight = inv_cell_volume * ( double )( particles.charge( ipart ) )*particles.weight( ipart );
    double r = sqrt( particles.position( 1, ipart )*particles.position( 1, ipart )+particles.position( 2, ipart )*particles.position( 2, ipart ) );
    
    if( type > 0 ) { //if current density
        charge_weight *= 1./sqrt( 1.0 + particles.momentum( 0, ipart )*particles.momentum( 0, ipart )
                                  + particles.momentum( 1, ipart )*particles.momentum( 1, ipart )
                                  + particles.momentum( 2, ipart )*particles.momentum( 2, ipart ) );
        if( type == 1 ) { //if Jl
            charge_weight *= particles.momentum( 0, ipart );
        } else if( type == 2 ) { //if Jr
            charge_weight *= ( particles.momentum( 1, ipart )*particles.position( 1, ipart ) + particles.momentum( 2, ipart )*particles.position( 2, ipart ) ) / r ;
            nr++;
        } else { //if Jt
            charge_weight *= ( -particles.momentum( 1, ipart )*particles.position( 2, ipart ) + particles.momentum( 2, ipart )*particles.position( 1, ipart ) ) / r ;
        }
    }
    
    complex<double> e_theta = ( particles.position( 1, ipart ) + Icpx*particles.position( 2, ipart ) )/r;
    complex<double> C_m = 1.;
    if( imode > 0 ) {
        C_m = 2.;
    }
    for( unsigned int i=0; i<( unsigned int )imode; i++ ) {
        C_m *= e_theta;
    }
    
    double xpn, rpn;
    double delta;
    double Sl1[2], Sr1[2];
    
    
    // locate the particle on the primal and dual grid at current time-step & calculate coeff. S1
    xpn = particles.position( 0, ipart ) * dl_inv_;
    int ip = round( xpn + 0.5 * ( type==1 ) );
    delta  = xpn - ( double )ip;
    Sl1[0] = delta ;
    Sl1[1] = 1.-delta;
    rpn = r * dr_inv_ ;
    int jp = round( rpn + 0.5*( type==2 ) );
    delta  = rpn - ( double )jp;
    Sr1[0] = delta;
    Sr1[1] = 1.-delta;
    
    ip -= i_domain_begin ;
    jp -= j_domain_begin ;
    
    if( type != 2 ) {
        for( unsigned int i=0 ; i<2 ; i++ ) {
            iloc = ( i+ip )*nr+jp;
            for( unsigned int j=0 ; j<2 ; j++ ) {
                rhoj [iloc+j] += C_m*charge_weight* Sl1[i]*Sr1[j] * invR[j+jp];
            }
        }//i
    } else {
        for( unsigned int i=0 ; i<2 ; i++ ) {
            iloc = ( i+ip )*nr+jp;
            for( unsigned int j=0 ; j<2 ; j++ ) {
                rhoj [iloc+j] += C_m*charge_weight* Sl1[i]*Sr1[j] * invRd[j+jp];
            }
        }//i
    }
} // END Project for diags local current densities

// ---------------------------------------------------------------------------------------------------------------------
//! Project local currents for all modes, not charge conserving
// ---------------------------------------------------------------------------------------------------------------------
void ProjectorAM1Order::currents( ElectroMagnAM *emAM, Particles &particles, unsigned int ipart, double invgf, bool diag_flag, int ispec)
{

    // -------------------------------------
    // Variable declaration & initialization
    // -------------------------------------
    int iloc, jloc, linindex;
    // (x,y,z) components of the current density for the macro-particle
    double charge_weight = inv_cell_volume * ( double )( particles.charge( ipart ) )*particles.weight( ipart );
    
    // variable declaration
    double xpn, ypn;
    double delta;
    complex<double>  Jl_p[2][2], Jr_p[2][2], Jt_p[2][2];

    double  Sl1[2], Sr1[2],Sl1d[2], Sr1d[2];
    complex<double> e_theta, C_m = 1.; 
    complex<double> *Jl, *Jr, *Jt, *rho;
    
    double yp = particles.position( 1, ipart );
    double zp = particles.position( 2, ipart );
    double rp = sqrt( particles.position( 1, ipart )*particles.position( 1, ipart )+particles.position( 2, ipart )*particles.position( 2, ipart ) );
    double crt_p = charge_weight * ( particles.momentum( 2, ipart )*particles.position( 1, ipart )-particles.momentum( 1, ipart )*particles.position( 2, ipart ) )/( rp )*invgf;
    double crl_p = charge_weight * ( particles.momentum( 0, ipart )) *invgf;
    double crr_p = charge_weight * ( particles.momentum( 1, ipart )*particles.position( 1, ipart ) + particles.momentum( 2, ipart )*particles.position( 2, ipart ))/rp*invgf;
    e_theta = ( particles.position( 1, ipart ) + Icpx*particles.position( 2, ipart ) )/rp;
    // locate the particle on the primal and dual grid at current time-step & calculate coeff. S1
    xpn = particles.position( 0, ipart ) * dl_inv_;
    int ip = round( xpn );
    int ipd = round( xpn + 0.5 );
    delta  = xpn - ( double )ip;
    Sl1[0] = delta;
    Sl1[1] = 1.-delta;
    delta  = xpn - ( double )ipd;
    Sl1d[0] = delta;
    Sl1d[1] = 1.-delta;
    
    ypn = rp *dr_inv_ ;
    int jp = round( ypn );
    int jpd = round( ypn +0.5 );
    delta  = ypn - ( double )jp;
    Sr1[0] = delta;
    Sr1[1] = 1.-delta;
    delta  = ypn - ( double )jpd;
    Sr1d[0] = delta;
    Sr1d[1] = 1.-delta;

    double *invR_local  = &(invR[jp]);
    double *invRd_local = &(invRd[jpd]);

    ip  -= i_domain_begin ;
    ipd -= i_domain_begin ;
    jp  -= j_domain_begin ;
    jpd -= j_domain_begin ;
    for( unsigned int imode=0; imode<( unsigned int )Nmode; imode++ ) {
        if( imode == 1 ) {
            C_m = 2.;
        }
        if( imode > 0 ) {
            C_m *= e_theta;
        }
        
        if (!diag_flag){
            Jl =  &( *emAM->Jl_[imode] )( 0 );
            Jr =  &( *emAM->Jr_[imode] )( 0 );
            Jt =  &( *emAM->Jt_[imode] )( 0 );
        } else {
            unsigned int n_species = emAM->Jl_.size() / Nmode;
            unsigned int ifield = imode*n_species+ispec;
            Jl  = emAM->Jl_s    [ifield] ? &( * ( emAM->Jl_s    [ifield] ) )( 0 ) : &( *emAM->Jl_    [imode] )( 0 ) ;
            Jr  = emAM->Jr_s    [ifield] ? &( * ( emAM->Jr_s    [ifield] ) )( 0 ) : &( *emAM->Jr_    [imode] )( 0 ) ;
            Jt  = emAM->Jt_s    [ifield] ? &( * ( emAM->Jt_s    [ifield] ) )( 0 ) : &( *emAM->Jt_    [imode] )( 0 ) ;
            rho = emAM->rho_AM_s[ifield] ? &( * ( emAM->rho_AM_s[ifield] ) )( 0 ) : &( *emAM->rho_AM_[imode] )( 0 ) ;

            for( unsigned int i=0 ; i<2 ; i++ ) {
                iloc = ( i+ip )*nprimr;
                for( unsigned int j=0 ; j<2 ; j++ ) {
                    jloc = j+jp;
                    linindex = iloc+jloc;
                    rho [linindex] += C_m*charge_weight* Sl1[i]*Sr1[j]*invR_local[j];
                }
            }//i
        }
        
        // Jl^(d,p)
        for( unsigned int i=0 ; i<2 ; i++ ) {
            iloc = ( i+ipd )*nprimr+jp;
            for( unsigned int j=0 ; j<2 ; j++ ) {
                linindex = iloc+j;
                Jl [linindex] += C_m * crl_p* Sl1d[i]*Sr1[j]*invR_local[j] ;
            }
        }//i
        // Jr^(p,d)
        for( unsigned int i=0 ; i<2 ; i++ ) {
            iloc = ( i+ip )*( nprimr+1 )+jpd;
            for( unsigned int j=0 ; j<2 ; j++ ) {
                linindex = iloc+j;
                Jr [linindex] += C_m * crr_p* Sl1[i]*Sr1d[j]*invRd_local[j] ;
            }
        }//i
        // Jt^(p,p)
        for( unsigned int i=0 ; i<2 ; i++ ) {
            iloc = ( i+ip )*nprimr + jp;
            for( unsigned int j=0 ; j<2 ; j++ ) {
                linindex = iloc+j;
                Jr [linindex] += C_m * crr_p* Sl1[i]*Sr1[j]*invR_local[j] ;
            }
        }
    }// end loop on modes
    
} // END Project local current densities (Jl, Jr, Jt)

//------------------------------------//
//Wrapper for projection
void ProjectorAM1Order::currentsAndDensityWrapper( ElectroMagn *EMfields, Particles &particles, SmileiMPI *smpi, int istart, int iend, int ithread, bool diag_flag, bool is_spectral, int ispec, int icell, int ipart_ref )
{
    if( is_spectral ) {
        ERROR( "Not implemented" );
    }
    
    std::vector<double> *invgf = &( smpi->dynamics_invgf[ithread] );
    
    ElectroMagnAM *emAM = static_cast<ElectroMagnAM *>( EMfields );

    for( int ipart=istart ; ipart<iend; ipart++ ) {
        currents( emAM, particles,  ipart, ( *invgf )[ipart], diag_flag, ispec);
    }

    //Boundary conditions for currents on axis
    if (invR[0] < 0. ) {
        double sign = -1. ;
        unsigned int n_species = emAM->Jl_.size() / Nmode;
        for ( int imode = 0; imode < Nmode; imode++){
            unsigned int ifield = imode*n_species+ispec;
            complex<double> *Jl  = emAM->Jl_s    [ifield] ? &( * ( emAM->Jl_s    [ifield] ) )( 0 ) : &( *emAM->Jl_    [imode] )( 0 ) ;
            complex<double> *Jr  = emAM->Jr_s    [ifield] ? &( * ( emAM->Jr_s    [ifield] ) )( 0 ) : &( *emAM->Jr_    [imode] )( 0 ) ;
            complex<double> *Jt  = emAM->Jt_s    [ifield] ? &( * ( emAM->Jt_s    [ifield] ) )( 0 ) : &( *emAM->Jt_    [imode] )( 0 ) ;
            complex<double> *rho = emAM->rho_AM_s[ifield] ? &( * ( emAM->rho_AM_s[ifield] ) )( 0 ) : &( *emAM->rho_AM_[imode] )( 0 ) ;
            sign *= -1.;

            // Fold primal quantities along r
            for( unsigned int i=0 ; i<npriml; i++ ) {
                int iloc = i*nprimr;
                for( unsigned int j=1 ; j<= oversizeR; j++ ) {
                    Jt [iloc+oversizeR+j] +=  sign * Jt [iloc+oversizeR-j];
                    Jt [iloc+oversizeR-j] = 0.; 
                    Jl [iloc+oversizeR+j] +=  sign * Jl [iloc+oversizeR-j];
                    Jl [iloc+oversizeR-j] = 0.; 
                    rho[iloc+oversizeR+j] +=  sign * rho[iloc+oversizeR-j];
                    rho[iloc+oversizeR-j] = 0.; 
                }
            }//i
            // Fold dual quantities along r
            int max_fold = 2*oversizeR+1;
            for( unsigned int i=0 ; i<npriml; i++ ) {
                int iloc = i*(nprimr+1);
                for( unsigned int j=0 ; j<= oversizeR; j++ ) {
                    Jr [iloc+max_fold-j] += sign * Jr [iloc+j];
                    Jr [iloc+j] = 0.; 
                }
            }//i


            // Jl and Jt on axis (primal)

            int j = oversizeR; //axis position
            if (imode > 0){
                // All Jl = zero on axis for imode > 0. Mode 0 is treated in general case.
                for( unsigned int i=0 ; i<npriml; i++ ) {
                    int iloc = i*nprimr;
                    Jl [iloc+j] = 0. ;
                    rho[iloc+j] = 0. ;
                }//i
            }
            if (imode == 1){
                for( unsigned int i=0 ; i<npriml; i++ ) {
                    int iloc = i*nprimr;
                    int ilocr = i*(nprimr+1);
                    Jt [iloc+j] = -1./3.*(4.*Icpx*Jr[ilocr+j+1] + Jt[iloc+j+1]) ;
                }//i
            } else{
                for( unsigned int i=0 ; i<npriml; i++ ) {
                    int iloc = i*nprimr;
                    Jt [iloc+j] = 0. ;
                }
            }
        }

    }
}
