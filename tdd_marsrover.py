import unittest

# Globale Variablen für die Position des Rovers
x, y = 0, 0

# Funktion zur Initialisierung des Rovers
def initialize_rover(local_x, local_y, direction):
    global x, y
    x, y = local_x, local_y

# Funktion zur Ausführung der Befehle
def execute_commands(commands):
    global x, y
    if not commands:
        return

    if commands[0] == 'f':
        x += 1
    elif commands[0] == 'b':
        x -= 1

# Testklasse für den Mars Rover
class TestTheMarsRover(unittest.TestCase):

    # Test zur Überprüfung der initialen Position des Rovers
    def test_initial_position(self):
        initialize_rover(1, 0, 'N')
        self.assertEqual(x, 1)

    # Test zur Überprüfung, ob der Rover einen leeren Befehlsarray akzeptiert
    def test_pass_commands_array(self):
        commands = []
        execute_commands(commands)

    # Test zur Überprüfung, ob der Rover sich um einen Schritt nach vorne bewegt
    def test_moves_one_forward(self):
        # Arrange
        initialize_rover(0, 0, 'N')
        # Act
        execute_commands(['f'])
        # Assert
        self.assertEqual(x, 1)

    # Test zur Überprüfung, ob der Rover sich um einen Schritt rückwärts bewegt
    def test_moves_one_backward(self):
        # Arrange
        initialize_rover(0, 0, 'N')
        # Act
        execute_commands(['b'])
        # Assert
        self.assertEqual(x, -1)

if __name__ == '__main__':
    unittest.main()
