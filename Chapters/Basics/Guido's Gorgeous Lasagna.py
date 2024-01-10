"""Functions used in preparing Guido's gorgeous lasagna.
 
Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
 
This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME = 40
def bake_time_remaining(minutes):
    """Calculate the bake time remaining.
    
    :param Elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    elapsed_bake_time = EXPECTED_BAKE_TIME - minutes
   
    return elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time with the equation - number_of_layers * 2
    Since one layer is set to take 2 minutes of prep.
    """
    preparation_time = number_of_layers * 2
    return preparation_time
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Total elapsed time in minutes equals the prep time in minutes + elapsed bake time
    """
    elapsed_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return elapsed_time
