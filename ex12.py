import math
from PIL import Image

evil = open('evil2.gfx','rb').read()

evil1 = open('evil1.jpg','wb')
evil2 = open('evil2.jpg','wb')
evil3 = open('evil3.jpg','wb')
evil4 = open('evil4.jpg','wb')
evil5 = open('evil5.jpg','wb')

for i in range(0,len(evil),5):
    evil1.write(evil[i])
    evil2.write(evil[i+1])
    evil3.write(evil[i+2])
    evil4.write(evil[i+3])
    evil5.write(evil[i+4])

evil1.close()
evil2.close()
evil3.close()
evil4.close()
evil5.close()
