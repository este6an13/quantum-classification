import cv2
import numpy as np
import h5py
import os

def read_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)
            images.append(image)
    return images

def process_images(images):
    processed_images = []
    for i in range(len(images)):
        # Conversion to grayscale
        gray = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)

        # Masking
        #mask = (gray < 250).astype(np.uint8)
        #masked = cv2.bitwise_and(gray, gray, mask=mask)

        # Histogram Equalization
        equalized = cv2.equalizeHist(gray)

        # Binary Thresholding
        #binary = cv2.inRange(equalized, 1, 10)

        # Resize to 28x28
        resized = cv2.resize(equalized, (32, 32))

        processed_images.append(resized)
    return processed_images

def write_to_h5(images, output_file):
    with h5py.File(output_file, 'w') as hf:
        for i in range(len(images)):
            hf.create_dataset(f'image_{i}', data=images[i])

def main():
    syndrome_folder = r'D:\dequi\Documents\REDN-Project\syndrome_images_200'
    non_syndrome_folder = r'D:\dequi\Documents\REDN-Project\non_syndrome_images_200'

    syndrome_images = read_images(syndrome_folder)
    non_syndrome_images = read_images(non_syndrome_folder)

    processed_syndrome = process_images(syndrome_images)
    processed_non_syndrome = process_images(non_syndrome_images)

    write_to_h5(processed_syndrome, 'syndrome_data_200_32.h5')
    write_to_h5(processed_non_syndrome, 'non_syndrome_data_200_32.h5')

if __name__ == "__main__":
    main()
