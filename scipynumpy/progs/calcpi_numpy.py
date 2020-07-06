import numpy as np
import time

def main():
    # No of terms in the series
    noofterms = 1000000
    # Calculate the denominator.
    # First few terms are 1,3,5,7 ...
    # den is short for denominator
    den  = np.linspace(1,noofterms*2,noofterms)
    # Calculate the numerator.
    # The first few terms are 1, -1, 1, -1 ...
    # num is short for numerator
    num = np.ones(noofterms)
    for i in range(1,noofterms):
        num[i] = pow(-1,i)
    # Find the ratio and sum all the fractions
    # to obtain pi value
    # Start the clock
    t1 = time.process_time()
    pi_value =  sum(num/den)*4.0
    print("pi_value is: %f" % pi_value)
    t2 = time.process_time()
    # Determine the time for computation
    timetaken = t2-t1
    print("Time taken is: %f seconds" % timetaken)

if __name__ == '__main__':
    main()
