import numpy as np
import re
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

ab = open('w_5_20.txt', 'r')
r1 = ab.read()
r1 = r1.replace('   ',',').replace(' ',',')
numbers = re.findall(r'\d+', r1)
numbers = np.array(numbers, dtype='float32')
numbers = np.asarray(numbers, dtype = np.uint8)
print(numbers)
print(len(numbers))
numbers = numbers[0:262144].reshape(512,512)
numbers = numbers[0:512,0:512]
print(numbers.dtype)
df = pd.DataFrame(numbers)
df.to_csv('sample.csv', index=False)

plt.imshow(numbers[0:512,0:512],cmap='gray')
plt.show()
img = Image.fromarray(numbers)
img.convert("L").save('vlena_result.png','png')