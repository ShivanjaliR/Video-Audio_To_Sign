from utils import get_speech_images, display_speech_image

if __name__ == '__main__':
    speech = ['Hello, hello.', 'Can you clap your hands?', 'Hello, hello.', 'Can you clap your hands?', 'Can you stretch up high?', 'Can you touch your toes?', 'Can you turn around?', 'Can you say, "Hello"?', 'Hello, hello.', 'Can you stamp your feet?', 'Hello, hello.', 'Can you stamp your feet?', 'Can you stretch up high?', 'Can you touch your toes?', 'Can you turn around?', 'Can you say, "Hello"?', 'Hello, hello.', 'Can you clap your hands?', 'Hello, hello.', 'Can you stamp your feet?']
    speech_in_images = get_speech_images(speech)
    print(speech_in_images)
    display_speech_image(speech_in_images)