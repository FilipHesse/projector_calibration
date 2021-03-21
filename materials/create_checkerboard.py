import svgwrite

dwg = svgwrite.Drawing('checkerboard_A4.svg')

beginA4x=100
beginA4y=20

frame_width = 30
beginA4x=60
beginA4y=frame_width

A4x=297
A4y=210

outer_rect=20

rows = 4
columns = 5

# draw a white box
height = (rows)*A4y+2*outer_rect+2*frame_width
width = (columns)*A4x+2*outer_rect+2*frame_width

dwg.add(dwg.rect(('0mm', '0mm'), (str(height/9*16)+'mm', str(height)+'mm'),
    fill='white')
)

for i in range(rows+2):
    for j in range(columns+2):
        if ((i % 2) == 0 and (j % 2) == 0) or ((i % 2) == 1 and (j % 2) == 1):
            if i==0 and j ==0:
                dwg.add(dwg.rect((str(beginA4x)+'mm', str(beginA4y)+'mm'), (str(outer_rect)+'mm', str(outer_rect)+'mm'),
                    fill='black')
                )
            elif i==0 and j==columns+1:
                dwg.add(dwg.rect((str(beginA4x+outer_rect+(j-1)*A4x)+'mm', str(beginA4y)+'mm'), (str(outer_rect)+'mm', str(outer_rect)+'mm'),
                    fill='black')
                )
            elif i==rows+1 and j==0:
                dwg.add(dwg.rect((str(beginA4x)+'mm', str(beginA4y+outer_rect+(i-1)*A4y)+'mm'), (str(outer_rect)+'mm', str(A4y)+'mm'),
                    fill='black')
                )
            elif i==0 and not j ==0:
                dwg.add(dwg.rect((str(beginA4x+outer_rect+(j-1)*A4x)+'mm', str(beginA4y)+'mm'), (str(A4x)+'mm', str(outer_rect)+'mm'),
                    fill='black')
                )

            elif not i==0 and j ==0:
                dwg.add(dwg.rect((str(beginA4x)+'mm', str(beginA4y+outer_rect+(i-1)*A4y)+'mm'), (str(outer_rect)+'mm', str(A4y)+'mm'),
                    fill='black')
                )

            elif i==rows+1 and j==columns+1:
                dwg.add(dwg.rect((str(beginA4x+outer_rect+(j-1)*A4x)+'mm', str(beginA4y+outer_rect+(i-1)*A4y)), (str(outer_rect)+'mm', str(outer_rect)+'mm'),
                    fill='black')
                )

            elif i==rows+1 and not j==columns+1:
                dwg.add(dwg.rect((str(beginA4x+outer_rect+(j-1)*A4x)+'mm', str(beginA4y+outer_rect+(i-1)*A4y)+'mm'), (str(A4x)+'mm', str(outer_rect)+'mm'),
                    fill='black')
                )

            elif not i==rows+1 and j==columns+1:
                dwg.add(dwg.rect((str(beginA4x+outer_rect+(j-1)*A4x)+'mm', str(beginA4y+outer_rect+(i-1)*A4y)+'mm'), (str(outer_rect)+'mm', str(A4y)+'mm'),
                    fill='black')
                )
            
            else:
                dwg.add(dwg.rect((str(beginA4x+outer_rect+(j-1)*A4x)+'mm', str(beginA4y+outer_rect+(i-1)*A4y)+'mm'), (str(A4x)+'mm', str(A4y)+'mm'),
                    fill='black')
            )


# write svg file to disk
dwg.save()

#h80w150
