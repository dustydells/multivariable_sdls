'''
Time worked: 5 hr, 2 mins
+ 35 mins research




helpful article that actually mentions integration
https://www.kdnuggets.com/2020/11/essential-math-data-science-integrals-area-under-curve.html
'''

import scipy.integrate as integrate
from scipy.integrate import quad, dblquad
import scipy.special as special
import parser


def main():
    # try: 

        # Print the menu and ask for user input.
        option = None
        options = ['Single quadratic integral', 'Double integral of f(x, y) = xy', 'quit']
        while option != options.index('quit'):
            print_menu(options)
            option = int(input('Enter the number of the desired integral: ')) - 1

            # BASIC BLAND BOI INTEGRAL (quadratic function)
            if option == options.index('Single quadratic integral'):

                lower_bound = float(input('Enter the lower bound: '))
                upper_bound = float(input('Enter the upper bound: '))

                print('This equation is done in the form ax^2 + b.\n')

                a = float(input('Enter a value for a: '))
                b = float(input('Enter a value for b: '))


                quad_result = compute_quad_integral(upper_bound, lower_bound, a=2, b=1)

                # Since result is a tuple with two values, separate them.
                estimated_value = quad_result[0]
                upper_error_bound = quad_result[1]

                print(f'\nQuadratic integral: \nEstimated value: {estimated_value}\nwith upper bound on error of {upper_error_bound}')


            # DOUBLE INTEGRAL
            elif option == options.index('Double integral of f(x, y) = xy'):
                equation = None

                y_lower_bound = float(input('Enter the lower bound for y: '))
                y_upper_bound = float(input('Enter the upper bound for y: '))
                x_lower_bound = float(input('Enter the lower bound for x: '))
                x_upper_bound = float(input('Enter the upper bound for x: '))

                # Call double integral function to compute an integral to the equation xy
                dbl_result = compute_dbl_integral(equation, y_lower_bound, y_upper_bound, x_lower_bound, x_upper_bound)

                # Since result is a tuple with two values, separate them.
                estimated_value = dbl_result[0]
                upper_error_bound = dbl_result[1]

                print(f'\nDouble integral: \nEstimated value: {estimated_value}\nwith upper bound on error of {upper_error_bound}')
    
    # except ValueError as value_err:
    #     print(type(ValueError), 'Please input a valid number.')


    # # FANCY INTEGRAL
    # # Call the integral computation function
    # result = compute_fancy_integral()

    # # Since result is a tuple with two values, separate them.
    # estimated_value = result[0]
    # upper_error_bound = result[1]
    
    # # Return results.
    # print(f'\nFancy integral: \nEstimated value: {estimated_value}\nwith upper bound on error of {upper_error_bound}')


def compute_quad_integral(upper_bound, lower_bound, a, b):
    '''
    Computes an integral.
    Parameters:

    Returns: 
        A tuple - (estimated value, upper bound of error)

    '''
    # Make the integrand so it can be used in the quad function.
    def integrand(x, a, b):
        return a * x**2 + b


    integral = quad(integrand, lower_bound, upper_bound, args = (a, b))

    return integral


def compute_fancy_integral():
    '''
    Computes an indefinite integral I think?? ?
    Parameters:
        none
    Returns:
        A tuple - (estimated value, upper bound of error)
    '''

    result = quad(lambda x: special.jv(2.5,x), 0, 4.5)
    
    return result


def compute_dbl_integral(equation, y_lower_bound, y_upper_bound, x_lower_bound, x_upper_bound):
    '''
    Computes a double integral:
    Parameters:
        equation:
        y_lower_bound: lower bound in terms of y.
        y_upper_bound: upper bound in terms of y.
        x_lower_bound: lower bound in terms of x.
        x_upper_bound: upper bound in terms of x.
    Returns:
        A tuple - (estimated value, upper bound of error)

    '''
    # Make the integrand so it can be used in the quad function.
    def integrand(x, y):
        return x*y
        # Grab equation from the user
        # equation_string = input('Enter * for xy, enter / for x/y.')

        # equation_list = equation_string.split(' ')

        # # Make a list of floats, and a list of operators. Then cal the lists into a function that parses the function. And then put it in as the integrand.

        # for i, _ in enumerate(equation_list):
            # next_term = equation_list[i+1]
            # if _ == '*':
            #     equation = x*y # multiply it to the other things
            # if _ == '/':
            #     equation = x/y
        #     if _ == '+':
        #         equation += next_term

        # code = parser.expr(equation_string).compile()


        # return equation

    # How to do this where you can switch out the equation and send it in as a parameter? 
    result = dblquad(lambda x, y: integrand(x, y), y_lower_bound, y_upper_bound, lambda x: x_lower_bound, lambda x: x_upper_bound)

    return result


def print_menu(options):
    '''
    Print the menu options. 
    '''
    print('\n MENU\n')
    for i in range(len(options)):
        print(f'{i+1}. {options[i]}')
    print()


main()