## Demonstration of Project Design and Diagramming

### Monte Carlo Radiation Transport

# Additional Refinement and Scope Consideration

Additional rounds of refinement can lead to the following diagram, with important notes following.

* Define domain & source
* Loop over many histories
  * Sample source characteristics
    * Sample position
      * assign fixed point source position (for now)
    * Sample direction
      * sample an angle from an isotropic distribution in 4*pi (for now)
    * Sample energy
      * assign fixed energy (for now)
  * Repeat until history is terminated
    * Look up mean free path for current material and particle energy
    * Sample distance to nuclear interaction in mean free paths
    * Calculate distance to boundary
      * Initialize min(distance to surface)
      * Loop over bounding surfaces
        * Calculate distance to surface
        * Update min(distance to surface)
        * Store surface with min(distance to surface)
      * Convert min(distance to surface) to mean free paths
    * Determine if next event is interaction or boundary crossing
      * For boundary crossing - record which boundary
      * For interaction - update direction & energy
        * Sample an angle from isotropic distribution in 4*pi
        * Calculate a new energy from initial energy & direction and new direction
          * return initial energy (for now)
    * Update position
    * Record contributions to tallies
    * Check for termination conditions


Some important aspects of refinement:

1. It is possible/reasonable to add new blocks to the diagram even if it
   doesn't provide refinement - there may be something that is simply forgotten
   in a prior stage.  In this case, the block to "Look up the mean free
   path...." was absent from the previous version and has been added now.
   Similarly, the "Record contributions to tallies" block.

2. Some additional scope limitation has been introduced, specifically the
   choice of isotropic scattering with no loss of energy.  These can be
   relaxed in the future by implementing different ways to update the
   direction and energy of a collision.
