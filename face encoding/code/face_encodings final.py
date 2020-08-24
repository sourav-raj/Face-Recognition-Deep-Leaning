# -*- coding: utf-8 -*-
# Indentation: Jupyter Notebook

'''
Face Encoding
'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"


import face_recognition

# Load the jpg files into numpy arrays
image = face_recognition.load_image_file("../data/person.jpg")

# Generate the face encodings
face_encodings = face_recognition.face_encodings(image)

if len(face_encodings) == 0:
    # No faces found in the image.
    print("No faces were found.")

else:
    # Grab the first face encoding
    first_face_encoding = face_encodings[0]

    # Print the results
    print(first_face_encoding)
