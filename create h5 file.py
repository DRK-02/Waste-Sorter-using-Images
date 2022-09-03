#========================== Part 1: Prepare Data ==========================
from random import shuffle
import glob

shuffle_data = True  # shuffle the addresses

hdf5_path = 'C:/Users/Admin/Desktop/Dhruv/Beta/M/m/BTech. Engineering/AI Club/Waste-Sorter-using-Images/images.hdf5'  # file path for the created .hdf5 file

dataset_path = 'C:/Users/Admin/Desktop/Dhruv/Beta/M/m/BTech. Engineering/AI Club/Waste-Sorter-using-Images/Enhanced Dataset/*.jpg' # the original data path

# get all the image paths
addrs = glob.glob(dataset_path)

# label the data as 0 = paper, 1 = glass, plastic = 2, metal = 3
labels = []

for addr in addrs:
    if 'paper' in addr:
        labels.append(0)

    elif 'glass' in addr:
        labels.append(1)

    elif 'plastic' in addr:
        labels.append(2)

    else:
        labels.append(3)

# shuffle data
if shuffle_data:
    c = list(zip(addrs, labels)) # use zip() to bind the images and labels together
    shuffle(c)

    (addrs, labels) = zip(*c)  # *c is used to separate all the tuples in the list c,
                               # "addrs" then contains all the shuffled paths and
                               # "labels" contains all the shuffled labels.

# Divide the data into 75% for train and 25% for test
train_addrs = addrs[0:int(0.75*len(addrs))]
train_labels = labels[0:int(0.75*len(labels))]

test_addrs = addrs[int(0.75*len(addrs)):]
test_labels = labels[int(0.75*len(labels)):]

#========================== Part 2: Create the h5py Object ==========================
import numpy as np
import h5py

train_shape = (len(train_addrs), 128, 128, 3)
test_shape = (len(test_addrs), 128, 128, 3)

# open a hdf5 file and create earrays
f = h5py.File(hdf5_path, mode='w')

# PIL.Image: the pixels range is 0-255,dtype is uint.
# matplotlib: the pixels range is 0-1,dtype is float.
f.create_dataset("train_img", train_shape, np.uint8)
f.create_dataset("test_img", test_shape, np.uint8)

# the ".create_dataset" object is like a dictionary, the "train_labels" is the key.
f.create_dataset("train_labels", (len(train_addrs),), np.uint8)
f["train_labels"][...] = train_labels

f.create_dataset("test_labels", (len(test_addrs),), np.uint8)
f["test_labels"][...] = test_labels

#========================== Part 3: Write the Images #########################
import cv2

# loop over train paths
for i in range(len(train_addrs)):

    if i % 1000 == 0 and i > 1:
        print ('Train data: {}/{}'.format(i, len(train_addrs)) )

    addr = train_addrs[i]
    img = cv2.imread(addr)
    img = cv2.resize(img, (128, 128), interpolation=cv2.INTER_CUBIC)# resize to (128,128)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # cv2 load images as BGR, convert it to RGB
    f["train_img"][i, ...] = img[None]

# loop over test paths
for i in range(len(test_addrs)):

    if i % 1000 == 0 and i > 1:
        print ('Test data: {}/{}'.format(i, len(test_addrs)) )

    addr = test_addrs[i]
    img = cv2.imread(addr)
    img = cv2.resize(img, (128, 128), interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    f["test_img"][i, ...] = img[None]

f.close()

print('hdf5 file successfully created!!!')
