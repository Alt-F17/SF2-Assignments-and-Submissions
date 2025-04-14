import pint
import pandas as pd
import matplotlib.pyplot as plt

ureg = pint.UnitRegistry()

velos = [
    -0.9584615384615366,
    -0.9573076923076911,
    -0.9773076923076914,
    -1.029999999999998,
    -1.032307692307691,
    -1.0242307692307686,
    -0.7988461538461535,
    -0.9584615384615379,
    -0.89076923076923,
    -0.9311538461538447,
]

term_velo = sum(velos) / len(velos) * ureg.m / ureg.s
area = (141.591 * ureg.cm ** 2).to(ureg.m ** 2)
mass = (8.8 * ureg.g / 10).to(ureg.kg)
density = 1.2006 * ureg.kg / (ureg.m ** 3)
drag_c = (2 * mass * 9.8) / (density * area * term_velo ** 2)
gravity = 9.8 * ureg.m / (ureg.s ** 2)

clean_df = pd.read_csv(r"sandbox\multi_data.csv")

run = 5
time = f"Time (s) Run #{run}"
position = f"Position (m) Run #{run}"
data = clean_df[[time, position]].dropna()

v = 0
t_values = [0]
y_values = [data[position].max()]

dt = 0.0001
while y_values[-1] > 0:
    a = -gravity.magnitude + (
        density.magnitude * drag_c.magnitude * area.magnitude * (v**2)
    ) / (2 * mass.magnitude * run)

    v = v + a * dt

    t_values.append(t_values[-1] + dt)
    y_values.append(y_values[-1] + v * dt)

plt.figure(figsize=(10, 5))

ax = plt.axes()
ax.plot(data[time], data[position], label=f"Run #{run}")
ax.plot(t_values, y_values, label="Simulation")

ax.set_xlabel("Time (s)")
ax.set_ylabel("Position (m)")
ax.legend()

plt.show()