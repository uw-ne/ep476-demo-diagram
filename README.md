## Demonstration of Project Design and Diagramming

# Monte Carlo Radiation Transport

## Introduction

This repository serves to demonstrate some artifacts of the design process for
a scientific software project.

The physics problem that is to be solved by this project is Monte Carlo
radiation transport, a stochastic approach to modeling radiation transport in
a domain.  A large number of individual particle histories are simulated, each
following a different path based on random sampling of the physical processes
encountered by each particle.  The mean behavior of those particles is
recorded to estimate the overall radiation fields.

## Software Diagram

Making progress on a software project is easier when the project has been
decomposed into a set of small components with well-defined interfaces.  A
software diagram is an extremely useful tool for achieving this decomposition.
A software diagram can take many forms, from a block diagram in a visual
software package to a text-based outline.  The latter is most effective for a
markdown file such as this.

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
    * Sample distance to nuclear interaction
      * Calculate distance in units of mean free path
    * Calculate distance to boundary
      * Initialize min(distance to surface)
      * Loop over bounding surfaces
        * Update min(distance to surface)
        * Store surface with min(distance to surface)
      * Convert min(distance to surface) to mean free paths
    * Determine if next event is interaction or boundary crossing
      * For boundary crossing - record which boundary
      * For interaction - update direction & energy
        * Sample an agle from isotropic distribution in 4*pi
        * Calculate a new energy from initial energy & direction and new direction
          * return initial energy (for now)
    * Update position
    * Record contributions to tallies
    * Check for termination conditions


This detailed version emerged from a few rounds of less detailed diagramming:

* [First Pass](first-pass.md)
* [Initial Refinement](refinement.md)
* [Scope and Progression](scope.md)



### Scope and Progression

Here we see a first opportunity to confront/define the desired scope and
complexity of our software project.  In general, a source can have a complex
description in a space-velocity phase space.  Options for defining the position of the source particles include:

* one or more point sources
* one or more line sources
* one or more area sources
* one or more volumetric sources
* a combination of the above

For anything other than a single point source, the relative intensity (or
intensity distribution) could be defined by a complex function.

It is generally wise to limit the scope and complexity as projects begin, with
a goal to add that complexity in the future.  This project will begin by only considering a single point source defined by a position in space.

Similar, the angular distribution of the radioactive emissions from this
source could be isotropic, mono-directional, or follow some function of
arbitrary complexity.  This project will begin by only considering isotropic
emission of particles from the point source.

Finally, the energy of the particle can be represented by different levels of
complexity.  The simplest is to assume a source born with a single precisely
defined energy, as opposed to a realistic distribution around a single
emission line or multiple emissions or even a continuum.  This project will begin with a single energy.

Having made these decisions on scope and complexity, a reasonable diagram of
the software that includes details on the source sampling could be:

