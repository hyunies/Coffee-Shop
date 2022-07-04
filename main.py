# Written by Sihyun (Erin) Park
# Last Edited 2020 10 15
# This program calculates the volume of a cube, pyramid and ellipsoid based on the dimensions inputted

# Importing summarize module
import summarize
# Importing volume module for functions used to calculate volume
import volumes


# Lists for calculated volumes of cubes, pyramids and ellipsoids, respectively
clist = []
plist = []
elist = []

# List used to determine if quit option was used before actually calculating any volumes
total_list = []

# First while loop allows escape from the second loop if input is valid
while True:
    while True:
        shape = input('What shape are you looking for the volume of? (“cube” or “c”, “pyramid” or “p”, “ellipsoid” or “e”, “quit” or “q"): ')
        if shape.lower() not in ('cube', 'c', 'pyramid', 'p', 'ellipsoid', 'e', 'quit', 'q'):
            # Prompting user for valid input if input is not accepted
            print('Please input a valid option.')
        else:
            # Allows escape from loop if input is valid
            break
# If statements to determine if code should print "You did not perform any calculations", "No shape entered" or the sorted list of volumes calculated when program is terminated
    if shape.lower() == 'q':
        if total_list == []:
            print('''
You have reached the end of your session.
You did not perform any volume calculations.
            ''')
        else:
            print('''
You have reached the end of your session. 
The volumes calculated for each shape are:
            ''')
            if clist != []:
                clist.sort()
                print('Cube: ', ", ".join(map(str, clist)))
            if clist == []:
                print('Cube: No shapes entered.')
            if plist != []:
                plist.sort()
                print('Pyramid: ', ", ".join(map(str, plist)))
            if plist == []:
                print('Pyramid: No shapes entered.')
            if elist != []:
                elist.sort()
                print('Ellipsoid: ', ", ".join(map(str, elist)))
            if elist == []:
                print('Ellipsoid: No shapes entered.')
            # Using summarize.py
            testNumber = int(input('Test Number: '))
            summary = summarize.summarize(clist, plist, elist, testNumber)
        break
# Previous if statements repeated for the input 'quit'
    elif shape.lower() == 'quit':
        if total_list == []:
            print('''
You have reached the end of your session.
You did not perform any volume calculations.
            ''')
        else:
            print('''
You have reached the end of your session. 
The volumes calculated for each shape are:
            ''')
            if clist != []:
                clist.sort()
                print('Cube: ', ", ".join(map(str, clist)))
            if clist == []:
                print('Cube: No shapes entered.')
            if plist != []:
                plist.sort()
                print('Pyramid: ', ", ".join(map(str, plist)))
            if plist == []:
                print('Pyramid: No shapes entered.')
            if elist != []:
                elist.sort()
                print('Ellipsoid: ', ", ".join(map(str, elist)))
            if elist == []:
                print('Ellipsoid: No shapes entered.')
        # Using summarize.py
        testNumber = int(input('Test Number: '))
        summary = summarize.summarize(clist, plist, elist, testNumber)
        break
# Calculating volumes for cubes
    if shape.lower() == 'cube':
        side_length = float(input('Please enter the length of the sides: '))
        # Using the cube_volume function from volumes.py
        cube_volume = volumes.cube_calculator(side_length)
        # Rounding cube_volume to 2 decimal places
        cube_volume = round(cube_volume, 2)
        # Appending the volume to the list of cube volumes
        clist.append(cube_volume)
        # Appending the volume to the list of all calculations
        total_list.append(cube_volume)
    elif shape.lower() == 'c':
        side_length = float(input('Please enter the length of the sides: '))
        cube_volume = volumes.cube_calculator(side_length)
        cube_volume = round(cube_volume, 2)
        clist.append(cube_volume)
        total_list.append(cube_volume)
# Calculating volumes for pyramids
    elif shape.lower() == 'pyramid':
        base_length = float(input('Please enter the base length: '))
        height = float(input('Please enter the height: '))
        pyramid_volume = volumes.pyramid_calculator(base_length, height)
        pyramid_volume = round(pyramid_volume, 2)
        plist.append(pyramid_volume)
        total_list.append(pyramid_volume)
    elif shape.lower() == 'p':
        base_length = float(input('Please enter the base length: '))
        height = float(input('Please enter the height: '))
        pyramid_volume = volumes.pyramid_calculator(base_length, height)
        pyramid_volume = round(pyramid_volume, 2)
        plist.append(pyramid_volume)
        total_list.append(pyramid_volume)
# Calculating volumes for ellipsoids
    elif shape.lower() == 'ellipsoid':
        radius1 = float(input('Please enter radius 1: '))
        radius2 = float(input('Please enter radius 2: '))
        radius3 = float(input('Please enter radius 3: '))
        ellipsoid_volume = volumes.ellipsoid_calculator(radius1, radius2, radius3)
        ellipsoid_volume = round(ellipsoid_volume, 2)
        elist.append(ellipsoid_volume)
        total_list.append(ellipsoid_volume)
    elif shape.lower() == 'e':
        radius1 = float(input('Please enter radius 1: '))
        radius2 = float(input('Please enter radius 2: '))
        radius3 = float(input('Please enter radius 3: '))
        ellipsoid_volume = volumes.ellipsoid_calculator(radius1, radius2, radius3)
        ellipsoid_volume = round(ellipsoid_volume, 2)
        elist.append(ellipsoid_volume)
        total_list.append(ellipsoid_volume)
