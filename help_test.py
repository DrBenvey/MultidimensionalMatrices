import help

class Test:
  def __init__(self, n, dim):
    self.n = n # Порядок многомерной матрицы
    self.dim = dim # Размерность многомерной матрицы

  def TestMM(self):
    MultyMat=help.GetMM(self.dim,self.n) # многомерная матрица
    print('вывести всю матрицу',MultyMat,sep='\n')
    print('вывести элемент матрицы',MultyMat[0,1,1,0],sep='\n')
  
  def SectionsMM(self):
    MultyMat=help.GetMM(self.dim,self.n) # многомерная матрица
    print('вывести сечение',MultyMat[0:,1,1,0:],sep='\n')
    print('то же самое но покрасивее',MultyMat[(slice(None, None, None), 1, 1, slice(None, None, None))],sep='\n')
    print('то же самое но программно',help.GetSectionsMM(MultyMat,[(0, 0), (1, 0)]),sep='\n')
    print('список сечений по индексу 0X00',help.GetListSectionsMM(MultyMat,[1]),sep='\n')
    print('список сечений по индексу XX00',help.GetListSectionsMM(MultyMat,[0,1]),sep='\n')
    print('список сечений по индексу XXX0',help.GetListSectionsMM(MultyMat,[0,1,2]),sep='\n')