import numpy as np

#многомерная матрица порядка _n и размерности _dim
def GetMM(_dim,_n):
  # n=2, dim=4
  dimentions=np.full_like(np.arange(_dim,dtype=int),_n) # -> [2 2 2 2]
  FM=np.arange(np.power(_n,_dim)) # -> [ 0  1  2  3  ... 12 13 14 15]
  return FM.reshape(dimentions)

#берем сечение
def GetSectionsMM(_MultyMat,_sk):
  # dim=4
  dim = len(_MultyMat.shape)
  # sk=[(0, 1), (1, 1)]  в 0 индексе фиксируем 1 в первом 1 остальные полностью 
  mask_list = [slice(None, None, None) for i in range(dim)]
  for i in range(len(_sk)):
    mask_list[_sk[i][0]]=_sk[i][1]
  mask_tuple = tuple(mask_list)
  return _MultyMat[mask_tuple]

#декартово произведение множеств _s1 и _s2
def decart(_s1,_s2):
  # decart([0,1],[0,1,2]) -> [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
  return [(a,b) for a in _s1 for b in _s2]

#декартово произведение множества множеств _s1 и _s2
def decart_second(_big_s1,_s2):
  #_big_s1=[(0, 0), (0, 1), (1, 0), (1, 1)]
  #_s2=[0,1]
  tmp=[[a,b] for a in _big_s1 for b in _s2]
  for i in range(len(tmp)):
    tmp[i][0]=list(tmp[i][0])
    tmp[i]=tuple(tmp[i][0]+[tmp[i][1]])
  return tmp

#получаем массив сечений по номерам индексов
def GetListSectionsMM(_MultyMat,_ind):
  #_ind=[1,2,3]
  n=_MultyMat.shape[0] # порядок матрицы
  res=[]
  s = [i for i in range(n)]
  if len(_ind) == 1:    
    for i in range(len(s)):
      res.append([])
      _sk=(_ind[0],i)
      res[i].append(_sk)
      res[i]=res[i]+[GetSectionsMM(_MultyMat,[_sk])]
  elif len(_ind) == 2:    
    all_pair=decart(s,s)
    for i in range(len(all_pair)):
      res.append([])
      _sk=[(_ind[0],all_pair[i][0]),(_ind[1],all_pair[i][1])]
      res[i].append(_sk)
      res[i]=res[i]+[GetSectionsMM(_MultyMat,_sk)]
  elif len(_ind) > 2:
    tmp_pair=decart(s,s)
    for x in range(2, len(_ind)):
      tmp_pair=decart_second(tmp_pair,s)
    for i in range(len(tmp_pair)):
      res.append([])
      _sk=[]
      for j in range(len(tmp_pair[i])):
        _sk.append((_ind[j],tmp_pair[i][j]))
      res[i].append(_sk)
      res[i]=res[i]+[GetSectionsMM(_MultyMat,_sk)]
  return res

#собрать многомерную матрицу по ее сечениям
def UniteSectionsMM(_sections,_ind_res,_n):
  C=GetMM(sum(_ind_res),_n)
  mask_list = [slice(None, None, None) for i in range(sum(_ind_res))]
  for i in range(len(_sections)):
    for j in range(len(_sections[i][0][0])):
      mask_list[_ind_res[0]+j]=_sections[i][0][0][j]
    mask_tuple=tuple(mask_list)    
    C[mask_tuple]=_sections[i][1]
  return C