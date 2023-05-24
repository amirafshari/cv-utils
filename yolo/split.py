import os
import shutil
import random



def splitor(tr, root, dirType='yolov5'):
    if dirType.lower() == 'yolov5': 
        # Create YOLOv5 style directory
        try:
            os.mkdir('dataset')
            os.mkdir('dataset/images')
            os.mkdir('dataset/labels')

            os.mkdir('dataset/images/train')
            os.mkdir('dataset/labels/train')

            os.mkdir('dataset/images/val')
            os.mkdir('dataset/labels/val')
        except FileExistsError:
            pass
        
        # Path
        img_path = os.path.join(root, 'images')
        label_path = os.path.join(root, 'labels')
        
        # All of em
        items = []
        for item in os.listdir(img_path):
            items.append(item)
        random.shuffle(items)


        train = []
        val = []
        
        train_size = int(tr * len(items))
        val_size = int(len(items) - train_size)

        
        # train
        for i in range(train_size):
            train.append(items[i])

        items = list(set(items) - set(train))
        
        # val
        for i in range(val_size):
            val.append(items[i])
        
        items = list(set(items) - set(val))

            
            
        # Copying
        try:
            for item in train:
                shutil.copyfile(os.path.join(img_path, item), os.path.join('dataset/images/train', item))

                label = item.replace(item[-4:], '.txt')
                shutil.copyfile(os.path.join(label_path, label), os.path.join('dataset/labels/train', label))
                
        except FileNotFoundError:
            print(item)
            

            
            
        try:
            for item in val:
                shutil.copyfile(os.path.join(img_path, item), os.path.join('dataset/images/val', item))

                label = item.replace(item[-4:], '.txt')
                shutil.copyfile(os.path.join(label_path, label), os.path.join('dataset/labels/val', label))
                
        except FileNotFoundError:
            print(item)




    elif dirType.lower() == 'yolov7':
        try:
            os.mkdir('dataset')
            os.mkdir('dataset/train')
            os.mkdir('dataset/val')
            # os.mkdir('dataset/test')

            os.mkdir('dataset/train/images')
            os.mkdir('dataset/train/labels')

            os.mkdir('dataset/val/images')
            os.mkdir('dataset/val/labels')


        except FileExistsError:
            pass
        
        # Path
        img_path = os.path.join(root, 'images')
        label_path = os.path.join(root, 'labels')
        
        # All of em
        items = []
        for item in os.listdir(img_path):
            items.append(item)
        random.shuffle(items)


        train = []
        val = []
        
        train_size = int(tr * len(items))
        val_size = int(len(items) - train_size)
        
        # train
        for i in range(train_size):
            train.append(items[i])

        items = list(set(items) - set(train))
        
        # val
        for i in range(val_size):
            val.append(items[i])
        
        items = list(set(items) - set(val))

            
            
        # Copying
        try:
            for item in train:
                shutil.copyfile(os.path.join(img_path, item), os.path.join('dataset/train/images', item))

                label = item.replace(item[-4:], '.txt')
                shutil.copyfile(os.path.join(label_path, label), os.path.join('dataset/train/labels', label))
                
        except FileNotFoundError:
            print(item)
            
            
        try:
            for item in val:
                shutil.copyfile(os.path.join(img_path, item), os.path.join('dataset/val/images', item))

                label = item.replace(item[-4:], '.txt')
                shutil.copyfile(os.path.join(label_path, label), os.path.join('dataset/val/labels', label))
                
        except FileNotFoundError:
            print(item)

    else:
        print('Invalid Type. Choose \'yolov5\' or \'yolov7\' ')

    print('Done')


f = splitor(.85, 'dataset', 'yolov7')
