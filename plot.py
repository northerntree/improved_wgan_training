

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


pathway = '/home/cui/GAN/github/improved_wgan_training/output/balan_';
iteration = '8200_';
istr = '4.npy';
full_path = pathway + iteration + istr;
b = np.load(full_path);
x = b[:, 0];
y = b[:, 1];

plt.scatter(x, y);
plt.show();