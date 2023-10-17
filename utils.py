import os
import imageio

def clear_graph_folder():
    folder = './graphs'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        os.remove(file_path)

def create_gifs(name='./animation.gif'):
    # Combine all images in graphs folder into a gif
    images = []
    for filename in os.listdir('./graphs'):
        file_path = os.path.join('./graphs', filename)
        images.append((int(filename[:-4]),imageio.imread(file_path)))
    images.sort(key=lambda x: x[0])
    imageio.mimsave(name, [img for _, img in images], duration=0.5)
