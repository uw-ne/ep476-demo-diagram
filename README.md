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

## Requirements

This software is required to stochastically estimate the radiation flux in
different regions of a 3-D domain.  Each region will be defined by
constructive solid geometry using only intersections of half-spaces defined by
analytical surfaces.  Each region may have a different material, as
represented by interaction parameters such as macroscopic cross-sections or
annenuation coefficients.  The user will be able to define the domain and
source characteristics, as well as how many individual histories should be
used.

## Scope and Complexity

The first milestone for this project is to implement the basic functionality
with reduced complexity.  In particular:

1. The source will be a mono-energetic point source emitted
   isotropically. This simplifies the amount of input required to formulate a
   problem, and reduces the breadth of random sampling capability needed for a
   first version.  Future versions will allow the source to be distributed in
   space, have non-isotropic emission directions, and support a variety of
   ways to specify energy distributions.
1. The interactions will be limited to isotropic scattering without energy
   loss. The simulation will all occur at a single energy, representing a
   1-group approach.  This simplifies the treatment of interaction physics in
   the initial version, and eliminates the need for complex interaction
   physics data.  Future versions might allow for simple models of energy loss
   (e.g. from elastic collisions) or read data tables that capture more
   detailed physics.

## Data Models

In the process of diagramming the software and defining the interfaces of
specific functions, some data models were defined.

- particle_state : a dictionary with keys that correspond to information about
  the particle such as:
   - 'position' : (1x3 numpy array) coordinates of the particle's current position
   - 'direction' : (1x3 numpy array) the unit vector for the particles current direction
   - 'energy' : (float) current energy of the particle
   - 'cell' : (string) name of current region in which particle is traveling

## Software Diagram

Making progress on a software project is easier when the project has been
decomposed into a set of small components with well-defined interfaces.  A
software diagram is an extremely useful tool for achieving this decomposition.
A software diagram can take many forms, from a block diagram in a visual
software package to a text-based outline.  The latter is most effective for a
markdown file such as this.

* Define domain & source
* ([#5]) Loop over many histories
  * (#4) Sample source characteristics
    * Sample position
      * assign fixed point source position (for now)
    * Sample direction
      * (#3) sample an angle from an isotropic distribution in 4*pi (for now)
    * Sample energy
      * assign fixed energy (for now)
  * Repeat until history is terminated
    * (#7) Look up mean free path for current material and particle energy
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
    * (#6) Check for termination conditions

This detailed version emerged from a few rounds of less detailed diagramming:

* [First Pass](first-pass.md)
* [Initial Refinement](refinement.md)
* [Scope and Progression](scope.md)
* [Additional Refinement](additional.md)
