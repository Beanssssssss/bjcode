import numpy as np
#insert
a = np.array([10,20,30])
a = np.insert(a, 0, 5)

#delete

a = np.delete(a, 0)

#array generation functions

a = np.arange(3)

a = np.zeros((2, 4))
a = np.ones((1, 3))

a = np.linspace(0, 10, 5) #0부터 10까지 5개를 균등한 간격으

a = np.array([10, 20, 30])

np.mean(a)

a.mean()

np.average(a)

np.average(a, weights = [1, 1, 0])

np.cumsum(a) #[10, 30, 60]

x = np.array([10, 20, 30, 40])

x_min, x_min_idx = x.min(), x.argmin()
#argsort sort된 것 원래 idx

a = np.array([10, 20, 30])
b = np.array([-5, 25])
np.searchsorted(a, b)
# b가 어디에 들어가야 sort되는지 알려준
d = np.arange(1, 7, 1)
e = d.reshape(2, 3) # 2차원 배열로 변
f = np.linspace(1, 10, 10).reshape(2, 5)
a = np.array([[1, 2], [3, 4]])
np.repeat(a, 2, axis = 0)
np.repeat(a, 2, axis = 1)
np.repeat(a, [1, 2], axis = 0) #첫번째가 1번반복, 두번째거 2번 반
a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])
np.concatenate((a, b), axis = 1)
#vstack(vertical로 스택) , hstack(가로방향으로 스택)
np.hsplit(a, 3) 
b = np.vsplit(a, 2)
#transpose 가로세로 바꾸
#2차원 -> 1치원 ravel(order = 'C' or 'F'), reshape(-1), flatten()
#squeeze도 가능 
a1 = np.array([1, 2, 3])
b1 = np.array([4, 5, 6])
#idea1
a2 = a1[:,np.newaxis]
b2 = b1[:,np.newaxis]
#idea2
np.vstack((a1, b1)).transpose()
#idea3
np.hstack((a1, b1)).reshape((2, 3)).treanspose()
a = np.array([10, 20, 30])
b = a#이건 참조
#shallow 데이터는 공유 , shape는 달라도 가능
a = np.array([10, 20, 30])
b = a.view()
b is a
#깊은 복사 
a = np.array([10, 20, 30 ,40])
b = a.copy()
#logic function
a = np.array([0, 1, 2])
a.all()#모든 값이 참인지
a.any()#하나라도 참이 있는지
a.nonzero()#0 아닌값
b = np.where(a > 0) #index알려줌
a = np.array([1, 2, 3, 4, 5])
a[:]
m1 = np.array([[100, 101, 102], [103, 104, 105]])
m1[0, 2] #이런식도 가
m1[0, :]
m1[: , 1]
m1[np.nonzero(m1 == 100)]
#image
import numpy as np

IMAGE = np.array([[255, 0, 255], [255, 0, 255], [255, 0, 255]])
idx = np.where(IMAGE ==  255)
IMAGE[idx] = 0
#liner algebra
N = np.array([[10, 20], [30, 40]])
M = np.array([[1, 2], [3, 4]])
a = np.zeros((3, 3))
b = np.ones((3, 3))

#함수활용
def f(x, y):
    return x * y
b = np.fromfunction(f, (5, 4), dtype = int)
#set
a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5])
np.setdiff1d(a, b)
np.random.randint(100)
np.randon.rand(5) 






