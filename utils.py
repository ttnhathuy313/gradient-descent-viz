import os
import imageio

def clear_graph_folder():
    folder = './graphs'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        os.remove(file_path)

def create_gifs():
    # Combine all images in graphs folder into a gif
    images = []
    for filename in os.listdir('./graphs'):
        file_path = os.path.join('./graphs', filename)
        images.append(imageio.imread(file_path))
    imageio.mimsave('./graphs/gradient_descent.gif', images, duration=0.5)
