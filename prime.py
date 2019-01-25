import math
import time

start_time = time.time()
def prime():
    total = 0
    prime_num = [2]
    start=2
    end=1000
    p=range(start,end)

    for num in p:

        i = 2
        while i < num:
                                #a factor would never be larger than the sqrt of num
            if i > math.sqrt(num):
                prime_num.append(num)
                break
            if num%i == 0:
                break
            i+=1


    print "Prime Numbers: ",prime_num
    print "Number of primes found: ", len(prime_num)

    for i in prime_num:
        total +=  i
    print(total)
prime()




end_time = time.time()
t = end_time-start_time
if t > 60:
    t = t/60
    print ("It took %10.3f minutes to run this program." % t)
else:
    print ("It took %10.3f seconds to run this program." % t)