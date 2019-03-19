minefield = [
  [0, 1, 0, 0, 1],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 0, 1],
]


'''
Check if input is valid
  - only numbers "0" and "1" allowed in minefield
  - minefield must be rectangular

@param {array of arrays} minefield - The input minefield
@param {integer} num_columns - The number of columns in every row of the input minefield

@returns {Boolean}
'''  # noqa


def input_is_valid(minefield, num_columns):
    for row in minefield:
        if num_columns != len(row):
            return False

        for j in range(0, len(row)):
            if row[j] != 0 and row[j] != 1:
                return False

    return True


'''
Add "0"'s' along all edges of input minefield

@param {array of arrays} minefield - The input minefield
@param {integer} num_columns - The number of columns in every row of the input minefield

@returns {array of arrays}  extended_minefield - The input minefield with ghost cells added
'''  # noqa


def add_ghost_cells(minefield, num_columns):
    extended_minefield = []
    for row in minefield:
        extended_minefield.append([0] + row + [0])

    ghost_row = [[0]*(num_columns+2)]
    extended_minefield = ghost_row + extended_minefield + ghost_row

    return extended_minefield


'''
Count the nubmer of mines in adjacent

@param {array of arrays} extended_minefield - The input minefield with ghost cells
@param {integer} num_rows - The number of rows of the input minefield
@param {integer} num_columns - The number of columns in every row of the input minefield

@returns {array of arrays}  mine_count - the number of mines in adjacent squares.  Has same dimensions
                                         as input minefield
'''  # noqa


def count_adjacent_mines(extended_minefield, num_rows, num_columns):
    mine_count = []
    for i in range(1, num_rows + 1):
        row_mine_count = []
        for j in range(1, num_columns + 1):
            if extended_minefield[i][j] != 1:
                row_mine_count.append(
                    sum(extended_minefield[i-1][j-1:j+2]) +
                    extended_minefield[i][j-1] +
                    extended_minefield[i][j+1] +
                    sum(extended_minefield[i+1][j-1:j+2])
                )
            else:
                row_mine_count.append(9)
        mine_count.append(row_mine_count)

    return mine_count


'''
Controlling function

@param {array of arrays} minefield - The input minefield

@returns {array of arrays}  mine_count - the number of mines in adjacent squares
'''  # noqa


def minesweeper(minefield):
    num_columns = len(minefield[0])
    num_rows = len(minefield)

    if input_is_valid(minefield, num_columns):
        extended_minefield = add_ghost_cells(minefield, num_columns)
        mine_count = count_adjacent_mines(
            extended_minefield, num_rows, num_columns
        )
        return mine_count
    else:
        return 0


if __name__ == '__main__':
    mine_count = minesweeper(minefield)

    if mine_count:
        print('The input minefield is:')
        for row in minefield:
            print(row)
        print('')
        print('The number of mines in the adjacent squares are:')
        for row in mine_count:
            print(row)
    else:
        print('Please specify a valid input minefield')
