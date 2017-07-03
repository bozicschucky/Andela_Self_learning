import time

def primenumbers(number):
    start = time.time()
    primes = set() # initialized empty set to store the values to be added to the set
    if type(number) == int and number > 0:
        for number in range(0, number + 1):
            if number > 1:
                for n in range(2, number): #
                    if number%n == 0: 
                        break # breaks if the number is not prime.
                else:
                    primes.add(number) # add prime number to the primes list
    else:
        return False

    return ("The prime numbers are " +str(primes) + ". The program ran for " + str(time.time()-start))

if __name__ == '__main__':
    #print prime_numbers(2)
    print primenumbers(5) # running time 4.48226928711e-05
    print primenumbers(10) # running time 1.50203704834e-05
    print primenumbers(100) # running time 0.000203132629395
    print primenumbers(500) # running time 0.00300407409668

	# the big O of the above function takes more time to print the prime numbers with an increase in the number of inputs in the function


""" The big O of the number basically follows n^2 since the loops are repeating and execute a given number of times.

so based on the inputs the big-O of the above function is n^2 keeping the constant steps fixed."""
