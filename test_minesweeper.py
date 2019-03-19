import copy

import unittest

from minesweeper import (
    add_ghost_cells,
    count_adjacent_mines,
    input_is_valid,
    minesweeper
)


class ValidateInputTest(unittest.TestCase):
    def test_minefield_contains_only_1_or_0(self):
        correct_minefield = [
            [0, 1],
            [1, 0]
        ]

        num_columns = 2

        minefield_with_non_integer = copy.deepcopy(correct_minefield)
        minefield_with_non_integer[0][0] = 1.1

        minefield_with_negative_integer = copy.deepcopy(correct_minefield)
        minefield_with_negative_integer[1][1] = -1

        minefield_with_unallowed_integer = copy.deepcopy(correct_minefield)
        minefield_with_unallowed_integer[0][1] = 7

        assert input_is_valid(correct_minefield, num_columns)
        assert not input_is_valid(minefield_with_non_integer, num_columns)
        assert not input_is_valid(minefield_with_negative_integer, num_columns)
        assert not input_is_valid(minefield_with_unallowed_integer, num_columns)

    def test_minefield_is_rectangular(self):
        non_rectangular_minefield = [
          [0, 1, 0],
          [0, 1],
          [0, 1, 0],
        ]

        assert not input_is_valid(non_rectangular_minefield, 2)


class AddGhostCellsTest(unittest.TestCase):
    def test_ghost_cells_are_added_correctly(self):
        input_minefield = [
            [0, 1],
            [1, 0]
        ]

        expected_minefield = [
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ]

        mine_field_with_ghost_cells = add_ghost_cells(input_minefield, 2)

        assert mine_field_with_ghost_cells == expected_minefield


class CountMinesTest(unittest.TestCase):
    def test_count_adjacent_mines(self):
        minefield_with_ghost_cells = [
          [0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 1, 0],
          [0, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
        ]

        # number of rows and columns should be equal to dimensions of initial
        # minefield, i.e., without ghost cells
        num_rows = 4
        num_columns = 4

        expected_mine_count = [
            [1, 9, 2, 1],
            [2, 3, 9, 2],
            [3, 9, 4, 9],
            [9, 9, 3, 1],
        ]

        mine_count = count_adjacent_mines(
            minefield_with_ghost_cells,
            num_rows,
            num_columns
        )

        assert mine_count == expected_mine_count


class ControlFunctionTest(unittest.TestCase):
    def test_integration_valid_minefield(self):
        input_minefield = [
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 1, 0, 1],
          [1, 1, 0, 0],
        ]

        expected_mine_count = [
            [1, 9, 2, 1],
            [2, 3, 9, 2],
            [3, 9, 4, 9],
            [9, 9, 3, 1],
        ]

        mine_count = minesweeper(
            input_minefield,
        )

        assert mine_count == expected_mine_count

    def test_integration_invalid_minefield(self):
        input_minefield = [
          [0, 1, 0, 0],
          [1, 0],
          [0, 1, 0, 0],
          [1, 1, 0, 0],
        ]

        expected_mine_count = 0

        mine_count = minesweeper(
            input_minefield,
        )

        assert mine_count == expected_mine_count
