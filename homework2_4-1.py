# The formula used for Computing is from https://en.wikipedia.org/wiki/Madelung_constant

import numpy as np
import matplotlib.pyplot as plt

def judge_vertex(r_array, n, a):
    if (r_array[1] == 0 and r_array[2] == 0 and r_array[3] == 0) or\
       (r_array[1] == n*a and r_array[2] == 0 and r_array[3] == 0) or\
       (r_array[1] == n*a and r_array[2] == n*a and r_array[3] == 0) or\
       (r_array[1] == 0 and r_array[2] == n*a and r_array[3] == 0) or\
       (r_array[1] == 0 and r_array[2] == 0 and r_array[3] == n*a) or\
       (r_array[1] == n*a and r_array[2] == 0 and r_array[3] == n*a) or\
       (r_array[1] == n*a and r_array[2] == n*a and r_array[3] == n*a) or\
       (r_array[1] == 0 and r_array[2] == n*a and r_array[3] == n*a):
           return True

def judge_edge(r_array, n, a):
    def judge_edge(r_array, n, a):
        if (r_array[1] == 0 and r_array[3] == 0 and (r_array[2] != 0 and r_array[2] != n*a)) or \
           (r_array[1] == 0 and r_array[3] == n*a and (r_array[2] != 0 and r_array[2] != n*a)) or \
           (r_array[1] == n*a and r_array[3] == 0 and (r_array[2] != 0 and r_array[2] != n*a)) or\
           (r_array[1] == n*a and r_array[3] == n*a and (r_array[2] != 0 and r_array[2] != n*a)) or\
           (r_array[1] == 0 and r_array[2] == 0 and (r_array[3] != 0 and r_array[3] != n*a)) or\
           (r_array[1] == 0 and r_array[2] == n*a and (r_array[3] != 0 and r_array[3] != n*a)) or\
           (r_array[1] == n*a and r_array[2] == 0 and (r_array[3] != 0 and r_array[3] != n*a)) or\
           (r_array[1] == n*a and r_array[2] == n*a and (r_array[3] != 0 and r_array[3] != n*a)) or\
           (r_array[2] == 0 and r_array[3] == 0 and (r_array[1] != 0 and r_array[1] != n*a)) or\
           (r_array[2] == n*a and r_array[3] == 0 and (r_array[1] != 0 and r_array[1] != n*a)) or\
           (r_array[2] == 0 and r_array[3] == n*a and (r_array[1] != 0 and r_array[1] != n*a)) or\
           (r_array[2] == n*a and r_array[3] == n*a and (r_array[1] != 0 and r_array[1] != n*a)):
               return True

def judge_face(r_array, n, a):
    if (r_array[1] == 0 and r_array[2] != 0 and r_array[2] != n*a and r_array[3] != 0 and r_array[3] != n*a) or\
       (r_array[1] == n*a and r_array[2] != 0 and r_array[2] != n*a and r_array[3] != 0 and r_array[3] != n*a) or\
       (r_array[3] == 0 and r_array[2] != 0 and r_array[2] != n*a and r_array[1] != 0 and r_array[1] != n*a) or\
       (r_array[3] == n*a and r_array[2] != 0 and r_array[2] != n*a and r_array[1] != 0 and r_array[1] != n*a) or\
       (r_array[2] == 0 and r_array[1] != 0 and r_array[1] != n*a and r_array[3] != 0 and r_array[3] != n*a) or\
       (r_array[2] == n*a and r_array[1] != 0 and r_array[1] != n*a and r_array[3] != 0 and r_array[3] != n*a):
           return True

def cal_in(e, r):
    result = e / r
    return result

def cal_surf_vertex(e, r):
    result = 1/8 * e / r
    return result
    
def cal_surf_face(e, r):
    result = 1/2 * e / r
    return result
    
def cal_surf_edge(e, r):
    result = 1/4 * e / r
    return result

def distance(x1, y1, z1, x2, y2, z2):
    result = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    return result

def check_repeat_and_self(wait_check_array, complete_array, n_d, r0):
    flag = True
    for i in np.arange(n_d):
        if (wait_check_array==complete_array[i]).all() or (wait_check_array==r0).all():
            flag = False

    return flag


# a = 14.24
a = 1
n = 11 #定义的n应为奇数
# r0 = np.sqrt(3)/4 * a

# 对不同晶体结构进行单胞初始化, 每个离子一个5维矩阵, (电荷,x,y,z)
'''
## no.1，K3C60晶体中，K(1)离子为中心的单胞，表面电荷-2
r1 = np.array([-3, -1/2*a, 1/2*a, 1/2*a])
r2 = np.array([1, -1/2*a, 0, 1/2*a])
r3 = np.array([-3, -1/2*a, -1/2*a, 1/2*a])
r4 = np.array([1, 0, 1/2*a, 1/2*a])
r5 = np.array([-3, 0, 0, 1/2*a])
r6 = np.array([1, 0, -1/2*a, 1/2*a])
r7 = np.array([-3, 1/2*a, 1/2*a, 1/2*a])
r8 = np.array([1, 1/2*a, 0, 1/2*a])
r9 = np.array([-3, 1/2*a, -1/2*a, 1/2*a])
r10 = np.array([1, -1/4*a, 1/4*a, 1/4*a])
r11 = np.array([1, -1/4*a, -1/4*a, 1/4*a])
r12 = np.array([1, 1/4*a, 1/4*a, 1/4*a])
r13 = np.array([1, 1/4*a, -1/4*a, 1/4*a])
r14 = np.array([1, -1/2*a, 1/2*a, 0])
r15 = np.array([-3, -1/2*a, 0, 0])
r16 = np.array([1, -1/2*a, -1/2*a, 0])
r17 = np.array([-3, 0, 1/2*a, 0])
r18 = np.array([1, 0, 0, 0])
r19 = np.array([-3, 0, -1/2*a, 0])
r20 = np.array([1, 1/2*a, 1/2*a, 0])
r21 = np.array([-3, 1/2*a, 0, 0])
r22 = np.array([1, 1/2*a, -1/2*a, 0])
r23 = np.array([1, -1/4*a, 1/4*a, -1/4*a])
r24 = np.array([1, -1/4*a, -1/4*a, -1/4*a])
r25 = np.array([1, 1/4*a, 1/4*a, -1/4*a])
r26 = np.array([1, 1/4*a, -1/4*a, -1/4*a])
r27 = np.array([-3, -1/2*a, 1/2*a, -1/2*a])
r28 = np.array([1, -1/2*a, 0, -1/2*a])
r29 = np.array([-3, -1/2*a, -1/2*a, -1/2*a])
r30 = np.array([1, 0, 1/2*a, -1/2*a])
r31 = np.array([-3, 0, 0, -1/2*a])
r32 = np.array([1, 0, -1/2*a, -1/2*a])
r33 = np.array([-3, 1/2*a, 1/2*a, -1/2*a])
r34 = np.array([1, 1/2*a, 0, -1/2*a])
r35 = np.array([-3, 1/2*a, -1/2*a, -1/2*a])
'''

## no.2，K3C60晶体中，K(2)离子为中心的单胞, 表面电荷+2
r1 = np.array([1, -1/2*a, 1/2*a, 1/2*a])
r2 = np.array([1, -1/2*a, 0, 1/2*a])
r3 = np.array([1, -1/2*a, -1/2*a, 1/2*a])
r4 = np.array([1, 0, 1/2*a, 1/2*a])
r5 = np.array([1, 0, 0, 1/2*a])
r6 = np.array([1, 0, -1/2*a, 1/2*a])
r7 = np.array([1, 1/2*a, 1/2*a, 1/2*a])
r8 = np.array([1, 1/2*a, 0, 1/2*a])
r9 = np.array([1, 1/2*a, -1/2*a, 1/2*a])
r10 = np.array([1, -1/4*a, 1/4*a, 1/4*a])
r11 = np.array([-3, -1/4*a, -1/4*a, 1/4*a])
r12 = np.array([-3, 1/4*a, 1/4*a, 1/4*a])
r13 = np.array([1, 1/4*a, -1/4*a, 1/4*a])
r14 = np.array([1, -1/2*a, 1/2*a, 0])
r15 = np.array([1, -1/2*a, 0, 0])
r16 = np.array([1, -1/2*a, -1/2*a, 0])
r17 = np.array([1, 0, 1/2*a, 0])
r18 = np.array([1, 0, 0, 0])
r19 = np.array([1, 0, -1/2*a, 0])
r20 = np.array([1, 1/2*a, 1/2*a, 0])
r21 = np.array([1, 1/2*a, 0, 0])
r22 = np.array([1, 1/2*a, -1/2*a, 0])
r23 = np.array([-3, -1/4*a, 1/4*a, -1/4*a])
r24 = np.array([1, -1/4*a, -1/4*a, -1/4*a])
r25 = np.array([1, 1/4*a, 1/4*a, -1/4*a])
r26 = np.array([-3, 1/4*a, -1/4*a, -1/4*a])
r27 = np.array([1, -1/2*a, 1/2*a, -1/2*a])
r28 = np.array([1, -1/2*a, 0, -1/2*a])
r29 = np.array([1, -1/2*a, -1/2*a, -1/2*a])
r30 = np.array([1, 0, 1/2*a, -1/2*a])
r31 = np.array([1, 0, 0, -1/2*a])
r32 = np.array([1, 0, -1/2*a, -1/2*a])
r33 = np.array([1, 1/2*a, 1/2*a, -1/2*a])
r34 = np.array([1, 1/2*a, 0, -1/2*a])
r35 = np.array([1, 1/2*a, -1/2*a, -1/2*a])


## 定义待计算的离子在晶胞中的位置，一般换了晶胞就要重新定义
### K(1)
'''
### in crystal no.1
e0 = 1
h0 = 0
k0 = 0
l0 = 0
'''

### in crystal no.2
e0 = 1
h0 = -1/4 * a
k0 = 1/4 * a
l0 = 1/4 * a

r0 = np.array([e0, h0, k0, l0])

r_single = np.array([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13\
                   , r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24\
                   , r25, r26, r27, r28, r29, r30, r31, r32, r33, r34, r35])

#相对坐标变换
r_origin = np.array([0, n/2*a, n/2*a, n/2*a])
'''
r_new = np.zeros((35, 4))
for i in np.arange(35):
    r_new[i] = r_single[i] + r_origin
'''
r0 = r0 + r_origin

#print(r0)
#拓展构建完整晶胞
r_all = np.array([[100, 100, 100, 100]])
for i in np.arange(n):
    for j in np.arange(n):
        for k in np.arange(n):
            r_origin = np.array([0, (2*i+1)/2*a, (2*j+1)/2*a, (2*k+1)/2*a])
            r_new = np.zeros((35, 4))
            for m in np.arange(35):
                r_new[m] = r_single[m] + r_origin
            for l in np.arange(np.shape(r_single)[0]):
                r_tmp = r_new[l]
                n_tmp = np.shape(r_all)[0]
                if check_repeat_and_self(r_tmp, r_all, n_tmp, r0):
                    #print(r_tmp, 'Accepted')
                    r_all = np.row_stack((r_all, r_tmp))
r_all = np.delete(r_all, 0, 0)
np.set_printoptions(threshold=np.nan)
#print(r_all)
# 更具全晶胞模型，求解马德隆常数
ion_number = np.shape(r_all)[0]
alpha = 0

for i in np.arange(ion_number):
    dis = distance(r0[1], r0[2], r0[3], r_all[i, 1], r_all[i, 2], r_all[i, 3])
    if judge_vertex(r_all[i], n, a):
        alpha = alpha + r0[0] * cal_surf_vertex(r_all[i, 0], dis)
    elif judge_edge(r_all[i], n, a):
        alpha = alpha + r0[0] * cal_surf_edge(r_all[i, 0], dis)
    elif judge_face(r_all[i], n, a):
        alpha = alpha + r0[0] * cal_surf_face(r_all[i, 0], dis)
    else:
        alpha = alpha + r0[0] * cal_in(r_all[i, 0], dis)

# 再取一个晶胞



print('alpha = %.4f' % alpha)

