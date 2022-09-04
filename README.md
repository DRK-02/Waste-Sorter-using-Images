# Waste-Sorter-using-Images

![png-clipart-reuse-reduce-recycle-logo-environmental-management-system-waste-management-natural-environment-recycle-bin-leaf-logo](https://user-images.githubusercontent.com/97865229/188336555-97e41217-3d26-47f5-9d13-1a368d9792d7.png)

## What it does
The software takes in images and identifies what type of waste it is, i.e., glass, metal, paper, or plastic, and classifies it accordingly.

![db7c24c3-ebcd-413a-9ee0-4b95b3882b0f](https://user-images.githubusercontent.com/97865229/188336594-4ee0f744-5e0a-4754-8387-47ad8a1eef83.png)

## How we built it
We needed to use artificial intelligence for this purpose. So, we made a CNN, i.e., Convolution Neural Network model for analyzing and classifying the images. 

While building the model we made multiple layers. The first few layers enhance the image making it easier for classifying. These layers were made of convolution layers of 32, 64, 128, and 256 filters, and the images coming out after the layer was normalized and passed through a max pooling layer. So, only the important features of the images were retained while the rest was discarded or ignored.

Next was dense layers. These layers are responsible for classifying the image. There were multiple dense layers of 1024, 512, 256, 128, and 4 decision trees in each one separately. Like in the earlier layers, the data coming out of each of the dense layers was also normalized.

![image](https://user-images.githubusercontent.com/97865229/188336643-f2c05b09-9c76-48e9-9a03-cb2401b73a57.png)

The data was split in a ratio of 3:1 for the training and validation sets respectively. Even though it was restricted to 40 epochs in the code, upon analyzing and studying the training graph, the model can yield an accuracy of up to 85-90%.

## Challenges we ran into
Since it is a CNN model, images are loaded and as such, it takes a lot of training time. The only way to reduce this is to integrate it with an extremely good processor and a GPU, i.e., Graphics Processing Unit, or a TPU, i.e., Tensor Processing Unit.

## What's next for Waste Sorter Using Images
This software must get a bigger dataset to learn from with more categories for the waste types. It must also be used on a processor with extremely high speed to train the model.

For this software to be applied in the real world, it must be integrated with a robotic arm or a conveyor belt system to segregate the waste.

![zen-robotics-image-2](https://user-images.githubusercontent.com/97865229/188336659-da23fdcf-1de1-4c43-8b1d-d704e238033f.jpg)

