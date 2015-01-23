# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']
# path_matrix gives the optimal path
path_matrix = [['.' for row in range(len(grid[0]))] for col in range(len(grid))]

cost = 1

# Magic code I do not understand
def print_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)
    
def findLowestCostCell(cost_cells, current_cell):
    print 'current cell'
    print current_cell
    x = current_cell[0]
    y = current_cell[1]
    min_cost = 100
    for i in range(len(delta)):
        x2 = x + delta[i][0]
        y2 = y + delta[i][1]
        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
            print cost_cells[x2][y2]
            if cost_cells[x2][y2] < min_cost and cost_cells[x2][y2] != -1:
                min_cost = cost_cells[x2][y2]
                min_cost_cell = [x2, y2]
                min_cost_i = (i + 2)%4
    path_matrix[min_cost_cell[0]][min_cost_cell[1]] = delta_name[min_cost_i]
    return min_cost_cell
        
                    
def find_optimal_path(cost_cells):
    optimal_path = [goal]
    current_cell = goal
    while current_cell != init:
        print 'current cell in find_optimal_path'
        print current_cell
        current_cell = findLowestCostCell(cost_cells, current_cell)
        optimal_path.append(current_cell)
    path_matrix[goal[0]][goal[1]] = '*'
    print_matrix(path_matrix)
    return optimal_path
    

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    
    # closed_cells checks which cells we have traversed
    closed_cells = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed_cells[init[0]][init[1]] = 1
    
    # counter_cells counts how many iterations it took to reach that cell
    counter_cells = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    count = 0
    counter_cells[init[0]][init[1]] = count
    
    # cost_cell counts what's the optimal cost to reach to that cell
    cost_cells = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    
    # intitial starting or seed location
    x = init[0]
    y = init[1]
    # g is the cost to get to that location
    g = 0
    
    # add to the open_cell list. We will use this list to do sort of a breadth-first search
    open_cell = [[g, x, y]]
    
    # found flag is set when you reach the goal location
    found = False
    # resign flag is for cases when you do not have any possible path
    resign = False
     
    while found is False and resign is False:
        # when there are no elements left in the open cell
        if len(open_cell) == 0:
            resign = True
            print 'fail'
        # if there are elements in the open cell take an element out of it    
        else:
            # sort to choose the lowest cost one
            open_cell.sort()
            # reverse because sort sorts it in the opposite order
            open_cell.reverse()
            next_cell = open_cell.pop()
            print 'take list item'
            print next_cell
            x = next_cell[1]
            y = next_cell[2]
            g = next_cell[0]
            counter_cells[x][y] = count
            count = count + 1
            print 'counter cells: '
            print_matrix(counter_cells)
            cost_cells[x][y] = g

        
        # check if done
        if x == goal[0] and y == goal[1]:
            found = True
            print next_cell 
            print '#### Search successful'
        
        else:
            # expand winning (lowest cost) element and add to the new open_cell list
            # iterate over possible x_+ and y_+ configurations
            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                # make sure that they are in the grid
                if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                    # make sure that they are not explored
                    if closed_cells[x2][y2] == 0 and grid[x2][y2] == 0:
                        # increment the cost
                        g2 = g + cost
                        # add it to the open_cell list
                        open_cell.append([g2, x2, y2])
                        # set the value in closed_cells to inform that this block has been explored
                        closed_cells[x2][y2] = 1
                        # set the cost in the cost_cell matrix to search for the best path

    
    print open_cell
    
    print 'Given problem: '
    print_matrix(grid)
    print 'Explored cells: '
    print_matrix(closed_cells)
    print 'cost_cells'
    print_matrix(cost_cells)
    print 'max'
    print max(max(cost_cells))
    print cost_cells[4][0]
    print range(len(cost_cells[0]))
    print range(len(cost_cells))
#     print cost_cells[5][0]
#     for row_y in range(len(cost_cells)):
#         for col_x in range(len(cost_cells[0])):
#             print [row_y, col_x]
#             cost_cells[row_y][col_x] = 11 - cost_cells[row_y][col_x]
    print 'cost_cells'
    print_matrix(cost_cells) 
    find_optimal_path(cost_cells)
    
    return open_cell # you should RETURN your result

search()

