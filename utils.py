import os
from os.path import join
import matplotlib.pyplot as plt
import numpy as np

def find_files(filename, search_path):

    for root, dir, files in os.walk(search_path):
        if filename in files:
            return True
    return False

def get_speech_images(speech):
    speech_in_images = []
    line_images = []
    for line in speech:
        tokens = line.split()
        line_images = []
        for token in tokens:
            token_images = []
            for alpha in token:
                image_name = alpha.lower() + '.gif'
                file_name = join('images/', image_name)
                if find_files(image_name, "images"):
                    token_images.append(file_name)
            line_images.append(token_images)
        speech_in_images.append(line_images)
    return speech_in_images

def get_words_in_line_size(line):
    words_in_line = 0
    for words in line:
        words_in_line += len(words) + 1
    return words_in_line

def display_speech_image(speech_in_images):
    imgs = []
    line = 0
    for line_images in speech_in_images:
        line = 1
        words_in_line = get_words_in_line_size(line_images)
        fig = plt.figure()
        word_count = 1
        for word in line_images:
            for character in word:
                fig.add_subplot(1, words_in_line, word_count)
                fig.set_size_inches((20, 20))
                plt.axis('off')
                image = plt.imread(character)
                plt.imshow(image, aspect='equal')
                word_count += 1
            blank_image = 255 * np.ones([20, 20, 4], dtype=np.uint8)
            fig.add_subplot(1, words_in_line, word_count)
            fig.set_size_inches((20, 20))
            plt.axis('off')
            plt.imshow(blank_image, aspect='equal')
            word_count += 1
        plt.show()

