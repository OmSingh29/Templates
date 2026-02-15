import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import cv2
image=img.imread(r"C:\Users\Om Singh\OneDrive\Pictures\IMG-20230911-WA0001.jpg")
print(image.shape)

r=image[:,:,0]
g=image[:,:,1]
b=image[:,:,2]
x=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
y=x.T
f1=cv2.filter2D(image,-1,x)
f2=cv2.filter2D(image,-1,y)

f,ax=plt.subplots(1,2,figsize=(100,100))
ax[0].imshow(f1,cmap='gray')
ax[0].set_title('Horizontal edge')
ax[1].imshow(f2,cmap='gray')
ax[1].set_title('Vertical edge')
plt.show()
