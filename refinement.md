## Demonstration of Project Design and Diagramming

### Monte Carlo Radiation Transport

# Initial Refinement

From the [first pass](first-pass.md) diagram, it is useful to refine it and
add detail at each layer.  Refinement of this diagram is often best
accomplished in a nearly "depth-first" approach.  Take block from the coarse
diagram and define all the blocks necessary to achieve that block, and then
one of those blocks can be refined, and so on.

Let's begin refining the "Sample source characteristics" block in the coarse
diagram:

* Sample source characteristics
  * Sample position
  * Sample direction
  * Sample energy

Here we see a first opportunity to confront/define the desired scope and
complexity of our software project.  In general, a source can have a complex
description in a space-velocity phase space. Since there are many ways to
describe the possible position, direction and energy, it is useful to consider
the [scope/complexity and how that might progress in the future](scope.md).
