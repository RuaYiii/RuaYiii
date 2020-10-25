import numpy as np
def natural_relu(x): #x 是一个numpy 2d 向量
    '''线性整流函数（Rectified Linear Unit, ReLU）
    又称修正线性单元，是一种人工神经网络中常用的**激活函数**（activation function）
    通常指代以斜坡函数及其变种为代表的非线性函数。'''
    assert len(x.shape)==2
    x=x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j]=max(x[i,j],0) #看样子是负数归零
    return x
def natural_add(x,y):
    assert len(x.shape)==2  #依旧假设是2d向量
    assert y.shape==x.shape
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j] +=y[i,j]
    return x
def natural_vector_dot(x,y): #点积
    assert len(x.shape)==1
    assert len(y.shape)==1
    assert x.shape[0]==y.shape[0]
    z=0.
    for i in range(x.shape[0]):
        z+=x[i]*y[i]
    return z
def natural_matrix_vector_dot(x,y):
    assert len(x.shape)==2
    assert len(y.shape)==1
    assert x.shape[1]==y.shape[0]
    z= np.zeros(x.shape[0])
    for i in range(x.shape[0]):#ROW
        '''
        或者 z[i]=natural_vector_dot(x[i,:],y)
        '''
        for j in range(x.shape[1]):#C
            z[i]+=x[i,j]*y[j]
    return z
def natural_matrix_dot():  #这就是实际的矩阵乘法辣
    assert len(x.shape)==2
    assert len(y.shape)==2
    assert len(x.shape[1])==len(y.shape[0])
    z= np.zeros((x.shape[0],y.shape[1]))
    for i in range(x.shape[0]):
        for j in range(y.shape[1]):
            row_x=x[i,:]
            column_y=y[:,j]
            z[i,j]=natural_vector_dot(row_x,column_y)
    return z


    


