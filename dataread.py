
import os
# path = "/home/cvlab/Documents/CASIA/NIR/"
# path = "/home/cvlab/Documents/CASIA/VIS/"
# path2 = "/home/cvlab/Documents/CASIA/filename/"
#
# path = "/home/cvlab/Documents/Dataset/Lab2_part2/Nir/"
# # path = "/home/cvlab/Documents/Dataset/Lab2_part2/Vsb/"
# path2 = "/home/cvlab/Documents/Dataset/Lab2_part2/filename/"

path="/home/cvlab/baidunetdiskdownload/NIR-VIS/NIR_crop_2/"
path2 = "/home/cvlab/baidunetdiskdownload/NIR-VIS/"


for a, b, c in os.walk(path):
    x = int(len(c)*0.9)
    train = c[:x]
    test = c[x:]


    # print(len(train),len(test), len(c))
    # with open(path2+'nir_train.txt','w') as file:
    with open(path2 + 'nir_crop_train.txt', 'w') as file:
        for i in train:
            # file.write(i+'\n')
    # with open(path2 + 'nir_test.txt', 'w') as file:
    with open(path2+'nir_crop_test.txt','w') as file:
        for i in test:
            # file.write(i+'\n')

