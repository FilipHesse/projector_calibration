import svgwrite

dwg = svgwrite.Drawing('checkerboard_A4.svg')

beginA4x=100
beginA4y=20

frame_width = 50
beginA4x=frame_width
beginA4y=frame_width

A4x=297
A4y=210


rows = 4
columns = 5

# draw a white box
dwg.add(dwg.rect(('0mm', '0mm'), (str((columns+2)*A4x+2*frame_width)+'mm', str((rows+2)*A4y+2*frame_width)+'mm'),
    fill='white')
)

for i in range(rows+2):
    for j in range(columns+2):
        if ((i % 2) == 0 and (j % 2) == 0) or ((i % 2) == 1 and (j % 2) == 1):
            dwg.add(dwg.rect((str(beginA4x+j*A4x)+'mm', str(beginA4y+i*A4y)+'mm'), (str(A4x)+'mm', str(A4y)+'mm'),
                fill='black')
            )


# write svg file to disk
dwg.save()

#h80w150
