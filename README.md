# Face-Attendence-System

Part-1 (Face attendence system)

The folder "face_similarity" contains the codes that are required for running the system

1) Download the dataset from http://vis-www.cs.umass.edu/lfw/lfw.tgz. extract it and rename it as "data" and place it in the "face_similarity" folder.
2) Install the haarcascade from https://drive.google.com/file/d/1UCoojYteOVdAlSyXmS37jnCQWC73Airw/view?usp=sharing. Place it in the "face_similarity" folder.
3) Download the pre-trained model from https://drive.google.com/file/d/1EqY0eBgXp-fG7DS532vY52SgoY762YOz/view?usp=sharing.place it in the "face_similarity" folder.
4) Run the "data.py" code to pre-process the images. The images are modified and replaced with the original images.
5) To train the model run "train.py". Change the model name at last to not replace the original model.
6) To test the model on given input run the "test.py". Change the locations of input images, written as 'img1_path" and "img2_path".
7) My images are in the "face_similarity" named, "soorya _01.jpg" and "soorya _02.jpg"

Requirements :-
1) Keras -- 2.3.1
2) Tensorflow -- 1.14.0
3) OpenCV -- 4.4.0
4) numpy -- 1.16.1
5) pandas -- 1.1.5

Part-2(Write up about use of image segmentation and FCN)

The pdf "intership part-2.pdf"
