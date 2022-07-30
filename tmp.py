from joblib import Parallel, delayed
import numpy as np
import time



def some(i,A,B):
   return A.dot(A)+i*B

def test():

   proc=4
   n=2000
   dim=2

   dimentions=np.full_like(np.arange(dim,dtype=int),n)
   A=np.arange(np.power(n,dim)).reshape(dimentions)
   B=np.eye(n, dtype=int)

   start_time = time.time()
   res1=[some(i) for i in range(1,5)]
   end_time = time.time()
   print('time one by one (s):',end_time -start_time,sep='\t')

   start_time = time.time()
   Parallel(n_jobs=proc)(delayed(some)(i,A,B) for i in range(1,5))
   end_time = time.time()
   print('time paralel 4 proc (s):',end_time -start_time,sep='\t')

print(2**3)




