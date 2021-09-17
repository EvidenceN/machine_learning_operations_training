import logging

# Logging levels "info, warning, error"
logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    # try to return the fraction but if the denominator is zero
    # catch the error and return a string saying: 
    # "denominator cannot be zero"
    
    try:
        fraction_val = numerator/denominator
        return fraction_val
    except ZeroDivisionError:
        print("You can't divide by zero")
    

def num_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    '''
    # try to split based on spaces and return num of words
    # but if text isnt a string return "text argument must be a string"
    
    try:
        num_words = len(text.split())
        return num_words
    except (SyntaxError, AttributeError):
        return "text argument must be a string"
    


