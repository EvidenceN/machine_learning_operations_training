## STEPS TO COMPLETE ##
# 1. import logging
# 2. set up config file for logging called `results.log`
# 3. add try except with logging for success or error
#    in relation to checking the types of a and b
# 4. check to see that log is created and populated correctly
#    should have error for first function and success for
#    the second
# 5. use pylint and autopep8 to make changes
#    and receive 10/10 pep8 score

'''
Logging exercise example
'''
import logging

logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')


def sum_vals(first_val, second_val):
    '''
    Args:
        first_val: (int)
        second_val: (int)
    Return:
        first_val + second_val (int)
    '''
    try:
        check_val = first_val + 1
        print("check_val type: {}".format(check_val))
        logging.info("Summing first_val + second_val: SUCCESS")
        return first_val + second_val
    except TypeError:
        logging.error("first_val and second_val should be integers.")


if __name__ == "__main__":
    sum_vals(4, 5)
    sum_vals('no', 'way')
