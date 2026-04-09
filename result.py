import os 
import numpy as np
import matplotlib.pyplot as plt

time = []
open("output10000.txt","w").close()
for i in range(10000):
	os.system("/usr/bin/time -f '%e' ./multip 2>>output10000.txt")

with open("output.txt", "r", encoding="utf-8") as file:
	for line in file:
		valeur = line.strip()
		time.append(float(valeur))

Q1,Q2,Q3 = np.quantile(time, [0.25, 0.5, 0.75])
print(f"min: {np.min(time)}s")
print(f"Q1: {Q1}s")
print(f"Q2: {Q2}s")
print(f"Q3: {Q3}s")
print(f"max: {np.max(time)}s")
print(f"WCET: {np.max(time)*1.2}s")

plt.hist(time)
plt.xlabel("execution time (s)")
plt.ylabl("N")
plt.title("execution times for 10 000 multiplication command")
plt.show()
