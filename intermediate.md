## Demonstration of Project Design and Diagramming

### Monte Carlo Radiation Transport

# Intermediate diagram

This diagram shows an expansion of the [first pass](first-pass.md) diagram
after [refining](refinement.md) only the tasks related to sampling the source,
with considerations for the current
[scope and progression of scope](scope.md).

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
    * Sample distance to nuclear interaction
    * Calculate distance to boundary
    * Determine if next event is interaction or boundary crossing
      * For boundary crossing - record which boundary
      * For interaction - update direction & energy
      * Update position
    * Check for termination conditions

[Additional rounds of refinement and scope consideration](additional.md)x are
necessary to complete the detailed diagram.


