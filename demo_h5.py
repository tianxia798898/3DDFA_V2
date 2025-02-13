import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 打开HDF5文件
file_path = 'examples/inputs/model2019_face12.h5'  # 请替换为你的H5文件路径
with h5py.File(file_path, 'r') as f:
    # 获取顶点数据（从 'shape/model/mean' 路径获取）
    vertices = f['shape/model/mean'][:]
    
    # 获取面数据（从 'shape/representer/cells' 路径获取）
    faces = f['shape/representer/cells'][:]

# 检查顶点数据的形状
print(f"Vertices shape: {vertices.shape}")  # 输出形状，如 (n, 3)，n为顶点数量

# 创建3D图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 可视化顶点
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], s=1)

# 假设 faces 是一个索引数组，表示面片的顶点索引
# 每个face是一个顶点的索引
for face in faces:
    # 获取面对应的顶点坐标
    x = vertices[face, 0]
    y = vertices[face, 1]
    z = vertices[face, 2]
    # 绘制三角形面
    ax.plot_trisurf(x, y, z, color='gray', linewidth=0.2)

# 显示3D图形
plt.show()