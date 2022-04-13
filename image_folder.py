from PIL import Image, ImageShow
import os


class ImageFolderIterator:
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.next_index = 0

    def __next__(self):
        if self.next_index >= len(self.image_folder):
            raise StopIteration
        image = self.image_folder[self.next_index]
        self.next_index += 1
        return image


class ImageFolder:
    def __init__(self, path):
        self.path = path
        self.names = os.listdir(path)
        self.names.sort()

    def __len__(self):
        return len(self.names)

    def __getitem__(self, index):
        image = Image.open(os.path.join(self.path, self.names[index]))
        image.load()
        return image

    def __iter__(self):
        return ImageFolderIterator(self)


ImageShow.register(ImageShow.DisplayViewer, order=0)

image_folder = ImageFolder('../images')
image = image_folder[0]
ImageShow.show(image)

for image in image_folder:
    print(image.filename, image.size)
