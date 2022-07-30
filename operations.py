import numpy as np
from joblib import Parallel, delayed
import help

#λ μ свернутое произведение
def λμ_convolution_product_sequential(_λ,_μ,_A,_B):
  n=_A.shape[0]
  dim_A = len(_A.shape)
  dim_B = len(_B.shape)
  s_a=[i for i in range(dim_A-_λ-_μ,dim_A-_μ)]
  A_split_s=help.GetListSectionsMM(_A,s_a)
  ind_res=[dim_A-_λ-_μ,_λ,dim_B-_λ-_μ]
  s_b=[i for i in range(_μ,_μ+_λ)]
  B_split_s=help.GetListSectionsMM(_B,s_b)
  res=[]
  for i in range(len(B_split_s)):
    res.append([])
    _ind_s_list=[]
    for j in range (len(B_split_s[i][0])):
      _ind_s_list=_ind_s_list+[B_split_s[i][0][j][1]]
    _ind_s_tuple=tuple(_ind_s_list)
    res[i].append([_ind_s_tuple])
  tensordot=[np.tensordot(A_split_s[i][1],B_split_s[i][1], _μ) for i in range(len(B_split_s))]  
  for i in range(len(B_split_s)):
    res[i]=res[i]+[tensordot[i]]
  return help.UniteSectionsMM(res,ind_res,n)

def λμ_convolution_product_parallel(_λ,_μ,_A,_B):
  n=_A.shape[0]
  dim_A = len(_A.shape)
  dim_B = len(_B.shape)
  s_a=[i for i in range(dim_A-_λ-_μ,dim_A-_μ)]
  A_split_s=help.GetListSectionsMM(_A,s_a)
  ind_res=[dim_A-_λ-_μ,_λ,dim_B-_λ-_μ]
  s_b=[i for i in range(_μ,_μ+_λ)]
  B_split_s=help.GetListSectionsMM(_B,s_b)
  res=[]
  for i in range(len(B_split_s)):
    res.append([])
    _ind_s_list=[]
    for j in range (len(B_split_s[i][0])):
      _ind_s_list=_ind_s_list+[B_split_s[i][0][j][1]]
    _ind_s_tuple=tuple(_ind_s_list)
    res[i].append([_ind_s_tuple])
  tensordot=Parallel(n_jobs=n**_λ)(delayed(np.tensordot)(A_split_s[i][1],B_split_s[i][1], _μ) for i in range(len(B_split_s)))
  for i in range(len(B_split_s)):
    res[i]=res[i]+[tensordot[i]]
  return help.UniteSectionsMM(res,ind_res,n)

