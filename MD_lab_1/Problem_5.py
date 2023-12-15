import numpy as np 
from PIL import Image 
  
total = int(input("Give the depth(preferable smaller then 5):"))
  
size = 3**total 
  
square = np.empty([size, size, 3], dtype = np.uint8) 
color = np.array([255, 255, 255], dtype = np.uint8) 

square.fill(0) 
  
for i in range(0, total + 1): 
    stepdown = 3**(total - i) 
    for x in range(0, 3**i): 
        if x % 3 == 1: 
            for y in range(0, 3**i): 
                if y % 3 == 1: 
                    square[y * stepdown:(y + 1)*stepdown, x * stepdown:(x + 1)*stepdown] = color 
save_file = "sierpinski_carpet.jpg"
Image.fromarray(square).save(save_file) 

i = Image.open("sierpinski_carpet.jpg")
i.show() 