'''
This program allows a user to input vectors in order to 
1. compute dot products
2. compute cross products
3. compute projections

Time spent: 4 hr, 52 mins
4:20

'''




import numpy as np

def main():
    vectors = []
    # Create u and v indexes so error handling doesn't reference them before assignment.
    u_index = -1
    v_index = -1
    # Kick off while loops.
    option = None
    menu_options = ['Enter a vector','Compute a dot product','Compute projection','Compute a cross product','Show all vectors','quit']

    while option != menu_options.index('quit'):
        # Give menu options and give user a chance to choose. 
        print('\n\nPlease choose from one of the following options: ')
        for i in range(len(menu_options)):
            print(f'{i+1}. {menu_options[i]}')
        
               

        try: 
            option = int(input('Enter the number of your selection: ')) - 1

            # Enter a vector.
            if option == menu_options.index('Enter a vector'):
                # Ask user for amount of dimensions so we know how many numbers to ask for.
                dimensions = 0

                while dimensions < 1:
                    dimensions = int(input('How many dimensions? '))


                vector = create_vector(dimensions)
                
                # Add new vectors into a list of all the vectors.
                vectors.append(vector)

            # Compute dot product.
            if option == menu_options.index('Compute a dot product'):
                # Print user options for vectors to choose for calculation.
                for i in range(len(vectors)):
                    print(f'{i+1}. {vectors[i]}')

                # Let user select the vectors they want to dot.

                u = vectors[int(input('Enter index number of first vector: ')) - 1]
                v = vectors[int(input('Enter index number of second vector: ')) - 1]

                # Check to see if vectors are the same size or not.
                if len(u) != len(v):
                    print('The two vectors you chose aren\'t the same length. Try again.')
                
                else:
                    # Get a dot product from the vectors
                    dot_product = compute_dot_product(u, v)
                    
                    print(f'\nThe dot product of {u} and {v} is {dot_product}.')

                    if dot_product == 0:
                        print(f'\n{u} and {v} are orthogonal.')
            
            # Compute cross product. 
            elif option == menu_options.index('Compute a cross product'):
                # Print user options for vectors to choose for calculation.
                for i in range(len(vectors)):
                    print(f'{i+1}. {vectors[i]}')

                # Let user select the vectors they want to cross.
                u_index = int(input('Enter index number of first vector: ')) - 1
                v_index = int(input('Enter index number of second vector: ')) - 1
                
                u = vectors[u_index]
                v = vectors[v_index]

                # Check to see if vectors are the same size or not.
                if len(u) != len(v):
                    print('The two vectors you chose aren\'t the same length. Try again.')
                elif len(u) != 3 or len(v) != 3:
                    print('Incompatible dimensions for cross product of the vectors you selected. Dimension must be 3. Try again.')

                else:
                    # Get a cross product from the vectors
                    cross_product = compute_cross_product(u, v)

                    print(f'\nThe cross product of {u} and {v} is {cross_product}')

            elif option == menu_options.index('Compute projection'):
                # Print user options for vectors to choose for calculation.
                for i in range(len(vectors)):
                    print(f'{i+1}. {vectors[i]}')

                # Let the user pick which vector gets projected onto which
                print('\nThe first vector will be projected onto the second.')
                u_index = int(input('Enter index number of first vector: ')) - 1
                v_index = int(input('Enter index number of second vector: ')) - 1
                
                u = vectors[u_index]
                v = vectors[v_index]

                # Check to see if vectors are the same size or not.
                if len(u) != len(v):
                    print('The two vectors you chose aren\'t the same length. Try again.')

                else:
                    projection = compute_projection(u, v)

                    # # Keep -0 from showing up. Find the index location of the -0 and replace it with 0.
                    # print(np.searchsorted(projection, -0))

                    print(f'The projection of {u} onto {v} is {projection}.')

            # Show all vectors.
            elif option == menu_options.index('Show all vectors'):
                if vectors == []:
                    print('\nNo vectors have been added.')

                else: 
                    # Print each vector line by line
                    for vector in vectors: 
                        print(vector)

        except ValueError as value_err:
            print('\nPlease enter a valid number. ')

        except IndexError as index_err:
            if u_index == -1:
                print('Please enter your vectors.')

            elif u_index < 0 or v_index < 0:
                print('Please enter the index number of an existing vector.')
            
            elif u_index > len(vectors) or v_index > len(vectors):
                print('Please enter the index number of an existing vector.')
            
            else: 
                print('Please enter a valid number.')
        
    print('\nEnd.')

def create_vector(dimensions):
    '''
    Asks for user input to store a vector in an array.
    Parameters: 
        dimensions, the amount of variables
    Returns: 
        a vector in the form of an array.
    '''
    # Create empty list for vector to fill.
    vector = []

    # Announce that a new vector is getting stored.
    print('\nINPUT VECTOR ')

    # Append one number for each dimension they specified.
    for _ in range(dimensions):
        number = float(input('Enter a number to fill up your vector: '))

        vector.append(number)

    # Convert vector list into an array
    vector = np.array(vector)

    return vector
    
def compute_dot_product(u, v):
    '''
    Computes the dot product of two vectors u & v. 
    Parameters:
        u, v
    Returns:
        dot product
    '''

    # Compute the dot product of the two vectors. 
    dot_product = u @ v

    return dot_product

def compute_cross_product(u, v):
    '''
    Computes the cross product of two vectors u & v. 
    Parameters:
        u, v
    Returns:
        cross product
    '''
    # Compute the cross product of the two vectors.
    cross_product = np.cross(u, v)

    return cross_product


def compute_projection(u, v):
    '''
    Computes the projection of vector u onto vector v.
    Parameters: 
        u, v
    Returns:
        projection of u onto v
    '''
    projection = (np.dot(u, v)/np.dot(v, v)) * v

    return projection


# Call the main function.
if __name__ == '__main__':
    main()



'''
NOTES


youtube.com/watch?v=xECXZ3tyONo

# Creates an empty array with 3 elements.
array = np.empty(3)

# Creates an array from a list
list = [1, 2, 3]
array = np.array([list])

# Accesses one entry in an array.
array[0]


'''