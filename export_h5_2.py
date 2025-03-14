import h5py
import numpy as np
from scipy.io import savemat

# 打开 HDF5 文件
with h5py.File('examples/inputs/model2019_face12.h5', 'r') as file:
    # 查看文件中的所有对象
    print(list(file.keys()))
    
    # 提取数据
    shape_model = file['catalog/MorphableModel/shape/model'][:]
    mean_shape = file['catalog/MorphableModel/shape/model/mean'][:]
    shape_pca_basis = file['catalog/MorphableModel/shape/model/pcaBasis'][:]
    shape_pca_variance = file['catalog/MorphableModel/shape/model/pcaVariance'][:]
    
    expression_model = file['catalog/MorphableModel/expression/model'][:]
    expression_pca_basis = file['catalog/MorphableModel/expression/model/pcaBasis'][:]
    expression_pca_variance = file['catalog/MorphableModel/expression/model/pcaVariance'][:]
    
    color_model = file['catalog/MorphableModel/color/model'][:]
    color_pca_basis = file['catalog/MorphableModel/color/model/pcaBasis'][:]
    color_pca_variance = file['catalog/MorphableModel/color/model/pcaVariance'][:]
    
    # 提取其它你需要的数据，例如纹理、表情等
    
    # 将数据保存在字典中，方便保存为 .mat 格式
    data = {
        'shape_model': shape_model,
        'mean_shape': mean_shape,
        'shape_pca_basis': shape_pca_basis,
        'shape_pca_variance': shape_pca_variance,
        'expression_model': expression_model,
        'expression_pca_basis': expression_pca_basis,
        'expression_pca_variance': expression_pca_variance,
        'color_model': color_model,
        'color_pca_basis': color_pca_basis,
        'color_pca_variance': color_pca_variance
    }
    
    # 保存为 .mat 文件
    savemat('examples/results/3dmm_model.mat', data)

print("3DMM data successfully converted to MAT format!")