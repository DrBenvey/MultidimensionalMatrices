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

    def Testλμ_convolution_product_sequential_vs_parallel(self):
        λ=3;μ=5;n=2;ν=9
        print('λ=', λ,'μ=',μ,'n=',n,'ν=',ν, sep=' ')
        l_indexes=np.arange(start=9, stop=17, step=1)
        y_axis_parallel = [0] * len(l_indexes)
        y_axis_sequential = [0] * len(l_indexes)
        dim_b=λ+μ+ν
        B=help.GetMM(dim_b,n)
        for i in range(len(l_indexes)):
            k=l_indexes[i]
            dim_a=λ+μ+k
            A=help.GetMM(dim_a,n)
            start_time = time.time()
            C1=operations.λμ_convolution_product_parallel(λ,μ,A,B)
            end_time = time.time()
            y_axis_parallel[i]=end_time - start_time
            print('k=',k,'dim_a=',dim_a,'time parallel (s): ',y_axis_parallel[i],sep=' ')
            start_time = time.time()
            C2=operations.λμ_convolution_product_sequential(λ,μ,A,B)
            end_time = time.time()
            y_axis_sequential[i]=end_time - start_time
            print('k=',k,'dim_a=',dim_a,'time sequential (s): ',y_axis_sequential[i],sep=' ')
        data = {'NumPy_parallel':y_axis_parallel,'NumPy_sequential':y_axis_sequential}
        plt.plot(l_indexes,y_axis_parallel,color='r')
        plt.scatter(l_indexes,y_axis_parallel,color='r')
        plt.plot(l_indexes,y_axis_sequential,color='b',linestyle='--')
        plt.scatter(l_indexes,y_axis_sequential,color='b')
        plt.legend(data, loc=2)
        plt.grid(True)
        plt.xlabel('N', fontsize=12, color='blue')
        plt.ylabel('Time, s', fontsize=12, color='blue')
        plt.show()

    
    def Testλμ_convolution_product_parallel(self):
        λ=3;μ=5;n=2;ν=9
        print('λ=', λ,'μ=',μ,'n=',n,'ν=',ν, sep=' ')
        l_indexes=np.arange(start=9, stop=17, step=1)
        y_axis_numpy = [0] * len(l_indexes)
        dim_b=λ+μ+ν
        B=help.GetMM(dim_b,n)
        for i in range(len(l_indexes)):
            k=l_indexes[i]
            dim_a=λ+μ+k
            A=help.GetMM(dim_a,n)
            start_time = time.time()
            C=operations.λμ_convolution_product_parallel(λ,μ,A,B)
            end_time = time.time()
            y_axis_numpy[i]=end_time - start_time
            print('k=',k,'dim_a=',dim_a,'time(s): ',y_axis_numpy[i],sep=' ')
        data = {'NumPy':y_axis_numpy}
        plt.plot(l_indexes,y_axis_numpy,color='b',linestyle='--')
        plt.scatter(l_indexes,y_axis_numpy,color='b')
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