""" Functions related to wire wrangling """

def earliest_intersection(paths: str) -> int:
    current_x = 0
    current_y = 0

    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0

    path_a, path_b = paths.split('\n')

    for move in path_a.split(','):
        direction = move[0]
        distance = int(move[1:])

        if direction == 'R':
            current_x += distance
        elif direction == 'L':
            current_x -= distance
        elif direction == 'U':
            current_y += distance
        elif direction == 'D':
            current_y -= distance
        else:
            raise ValueError(f'Invalid direction: {direction}')

        if current_x > max_x:
            max_x = current_x
        if current_x < min_x:
            min_x = current_x
        if current_y > max_y:
            max_y = current_y
        if current_y < min_y:
            min_y = current_y
    
    current_x = 0
    current_y = 0

    for move in path_b.split(','):
        direction = move[0]
        distance = int(move[1:])

        if direction == 'R':
            current_x += distance
        elif direction == 'L':
            current_x -= distance
        elif direction == 'U':
            current_y += distance
        elif direction == 'D':
            current_y -= distance
        else:
            raise ValueError(f'Invalid direction: {direction}')

        if current_x > max_x:
            max_x = current_x
        if current_x < min_x:
            min_x = current_x
        if current_y > max_y:
            max_y = current_y
        if current_y < min_y:
            min_y = current_y
        
    offset_x = abs(min_x)
    offset_y = abs(min_y)

    grid = [[False for y in range(max_y + offset_y + 1)] for x in range(max_x + offset_x + 1)]

    current_x = offset_x
    current_y = offset_y
    steps = 0

    grid[current_x][current_y] = 0

    for move in path_a.split(','):
        direction = move[0]
        distance = int(move[1:])

        if direction == 'R':
            steps = fill_steps_x(current_x+1, current_x+distance, current_y, grid, steps)
            current_x += distance
        elif direction == 'L':
            steps = fill_steps_x(current_x-1, current_x-distance, current_y, grid, steps)
            current_x -= distance
        elif direction == 'U':
            steps = fill_steps_y(current_y+1, current_y+distance, current_x, grid, steps)
            current_y += distance
        elif direction == 'D':
            steps = fill_steps_y(current_y-1, current_y-distance, current_x, grid, steps)
            current_y -= distance
    
    current_x = offset_x
    current_y = offset_y
    steps = 0

    intersections = []

    for move in path_b.split(','):
        direction = move[0]
        distance = int(move[1:])

        current_intersections = []

        if direction == 'R':
            steps, current_intersections = check_steps_x(current_x+1, current_x+distance, current_y, grid, steps)
            current_x += distance
        elif direction == 'L':
            steps, current_intersections = check_steps_x(current_x-1, current_x-distance, current_y, grid, steps)
            current_x -= distance
        elif direction == 'U':
            steps, current_intersections = check_steps_y(current_y+1, current_y+distance, current_x, grid, steps)
            current_y += distance
        elif direction == 'D':
            steps, current_intersections = check_steps_y(current_y-1, current_y-distance, current_x, grid, steps)
            current_y -= distance
        
        if current_intersections:
            intersections.extend(current_intersections)
    
    return min(intersections) + 2


def fill_steps_x(start_x, end_x, current_y, grid, steps):
    x_range = None
    if start_x < end_x:
        x_range = range(start_x, end_x+1)
    else:
        x_range = reversed(range(end_x, start_x+1))

    for x in x_range:
        if not grid[x][current_y]:
            grid[x][current_y] = steps

        steps += 1
    
    return steps


def fill_steps_y(start_y, end_y, current_x, grid, steps):
    y_range = None

    if start_y < end_y:
        y_range = range(start_y, end_y+1)
    else:
        y_range = reversed(range(end_y, start_y+1))

    for y in y_range:
        if not grid[current_x][y]:
            grid[current_x][y] = steps
        steps += 1
    
    return steps


def check_steps_x(start_x, end_x, current_y, grid, steps):
    intersections = []

    x_range = None
    if start_x < end_x:
        x_range = range(start_x, end_x+1)
    else:
        x_range = reversed(range(end_x, start_x+1))

    for x in x_range:
        if grid[x][current_y]:
            intersections.append(grid[x][current_y] + steps)
        
        steps += 1
    
    return steps, intersections


def check_steps_y(start_y, end_y, current_x, grid, steps):
    intersections = []

    y_range = None

    if start_y < end_y:
        y_range = range(start_y, end_y+1)
    else:
        y_range = reversed(range(end_y, start_y+1))

    for y in y_range:
        if grid[current_x][y]:
            intersections.append(grid[current_x][y] + steps)
        
        steps += 1
    
    return steps, intersections


def nearest_intersection(paths: str) -> int:
    current_x = 0
    current_y = 0

    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0

    path_a, path_b = paths.split('\n')

    for move in path_a.split(','):
        direction = move[0]
        distance = int(move[1:])

        if direction == 'R':
            current_x += distance
        elif direction == 'L':
            current_x -= distance
        elif direction == 'U':
            current_y += distance
        elif direction == 'D':
            current_y -= distance
        else:
            raise ValueError(f'Invalid direction: {direction}')

        if current_x > max_x:
            max_x = current_x
        if current_x < min_x:
            min_x = current_x
        if current_y > max_y:
            max_y = current_y
        if current_y < min_y:
            min_y = current_y
    
    current_x = 0
    current_y = 0

    for move in path_b.split(','):
        direction = move[0]
        distance = int(move[1:])

        if direction == 'R':
            current_x += distance
        elif direction == 'L':
            current_x -= distance
        elif direction == 'U':
            current_y += distance
        elif direction == 'D':
            current_y -= distance
        else:
            raise ValueError(f'Invalid direction: {direction}')

        if current_x > max_x:
            max_x = current_x
        if current_x < min_x:
            min_x = current_x
        if current_y > max_y:
            max_y = current_y
        if current_y < min_y:
            min_y = current_y
        
    offset_x = abs(min_x)
    offset_y = abs(min_y)

    grid = [[False for y in range(max_y + offset_y + 1)] for x in range(max_x + offset_x + 1)]

    current_x = offset_x
    current_y = offset_y

    for move in path_a.split(','):
        direction = move[0]
        distance = int(move[1:])

        if direction == 'R':
            fill_x(current_x, current_x+distance, current_y, grid)
            current_x += distance
        elif direction == 'L':
            fill_x(current_x-distance, current_x, current_y, grid)
            current_x -= distance
        elif direction == 'U':
            fill_y(current_y, current_y+distance, current_x, grid)
            current_y += distance
        elif direction == 'D':
            fill_y(current_y-distance, current_y, current_x, grid)
            current_y -= distance
    
    current_x = offset_x
    current_y = offset_y

    intersections = []

    for move in path_b.split(','):
        direction = move[0]
        distance = int(move[1:])

        current_intersections = []

        if direction == 'R':
            current_intersections = check_x(current_x, current_x+distance, current_y, grid)
            current_x += distance
        elif direction == 'L':
            current_intersections = check_x(current_x-distance, current_x, current_y, grid)
            current_x -= distance
        elif direction == 'U':
            current_intersections = check_y(current_y, current_y+distance, current_x, grid)
            current_y += distance
        elif direction == 'D':
            current_intersections = check_y(current_y-distance, current_y, current_x, grid)
            current_y -= distance
        
        if current_intersections:
            intersections.extend(current_intersections)

    min_intersection = 0

    for intersection in intersections:
        distance_from_origin = abs(intersection[0] - offset_x) + abs(intersection[1] - offset_y)
        if not min_intersection:
            min_intersection = distance_from_origin
        elif distance_from_origin and distance_from_origin < min_intersection:
            min_intersection = distance_from_origin
    
    return min_intersection


def fill_x(start_x, end_x, current_y, grid):
    for x in range(start_x, end_x+1):
        grid[x][current_y] = True


def fill_y(start_y, end_y, current_x, grid):
    for y in range(start_y, end_y+1):
        grid[current_x][y] = True


def check_x(start_x, end_x, current_y, grid):
    intersections = []

    for x in range(start_x, end_x+1):
        if grid[x][current_y]:
            intersections.append((x,current_y))
    
    return intersections


def check_y(start_y, end_y, current_x, grid):
    intersections = []

    for y in range(start_y, end_y+1):
        if grid[current_x][y]:
            intersections.append((current_x,y))
    
    return intersections


def print_grid_steps(grid):
    for y in reversed(range(len(grid[0]))):
        print(f'{str(y).rjust(3, " ")}', end='')
        for x in range(len(grid)):
            if grid[x][y]:
                print(str(grid[x][y]).rjust(5), end='')
            else:
                print('     ', end='')
        print('')


def print_grid(grid):
    for y in reversed(range(len(grid[0]))):
        print(f'{str(y).rjust(3, " ")}', end='')
        for x in range(len(grid)):
            if grid[x][y]:
                print('█', end='')
            else:
                print(' ', end='')
        print('')