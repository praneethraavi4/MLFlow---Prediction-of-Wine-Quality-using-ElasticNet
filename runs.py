import numpy as np
import os

alpha_s = np.linspace(0.1,1.0,5)
l1_ratio_s = np.linspace(0.1,1.0,5)


for alpha in alpha_s:
    for l1 in l1_ratio_s:
        os.system(f"python mlmodel.py -a {alpha} -l1 {l1}")
