## w-boson-mass-analysis
The study recreates the core analysis method of the UA1 experiment, which earned 1984 Nobel Prize in Physics. With the simulation and analysis; W boson is observed, and its mass is determined.

*Since this analysis is based on parton-level Monte Carlo simulations, detector effects are excluded.*
### Simulation
Generated 50.000 events of p p → μ⁺ νμ using MadGraph5.

(In the process, intermediate particle is the W boson.)
### Analysis
While in processes such as Z → μ⁺ μ⁻, invariant mass can be calculated easily, (for further info, visit my other repo. 'muon-sm-llp-analysis') in current process, since the neutrino leaves no trace in the detector, pz of the neutrino is unknown. Therefore, the classical invariant mass formula cannot be used.

Instead the transverse mass mT is calculated, which cancels out pz in the formula.

$$
M_T^2 = 2|\boldsymbol{p}_T(μ)||\boldsymbol{ν}_T(2)|(1 - \cos\phi_{μν}) \, ,
$$
