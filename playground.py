# break = Abort mission, stop the loop completely
# continue = Skip this step of the loop, but continue the loop
# pass = Be pass-ive and do nothing

import numpy as np
lll = [1, 2]

array = np.full((5,5), 'A')
print(array)
print(array[lll])

a = [[False,False,False],
    [False,False,False],
    [False,False,False],
    [False,False,False]]

print("HAaaaaaaaa", a[1][2])

a[1][2] = True

print(a)




"""
  01234567890123456789
0 %%%%%%%%%%%%%%%%%%%%
1 %--------------%---%  
2 %-%%-%%-%%-%%-%%-%-%  
3 %--------P-------%-%  
4 %%%%%%%%%%%%%%%%%%-%  
5 %.-----------------%  
6 %%%%%%%%%%%%%%%%%%%%  
"""


"""
3 9  
5 1  
7 20  
%%%%%%%%%%%%%%%%%%%%
%--------------%---%  
%-%%-%%-%%-%%-%%-%-%  
%--------P-------%-%  
%%%%%%%%%%%%%%%%%%-%  
%.-----------------%  
%%%%%%%%%%%%%%%%%%%% 
"""