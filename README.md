# Using Synthetic Data in Training Deep Neural Networks for Real-World Underwater Objects Recognition

Vladislav A. Plotnikov
plotnikovva@student.bmstu.ru
vladislav.a.plotnikov@yandex.ru

Yaroslav M. Kamenev
kamenev.yar@gmail.com

Vladimir V. Serebrenny
vsereb@bmstu.ru

**Abstract.** Convolutional neural networks are widely used to solve the problem of object recognition in images and have many advantages over classical image processing algorithms. However, training such neural networks requires a large dataset, the collection and labeling of which are time-consuming, especially for underwater objects. Underwater data collection involves full-scale trips to a pool or open water and requires waterproof equipment. This article explores the use of the computer simulator and domain randomization, as well as the use of a generative neural network to collect data and use it in training convolutional neural networks for recognizing underwater objects. Virtual simulator built on the Unity engine was used to visualize underwater scenes with different camera positions and underwater objects, visual effects, as well as various textures and objects. The generative neural network CycleGAN was used to transform synthetic data to a “real” form. The authors of the article prepared several datasets containing real, semi-synthetic and fully synthetic images, which were used to train the YOLOv5 convolutional neural network and compared the quality of object recognition on a validation set consisting of real data. For training, objects were selected from the SAUVC underwater robotics competition tasks.

**Keywords.** *Convolutional neural networks, object recognition, underwater robotics, domain randomization, CycleGAN, YOLOv5*

## Introduction

Training neural networks requires a large dataset, the collection and labeling of which are time-consuming, especially for underwater objects. 
Underwater data collection involves full-scale trips to a pool or open water and requires waterproof equipment.

![Tests of the ROV Cousteau-2 in the swimming pool](/images/introduction/pool.png)
Tests of the ROV Cousteau-2 in the swimming pool


## Related Work

### Dataset

Dataset was collected using the Unity game engine.
Script for randomization camera positions and environment (fog and textures) was designed. 
After randomizing, script generates bounding boxes for the objects on the screen and creates text file with bounding boxes information, then takes screenshot.

![View of underwater scene from Unity Editor](/images/dataset/scene.png)
View of underwater scene from Unity Editor

Script works in “rounds”. This system was designed to ease the collection and editing of datasets.
Rounds:
- **round_1** - randomized fog and camera position;
- **round_2** - round_1 with randomized underwater props textures;
- **round_3** - round_1 with randomized pool textures;
- **round_0** - round_1 with randomized underwater props and pool textures;

Camera is pointed at one of the props, each 100 positions new prop is selected

![Examples of one image in 4 rounds, clockwise: round_1 (upper left corner), round_2, round_0, round_3](/images/dataset/examples.png)
Examples of one image in 4 rounds, clockwise: round_1 (upper left corner), round_2, round_0, round_3

### Training on real data

Neural net: YOLOv5m

Training parameters:
- GPU: Nvidia Quadro P4000
- framework: PyTorch 
- 869 images total: 732 in train set, 137 in validation set;
- image size: 640x640
- 300 epochs
- batch size - 16
- data augmentation

![Train batch](/images/training_real/batch.png)
Train batch

![Metrics](/images/training_real/graphs.png)
Metrics

![Validaton on real data](/images/training_real/val.png)
Validaton on real data

### Training on synthetic data

Neural net: YOLOv5m

Training parameters:
- Same as on real data
- 500 images total: 400 in train set, 100 in validation set;

Training on round_1 (randomized fog and camera position) and round_3 (as round_1 with randomized pool textures) data show best results

Training on fully randomized data show lower quality on validation data


### Synthetic dataset enhancement

Generative adversarial network - CycleGAN
Style transferring from simulation to reality

## Results

## Conclusion

- Training on randomized data from the simulator shows a low quality of recognition on the validation set;
- Using CycleGAN to enhance synthetic images in the dataset improved the quality of real objects recognition;
- Training on enhanced data and small amount of real data gave almost the same recognition quality as training on real data only.

## References

[1] Plotnikov, Vladislav & Akhtyamov, T. & Kopanev, Pavel & Serebrenny, Vladimir. (2022). Classical and neural network approaches to object detection in underwater robotics competitions. AIP Conference Proceedings. 2383. 020021. 10.1063/5.0083975. 