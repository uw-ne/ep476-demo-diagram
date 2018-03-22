## Demonstration of Project Design and Diagramming

### Monte Carlo Radiation Transport

# Scope and Progression

Options for defining the position of the source particles include:

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
emission line or multiple emissions or even a continuum.  This project will
begin with a single energy.

Having made these decisions on scope and complexity, a reasonable diagram of
the software that includes details on the source sampling is considered an
[intermediate diagram](intermediate.md).
