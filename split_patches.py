import numpy as np
#import pickle
import re
import random
import os
from PIL import Image
from skimage.io import imread,imsave
import shutil

def patch_split(base_dir,save_dir,img_size=384):
	#imgs=[]
	#labels=[]
	for img in os.listdir(base_dir+"//image"):
		image=imread(base_dir+"//image//"+img)
		label=np.asarray(Image.open(base_dir+"//label//"+img[:-4]+"_instanceIds.png"))
		print(np.unique(label))
		x,y,z=image[:,:,:3].shape
		coords_x = x /img_size
		coords_y = y/img_size
		coords = [ (q,r) for q in range(int(coords_x)) for r in range(int(coords_y)) ]
		for coord in coords:
			imgs=image[coord[0]*img_size:(coord[0]+1)*img_size,coord[1]*img_size:(coord[1]+1)*img_size,:]
			labels=label[coord[0]*img_size:(coord[0]+1)*img_size,coord[1]*img_size:(coord[1]+1)*img_size]
			if np.unique(labels//1000).any()==0:
				continue
			else:
				imsave(save_dir+"//new_image//"+img[:-4]+"_"+str(coord)+".jpg",imgs)
				imsave(save_dir+"//new_label//"+img[:-4]+"_"+str(coord)+"_instanceIds.png",labels)
		
		