## Demonstration of Project Design and Diagramming

### Monte Carlo Radiation Transport

# First Pass

It is often valuable to sketch the overall problem first with a relatively
coarse granularity, covering the majority of what needs to happen.

* Define domain & source
* Loop over many histories
  * Sample source characteristics
  * Repeat until history is terminated
    * Sample distance to nuclear interaction
    * Calculate distance to boundary
    * Determine if next event is interaction or boundary crossing
      * For boundary crossing - record which boundary
      * For interaction - update direction & energy
      * Update position
    * Check for termination conditions

Once confident in this first pass, the next step is to [refine](refinement.md).
