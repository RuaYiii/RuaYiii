import numpy
def nautual_relu(x):
#x 是一个numpy 2d 向量
    assert len(x.shape)==2:
    x=x.copy()
    for i range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j]=max(x[i,j],0) #看样子是负数归零
    return x
    

