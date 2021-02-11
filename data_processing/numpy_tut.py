import numpy as np

def create_np_array():
    a = np.array([2,23,4], dtype=np.int64)
    # dtype can be np.int, np.int64, np.int32, np.float, np.float32 and etc
    print(f"1D array: {a}, dtype is {a.dtype}")

    a = np.array([[2,23,4],[2,32,4]])  # 2d 矩阵 2行3列
    print(f"2D array: \n{a}")

    a = np.zeros((3,4)) # 数据全为0，3行4列
    print(f"2D 3*4 all zeros array: \n{a}")

    a = np.ones((3,4),dtype = np.int)
    print(f"2D 3*4 all ones array: \n{a}")

    a = np.empty((3,4)) # 数据为empty，3行4列, each value is extremely close to zero 
    print(f"2D 3*4 all empty array: \n{a}")

    # Using arange to create continurous array
    a = np.arange(10,20,2)
    print(f"using arange with 1D array, from 10 to 20 with interval 2: \n{a}")

    a = np.arange(12).reshape((3,4))
    print(f"arange and reshape: \n{a}")

    a = np.linspace(1,10,20)    # 开始端1，结束端10，且分割成20个数据，生成线段
    print(f"linspace array: \n{a}")


if __name__ == "__main__":
    create_np_array()