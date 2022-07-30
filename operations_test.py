import operations
import help
import time
import matplotlib.pyplot as plt
import numpy as np

class SpeedTest:
    def Testλμ_convolution_product_sequential(self):
        #11 ок но долго
        x_axis = np.arange(start=5, stop=9, step=1)
        y_axis_numpy = [0] * x_axis.shape[0]
        λ=2;μ=4
        dim_a=7;dim_b=9
        print('dim_a: ', dim_a,'dim_b: ',dim_b, sep='\t')
        print('(', λ,',',4,')(A*B)', sep='')
        for i in range(len(x_axis)):
            n=x_axis[i]
            A=help.GetMM(dim_a,n)
            B=help.GetMM(dim_b,n)
            start_time = time.time()
            C=operations.λμ_convolution_product_sequential(λ,μ,A,B)
            end_time = time.time()
            y_axis_numpy[i]=end_time - start_time
            print('n=',n,' time(s): ',y_axis_numpy[i],sep='')
        data = {'NumPy':y_axis_numpy}
        plt.plot(x_axis,y_axis_numpy,color='b',linestyle='--')
        plt.scatter(x_axis,y_axis_numpy,color='b')
        plt.legend(data, loc=2)
        plt.grid(True)
        plt.xlabel('N', fontsize=12, color='blue')
        plt.ylabel('Time, s', fontsize=12, color='blue')
        plt.show()

class Test:
    def __init__(self):
        self.n = 2 # Порядок многомерной матрицы
        self.dim_a = 4 # Размерность многомерной матрицы A
        self.dim_b = 3 # Размерность многомерной матрицы B
        self.λ = 2
        self.μ = 1
        self.A=help.GetMM(self.dim_a,self.n)
        self.A[0][0][0][0]=1;self.A[0][1][0][0]=3
        self.A[0][0][0][1]=2;self.A[0][1][0][1]=2
        self.A[0][0][1][0]=0;self.A[0][1][1][0]=4
        self.A[0][0][1][1]=-1;self.A[0][1][1][1]=1
        self.A[1][0][0][0]=-2;self.A[1][1][0][0]=0
        self.A[1][0][0][1]=0;self.A[1][1][0][1]=1
        self.A[1][0][1][0]=1;self.A[1][1][1][0]=2
        self.A[1][0][1][1]=3;self.A[1][1][1][1]=1
        self.B=help.GetMM(self.dim_b,self.n)
        self.B[0][0][0]=1;self.B[1][0][0]=1
        self.B[0][0][1]=2;self.B[1][0][1]=3
        self.B[0][1][0]=-2;self.B[1][1][0]=4
        self.B[0][1][1]=0;self.B[1][1][1]=1
        self.H=help.GetMM(3,2) # рузультат (2,1) свернутого произведения вычисленного на бумаге
        self.H[0][0][0]=3;self.H[1][0][0]=-2
        self.H[0][0][1]=-3;self.H[1][0][1]=11
        self.H[0][1][0]=2;self.H[1][1][0]=4
        self.H[0][1][1]=1;self.H[1][1][1]=1

    def Testλμ_convolution_product_sequential(self):
        C=operations.λμ_convolution_product_sequential(self.λ,self.μ,self.A,self.B)
        print('Проверка', self.H==C, sep='\n')
  
    def Testλμ_convolution_product_parallel(self):
        C=operations.λμ_convolution_product_parallel(self.λ,self.μ,self.A,self.B)
        print('Проверка', self.H==C, sep='\n')