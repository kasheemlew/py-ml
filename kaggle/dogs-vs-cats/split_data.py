import os, shutil


def mkne(directory):
    '''
    mkdir if not exists
    '''
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

dataset_dir = mkne(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'))
train_dir = mkne(os.path.join(dataset_dir, 'train'))
small_train_dir = mkne(os.path.join(dataset_dir, 'small_train'))
val_dir = mkne(os.path.join(dataset_dir, 'validation'))
test_dir = mkne(os.path.join(dataset_dir, 'test'))

train_cats_dir = mkne(os.path.join(small_train_dir, 'cats'))
train_dogs_dir = mkne(os.path.join(small_train_dir, 'dogs'))

val_cats_dir = mkne(os.path.join(val_dir, 'cats'))
val_dogs_dir = mkne(os.path.join(val_dir, 'dogs'))

test_cats_dir = mkne(os.path.join(test_dir, 'cats'))
test_dogs_dir = mkne(os.path.join(test_dir, 'dogs'))

def chdir(fnames, src_dir, dst_dir):
    for fn in fnames:
        src = os.path.join(src_dir, fn)
        dst = os.path.join(dst_dir, fn)
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.move(src, dst)

if __name__ == '__main__':
      chdir([f'cat.{i}.jpg' for i in range(1, 1000)], train_dir, train_cats_dir)
      chdir([f'cat.{i}.jpg' for i in range(1000, 1500)], train_dir, val_cats_dir)
      chdir([f'cat.{i}.jpg' for i in range(1500, 2000)], train_dir, test_cats_dir)
      chdir([f'dog.{i}.jpg' for i in range(1, 1000)], train_dir, train_dogs_dir)
      chdir([f'dog.{i}.jpg' for i in range(1000, 1500)], train_dir, val_dogs_dir)
      chdir([f'dog.{i}.jpg' for i in range(1500, 2000)], train_dir, test_dogs_dir)
