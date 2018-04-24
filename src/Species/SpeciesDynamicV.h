#ifndef SPECIESDYNAMICV_H
#define SPECIESDYNAMICV_H

#include <vector>
#include <string>

#include "Species.h"

class ElectroMagn;
class Pusher;
class Interpolator;
class Projector;
class PartBoundCond;
class PartWalls;
class Field3D;
class Patch;
class SimWindow;


//! class Species
class SpeciesDynamicV : public Species
{
 public:
    //! Species creator
    SpeciesDynamicV(Params&, Patch*);
    //! Species destructor
    virtual ~SpeciesDynamicV();

    void initCluster(Params& params) override;

    void resizeCluster(Params& params) override;

//virtual void dynamics(double time, unsigned int ispec, ElectroMagn* EMfields, Interpolator* interp,
//                      Projector* proj, Params &params, bool diag_flag,
//                      PartWalls* partWalls, Patch* patch, SmileiMPI* smpi) override;
//

    //! Method calculating the Particle dynamics (interpolation, pusher, projection)
    void dynamics(double time, unsigned int ispec,
                          ElectroMagn* EMfields,
                          Params &params, bool diag_flag,
                          PartWalls* partWalls, Patch* patch, SmileiMPI* smpi,
                          RadiationTables &RadiationTables,
                          MultiphotonBreitWheelerTables & MultiphotonBreitWheelerTables,
                          std::vector<Diagnostic*>& localDiags) override;

    //! Method calculating the Particle charge on the grid (projection)
    void computeCharge(unsigned int ispec, ElectroMagn* EMfields) override;

    //! Method used to sort particles
    void sort_part(Params& params) override;

    //! This function reconfigures the species according to the vectorization mode
    void reconfiguration( Params& params, Patch * patch) override;

    //! Compute cell_keys for all particles of the current species
    void compute_part_cell_keys(Params &params);

    //! Compute cell_keys for the specified bin boundaries.
    void compute_bin_cell_keys(Params &params, int istart, int iend);

    //! Create a new entry for a particle
    void add_space_for_a_particle() override {
        particles->cell_keys.push_back(-1);
    }

    //! Method to import particles in this species while conserving the sorting among bins
    void importParticles( Params&, Patch*, Particles&, std::vector<Diagnostic*>& )override;

private:

    // Metrics for the dynamic vectorization
    int max_number_of_particles_per_cells;
    int min_number_of_particles_per_cells;
    double ratio_number_of_vecto_cells;

};

#endif
