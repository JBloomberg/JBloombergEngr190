from PIL import  Image,ImageDraw

img = Image.new('RGB',(100,100),'white')
draw = ImageDraw.Draw(img)

aboveLine = [0] * 100
aboveLine[int(len(aboveLine)//2)] = 1
print(aboveLine)

# Create a checkboard first line
for j in range(1,50) :
    newLine = [0] * 100
    
    for i in range(1,50) : # 3 Numbers in next line deterime direction
        if (aboveLine[i-1] == 0) and (aboveLine[i] == 0) and (aboveLine[i+1] == 1) :
            # Draw Black
            draw.point((i,j), fill='black')
            newLine[i] = 1
        else :
            #draw white
            draw.point((i,j), fill='white')
            newLine[i] = 0



    

    
    for i in range(50,99) : # 3 Numbers in next line deterime direction
        if (aboveLine[i-1] == 1) and (aboveLine[i] == 0) and (aboveLine[i+1] == 0) :
            # Draw Black
            draw.point((i,j), fill='black')
            newLine[i] = 1
        else :
            #draw white
            draw.point((i,j), fill='white')
            newLine[i] = 0


    aboveLine = newLine



img.show()