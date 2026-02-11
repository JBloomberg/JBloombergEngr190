from PIL import  Image,ImageDraw

img = Image.new('RGB',(100,100),'white')
draw = ImageDraw.Draw(img)

aboveLine = [0] * 100
aboveLine[int(len(aboveLine)/2)] = 1

print(aboveLine)

# Create a checkboard first line
for j in range(100) :
    newLine = [0] * 100
    for i in range(1,99) :
        
        if (aboveLine[i-1] == 1) and (aboveLine[i] == 1) and (aboveLine[i+1] == 1): #DIGIT 1
            # Draw Black
            draw.point((i,j), fill='black')
            newLine[i] = 1

        elif (aboveLine[i-1] == 1) and (aboveLine[i] == 1) and (aboveLine[i+1] == 0): #DIGIT 2
            #draw black
            draw.point((i,j), fill='black')
            newLine[i] = 1

        elif (aboveLine[i-1] == 1) and (aboveLine[i] == 0) and (aboveLine[i+1] == 1): #DIGIT 3
            # Draw Black
            draw.point((i,j), fill='black')
            newLine[i] = 1

        elif (aboveLine[i-1] == 1) and (aboveLine[i] == 0) and (aboveLine[i+1] == 0): #DIGIT 4
            #draw black
            draw.point((i,j), fill='black')
            newLine[i] = 1

        elif (aboveLine[i-1] == 0) and (aboveLine[i] == 1) and (aboveLine[i+1] == 1): #DIGIT 5
            # Draw Black
            draw.point((i,j), fill='black')
            newLine[i] = 1

        elif (aboveLine[i-1] == 0) and (aboveLine[i] == 1) and (aboveLine[i+1] == 0): #DIGIT 6
            #draw black
            draw.point((i,j), fill='white')
            newLine[i] = 0

        elif (aboveLine[i-1] == 0) and (aboveLine[i] == 0) and (aboveLine[i+1] == 1): #DIGIT 7
            # Draw Black
            draw.point((i,j), fill='black')
            newLine[i] = 1

        elif (aboveLine[i-1] == 0) and (aboveLine[i] == 0) and (aboveLine[i+1] == 0): #DIGIT 8
            #draw black
            draw.point((i,j), fill='white')
            newLine[i] = 0

        else :
           # draw white
           draw.point((i,j), fill='white')
           newLine[i] = 0
        
    aboveLine = newLine

img.show()
img.save('Automata.gif')