'''

Day 40 Cup of Code


Write a function that will take 3 arguments:
bombs = list of bomb locations
rows, columns
mine_sweeper([[0,0], [1,2]], 3, 4)

bomb at row index 0 column index 0
bomb at row index 0 column index 1
3 rows
4 columns

we should return a 3 x 4 array (-1) = bomb
'''

def mine_sweeper(bombs, num_rows, num_cols):
    # create list of lists with all zeros
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    
    for bomb_location in bombs:
        
        # noting bomb locations
        (bomb_row, bomb_col) = bomb_location
        
        # placing bombs
        field[bomb_row][bomb_col] = -1
    
        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for i in row_range:
            current_i = i # used for debugging
            for j in col_range:
                current_j = j # used for debugging

mine_sweeper([[0,0], [1,2]], 3, 4)