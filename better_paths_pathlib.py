#pathlib avoids using os.path.join
from pathlib import Path

dataset = 'wiki_images'
datasets_root = Path('/path/to/datasets/')

train_path = datasets_root / dataset / 'train'
test_path = datasets_root/ dataset/ 'test'

for image_path in train_path.iterdir():
    with image_path.open() as f: #open is a method of Path object
        # do something with an image in train

#pathlib.Path has a bunch of methods methods and properties
p.exists()
p.is_dir()
p.parts
p.with_name('siblings.png') # only change the name, but keep the folder
p.with_suffix('.jpg') #only change the extensions, but keep the folder and the  name
p.chmod(mode) #change mode of a file
p.rmdir() #remove directory

