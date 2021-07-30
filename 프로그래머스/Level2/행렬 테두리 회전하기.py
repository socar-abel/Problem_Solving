def rotation(matrix, x1, y1, x2, y2):
    
    elements = []
    coordinates = []
    
    for y in range(y1,y2):
        elements.append(matrix[x1][y])
        coordinates.append((x1,y))
    for x in range(x1,x2):
        elements.append(matrix[x][y2])
        coordinates.append((x,y2))
    for y in reversed(range(y1+1,y2+1)):
        elements.append(matrix[x2][y])
        coordinates.append((x2,y))
    for x in reversed(range(x1+1,x2+1)):
        elements.append(matrix[x][y1])
        coordinates.append((x,y1))
    
    coordinates.append(coordinates[0])
    for i in range(len(elements)):
        nx, ny = coordinates[i+1][0], coordinates[i+1][1]
        matrix[nx][ny] = elements[i]    
        
    minValue = min(elements)
    #print('elements, minV',elements,minValue)
    #print('coordinates',coordinates)
    
    #print('변경된 matrix')
    #for x in range(len(matrix[0])):
        #print(matrix[x])
    
    
    return matrix, minValue


def solution(rows, columns, queries):
    answer = []
    matrix = [[] for _ in range(rows)]
    
    for x in range(rows):
        for y in range(columns):
            matrix[x].append(columns*x + (y+1))
    
    
    for query in queries:
        x1 = query[0] - 1
        y1 = query[1] - 1
        x2 = query[2] - 1
        y2 = query[3] - 1
        
        rot = rotation(matrix, x1, y1, x2, y2)
        matrix = rot[0]
        answer.append(rot[1])
    
    
    
    return answer
