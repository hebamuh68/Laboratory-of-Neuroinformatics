#!/usr/bin/env python
# encoding: utf-8
import matplotlib.pyplot as plt
from load_data import data, mice, phases
import pandas as pd

# List of Mice and phases in experiment
Mice = list(mice)
Phases = [ph for ph in phases.sections()]

# Problem 1 ==============================================================
# Creating a panda dataframe for the result
Problem1 = pd.DataFrame(columns=['MouseID',
                                 'R1-P1D', 'R1-P1L', 'R1-P2D', 'R1-P2L', 'R1-P3D', 'R1-P3L',
                                 'R2-P1D', 'R2-P1L', 'R2-P2D', 'R2-P2L', 'R2-P3D', 'R2-P3L',
                                 'R3-P1D', 'R3-P1L', 'R3-P2D', 'R3-P2L', 'R3-P3D', 'R3-P3L',
                                 'R4-P1D', 'R4-P1L', 'R4-P2D', 'R4-P2L', 'R4-P3D', 'R4-P3L'])
for mouse in Mice:

    # creating raw to store all data corresponding to each mouse
    raw = [mouse]
    R1 = [0, 0, 0, 0, 0, 0]
    R2 = [0, 0, 0, 0, 0, 0]
    R3 = [0, 0, 0, 0, 0, 0]
    R4 = [0, 0, 0, 0, 0, 0]

    for phase in Phases:
        data.unmask_data()
        data.mask_data(*phases.gettime(phase))
        # Because of masking only visits starting in the given phase are returned.
        start_times = data.getstarttimes(mouse)
        end_times = data.getendtimes(mouse)
        room_numbers = data.getaddresses(mouse)

        for st, en, room in zip(start_times, end_times, room_numbers):
            if room == 1:
                R1[Phases.index(phase)] += (en - st)
            elif room == 2:
                R2[Phases.index(phase)] += (en - st)
            elif room == 3:
                R3[Phases.index(phase)] += (en - st)
            elif room == 4:
                R4[Phases.index(phase)] += (en - st)
            else:
                print("The room provided out of the ones considered in this experiment")

    # add the mouse data to the dataframe
    raw += R1 + R2 + R3 + R4
    Problem1.loc[len(Problem1.index)] = raw

# Problem 2 ==============================================================
raw = ["Total"]

# sum all time for pair of mice spent in each room for each phase
for col in Problem1.columns[1:]:
    raw.append(sum(Problem1[col]))

Problem1.loc[len(Problem1.index)] = raw

# Problem 3 ==============================================================
# Add description to the csv clarifying the header info
Problem1.loc[len(Problem1.index), 'MouseID'] = "R(Room)1-P(Phase)1(Dark)D/(Light)L"
# convert the dataframe to csv file
Problem1.to_csv('Problem1.csv', index=False)

# Visualization ==============================================================
plt.figure(figsize=(10, 16))

# Plotting a stacked bar chart
Problem1.set_index('MouseID')[:-2].T.plot(kind='bar', stacked=True)

plt.title('Time Spent in Each Room for Each Phase')
plt.xlabel('Room and Phase')
plt.ylabel('Time (in seconds)')
plt.legend(title='Mouse ID', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('visualization.png', dpi=300)

# Show the plot (optional)
plt.show()