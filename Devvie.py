def solution(line):    
    xDistance, yDistance, direction = 0, 0, 0
    for command in line:
        command = command.upper()
        if command == 'F':
            if direction % 360 == 0: #north
                yDistance += 1
            elif direction % 360 == 90: # east
                xDistance += 1
            elif direction % 360 == 180: # south
                yDistance -= 1
            elif direction % 360 == 270: # west
                xDistance -= 1
        elif command == 'L':
            direction -= 90
            if direction < 0:
                direction = 270
        elif command == 'R':
            direction += 90
            if direction > 360:
                direction = 90
        else:
            pass
        print(direction, yDistance, xDistance)
    
    # Now work out path from those coords back to 0,0
    numMoves = 0
    while xDistance != 0:
        if xDistance > 0:
            # If heading west remove distance
            if direction == 270:
                direction = 270
                xDistance -= 1
                numMoves += 1
                print("F"+str(direction))
            # If not, turn around x times to west
            else:
                while direction != 270:
                    # work out if its better to turn right than left
                    if direction == 180:
                        direction += 90
                    else:
                        direction -= 90
                        if direction < 0:
                            direction = 270
                    numMoves += 1
                    print("L"+str(direction))
        elif xDistance < 0:
            # If heading east add distance
            if direction == 90:
                xDistance += 1
                numMoves += 1
                print("F"+str(direction))
            # If not, turn around x times to east
            else:
                while direction != 90:
                    # work out if its better to turn right than left
                    if direction == 0 or direction == 270:
                        direction += 90
                        if direction > 360:
                            direction = 90
                    else:
                        direction -= 90
                        if direction < 0:
                            direction = 270
                    numMoves += 1
                    print("L"+str(direction))
    while yDistance != 0:
        if yDistance > 0:
            # if heading south remove yDistance
            if direction == 180:
                yDistance -= 1
                numMoves += 1
                print("F"+str(direction))
            else:
                while direction != 180:
                    # work out if its better to turn right than left
                    if direction == 90:
                        direction += 90
                    else:
                        direction -= 90
                        if direction < 0:
                            direction = 270
                    numMoves += 1
                    print("L"+str(direction))
        elif yDistance < 0:
            # if heading north add yDistance
            if direction == 0 or direction == 360: 
                yDistance += 1
                numMoves += 1
                print("F"+str(direction))
            else:
                while direction != 0 and direction != 360:
                    # work out if its better to turn right than left
                    if direction == 270:
                        direction += 90
                    else:
                        direction -= 90
                        if direction < 0:
                            direction = 270
                    numMoves += 1
                    print("L"+str(direction))
    return numMoves

print(solution("LFRFRFR"))