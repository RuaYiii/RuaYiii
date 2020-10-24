import numpy
def nautual_relu(x): #x 是一个numpy 2d 向量
    assert len(x.shape)==2
    x=x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j]=max(x[i,j],0) #看样子是负数归零
    return x
def nautual_add(x,y):
    assert len(x.shape)==2  #依旧假设是2d向量
    assert y.shape==x.shape
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j] +=y[i,j]
    return x

    
    


