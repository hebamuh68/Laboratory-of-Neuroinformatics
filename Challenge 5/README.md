# Extracellular Stimulation of Neurons

## Overview

This set of experiments aims to explore the effects of extracellular stimulation on neurons using the LFPy and MEAutility libraries in Python. The experiments involve varying stimulation parameters to observe changes in the somatic potential and extracellular field.

## Experimental Setup

### Cell Parameters

The neuron is modeled using the following parameters:
- Morphology file: 'morphologies/L5_Mainen96_LFPy.hoc'
- Simulation time: -50 ms to 100 ms
- Time step: 2^-4 ms
- Initial membrane potential: -60 mV
- Active membrane properties included

### Instantiate Cell

A function `instantiate_cell` creates an LFPy.Cell object based on the specified parameters. The cell is positioned at (0, 0, 0) and rotated for proper orientation. Hodgkin-Huxley (hh) mechanisms are inserted into all sections, with adjusted channel density in non-soma sections.

### Plot Results

The function `plot_results` generates a 2x2 grid of plots:
1. Extracellular potential heatmap
2. Somatic voltage over time
3. Morphology plot with electrode positions

## Experiment 1: Hyperpolarization

1. Instantiate a neuron cell.
2. Create a Neuronexus-32 electrode probe and position it.
3. Apply a pulse stimulation current with positive amplitude (20,000 nA) for 2 pulses with a 10 ms interpulse interval.

## Experiment 2: Depolarization

1. Re-instantiate the neuron cell.
2. Use the same Neuronexus-32 electrode probe.
3. Apply a pulse stimulation current with negative amplitude (-20,000 nA) for 2 pulses with a 10 ms interpulse interval.

## Experiment 3: Action Potential Elicitation

1. Increase the stimulation current to a higher negative value (-75,000 nA) to elicit action potentials.
2. Plot the resulting somatic potential, extracellular field, and LFP.

## Experiment 4: Varied Pulse Width

1. Re-instantiate the neuron cell.
2. Apply a pulse stimulation current with negative amplitude (-30,000 nA) for 1 pulse with a longer pulse width (15 ms).
3. Plot the resulting somatic potential, extracellular field, and LFP.

## Conclusion

The experiments demonstrate the impact of extracellular stimulation on neuron behavior, showcasing hyperpolarization, depolarization, and action potential elicitation under different current amplitudes and pulse widths.
