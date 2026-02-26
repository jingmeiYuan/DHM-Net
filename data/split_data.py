import os, shutil, random
import numpy as np

# 设置随机种子保证结果可复现
random.seed(0)

# 设置验证集比例 20% (训练集自动为 80%)
val_size = 0.2
postfix = 'jpg'

# 原始数据路径
imgpath = r'D:\YOLO12.22\ultralytics-yolo11-20251122\ultralytics-yolo11-main\data\images'
txtpath = r'D:\YOLO12.22\ultralytics-yolo11-20251122\ultralytics-yolo11-main\data\labels'

# 创建文件夹 (仅 Train 和 Val)
os.makedirs('images/train', exist_ok=True)
os.makedirs('images/val', exist_ok=True)
os.makedirs('labels/train', exist_ok=True)
os.makedirs('labels/val', exist_ok=True)

# 获取所有txt文件列表
listdir = np.array([i for i in os.listdir(txtpath) if 'txt' in i])
random.shuffle(listdir)

# 计算训练集数量
num_train = int(len(listdir) * (1 - val_size))

# 切分数据集 (8:2)
train = listdir[:num_train]
val = listdir[num_train:]

print(f'Total images: {len(listdir)}')
print(f'Train set size: {len(train)}')
print(f'Val set size: {len(val)}')

# 复制训练集
print("正在复制训练集...")
for i in train:
    # 复制图片
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'images/train/{}.{}'.format(i[:-4], postfix))
    # 复制标签
    shutil.copy('{}/{}'.format(txtpath, i), 'labels/train/{}'.format(i))

# 复制验证集
print("正在复制验证集...")
for i in val:
    # 复制图片
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'images/val/{}.{}'.format(i[:-4], postfix))
    # 复制标签
    shutil.copy('{}/{}'.format(txtpath, i), 'labels/val/{}'.format(i))

print("数据集划分完成！")