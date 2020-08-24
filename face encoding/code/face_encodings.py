# -*- coding: utf-8 -*-
# Indentation: Jupyter Notebook

'''
Face Encoding
'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"



# Load the jpg files into numpy arrays


# Generate the face encodings


if len(face_encodings) == 0:
    # No faces found in the image.
    print("No faces were found.")

else:
    # Grab the first face encoding
    first_face_encoding = face_encodings[0]

    # Print the results
    print(first_face_encoding)
