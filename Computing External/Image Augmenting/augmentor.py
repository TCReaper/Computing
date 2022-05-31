import Augmentor

# change this path to your own
path = r"C:\Users\haosh\Documents\GitHub\Computing\Computing External\Image Augmenting\images"

p = Augmentor.Pipeline(path)

""" p.zoom(probability=0.3,min_factor=0.8,max_factor=1.5)
p.flip_top_bottom(probability=0.4)
p.random_brightness(probability=0.3,min_factor=0.3,max_factor=1.2)
p.random_distortion(probability=1,grid_width=4,grid_height=4,magnitude=8) """

p.gaussian_distortion(
    probability=0.5,
    grid_width=10,
    grid_height=10,
    magnitude=25,
    corner='bell',
    method='in'
)

p.random_brightness(
    probability=0.5,
    min_factor=0.75,
    max_factor=1.75
)

p.random_contrast(
    probability=0.5,
    min_factor=0.25,
    max_factor=1.75
)

# p.random_erasing(
#     probability=0.33,
#     rectangle_area=0.05
# )

p.random_color(
    probability=0.5,
    min_factor=0.5,
    max_factor=2.75
)

p.random_distortion(
    probability=0.33,
    grid_height=10,
    grid_width=10,
    magnitude=25
)

p.zoom_random(
    probability=0.5,
    percentage_area=0.99,
    randomise_percentage_area=True
    )


p.save_format = 'PNG' # had an error without this line so it's here

p.sample(500)

import os
def randomer(filename,path,n):
      new = str(n)+'.PNG'
      os.rename(os.path.join(path,filename), \
                os.path.join(path,new))

outputpath = path+r'\output'
files = os.listdir(outputpath)
n = 0
for file in range(len(files)):
    randomer(files[file],outputpath,n)
    n+=1

