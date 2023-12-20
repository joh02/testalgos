'''
christmas tree:
bel Größe mit mittigem Stamm der Länge 1
z.B. tree(1):
*
|

tree(2):
 *
***
 |

'''

import pytest

def getCrownLine(index, height):
    anzX = 2 * index + 1
    maxX = 2 * height - 1
    anzSpaces = int((maxX - anzX) / 2)
    crownLine = anzSpaces*' '  + anzX*'X' +  anzSpaces*' ' + '\n'
    return crownLine

def getTrunkString(height):
    anzTrunkSpaces = height - 1
    trunkString = anzTrunkSpaces * ' ' +'|' + anzTrunkSpaces * ' '  +  '\n'
    return trunkString

def get_tree(height):
    treeStr = ''
    #only int > 0
    if height:
        #Kronenzeilen:
        for index in range(height):
            treeStr += getCrownLine(index, height)
        #Stammzeile
        treeStr += getTrunkString(height)
    return treeStr

# ------------------ tests ----------------------

def test_Anz_lines0():
    assert get_tree(0) == '', 'Anzahl null wird falsch bedient'

def test_anz_lines_gesamt():
    '''test Gesamtlänge incl Stammzeile'''
    for i in range(1,4+1):
        treeStr = get_tree(i)
        assert len(get_tree(i).splitlines()) - 1 == i, f'Längenfehler bei Länge {i}'

def test_trunk():
    assert '|' in getTrunkString(2), 'no | in trunk string'

def test_anz_ges():
    for i in range(1,4+1):
        assert len(get_tree(i)) == 2*i**2+2*i

if __name__ == '__main__':
    print(get_tree(20))
