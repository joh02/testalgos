# according to:
# https://github.com/technicalagilecoach/RemoteTDDPracticeGroup/blob/main/20240116-Softwaredesign_mit_Bottom-up-TDD/mars_rover.cpp
# https://kata-log.rocks/images/mars_rover.jpg


import unittest

# Global variables for the position of the rover
x, y = 0, 0
dir = 'n'

# Commands, etc.
f = 'f'
b = 'b'
n = 'n'
e = 'e'
s = 's'
w = 'w'
l = 'l'
r = 'r'


def initialize_rover(local_x, local_y, direction=n):
    '''Initialize the rover
    '''
    global x, y, dir
    x, y, dir = local_x, local_y, direction


def execute_commands(commands):
    '''Execution of commands
    '''
    global x, y, dir
    if not commands:
        return
    else:  # at least 1 character/cmd
        while commands:
            cmd = commands[0] # get and cut the cmd from the list
            commands = commands[1:]

            if cmd in ('l', 'r'):  # turning
                trn = dir + cmd
                dir = {'nl': w,
                       'el': n,
                       'sl': e,
                       'wl': s,
                       'nr': e,
                       'er': s,
                       'sr': w,
                       'wr': n,
                       }[trn]

            if cmd in ('f', 'b'):  # moving
                mov = cmd + dir
                inc_x, inc_y = {'fn': (0, 1),  # move forward, facing north
                                'fe': (1, 0),
                                'fs': (0, -1),
                                'fw': (-1, 0),
                                'bn': (0, -1),
                                'be': (-1, 0),
                                'bs': (0, 1),
                                'bw': (1, 0),
                                }[mov]
                x += inc_x
                y += inc_y



#-- TDD tests ----------------------------------------------------------------
class TestTheMarsRover(unittest.TestCase):
    '''Test class for the Mars Rover
    '''

    def test_initial_position(self):
        '''Test to check the initial position of the rover
        '''
        initialize_rover(1, 0, 'n')
        self.assertEqual(x, 1)

    def test_pass_commands_array(self):
        '''Test if the rover accepts an empty command array
        '''
        commands = []
        execute_commands(commands)

    def test_moves_square_seq1(self):
        '''Test if the rover returns to the starting point after moving in a square, cmd-sequence1
        '''
        # Arrange
        initialize_rover(0, 0, 'e')
        # Act
        execute_commands(['frfrfrf'])
        # Assert
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

    def test_moves_square_seq2(self):
        '''Test if the rover returns to the starting point after moving in a square, cmd-sequence2
        '''
        # Arrange
        initialize_rover(-2, 3, 's')
        # Act
        execute_commands(['frfrfrf'])
        # Assert
        self.assertEqual(x, -2)
        self.assertEqual(y, 3)

    def test_moves_square(self):
        '''Test if the rover returns to the starting point after moving in a square
        '''
        # Arrange
        initialize_rover(0, 0, 'e')
        # Act
        execute_commands(['f'])
        execute_commands(['r'])
        execute_commands(['f'])
        execute_commands(['r'])
        execute_commands(['f'])
        execute_commands(['r'])
        execute_commands(['f'])
        # Assert
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

    def test_moves_one_backward(self):
        '''Test if the rover moves one step backward
        '''
        # Arrange
        initialize_rover(0, 0, 'n')
        # Act
        execute_commands(['b'])
        # Assert
        self.assertEqual(y, -1)

    def test_moves_one_forward(self):
        '''Test if the rover moves one step forward
        '''
        # Arrange
        initialize_rover(0, 0, 'n')
        # Act
        execute_commands(['f'])
        # Assert
        self.assertEqual(y, 1)

if __name__ == '__main__':
    unittest.main()
