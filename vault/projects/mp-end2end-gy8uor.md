---
slug: "mp-end2end-gy8uor"
url: "https://devpost.com/software/mp-end2end-gy8uor"
title: "MP-End2End"
hackathon: "Forest Hacks"
organization: "ForestHackathons"
winner: true
words: 1292
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# MP-End2End

> A novel low-cost depth-from-focus method to perform 3D reconstruction of microplastics, to better analyse environmental impacts.

[Devpost](https://devpost.com/software/mp-end2end-gy8uor) · hackathon [[Forest Hacks]]

## Facets

**mechanism** [[retrieval_grounding]] [[vision_ocr]]
**domain** [[education]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** egbis, opencv, python, pytorch, sift

## How they structured the write-up

- inspiration
- 💡 inspiration
- 👍what it does
- 🛠️ how we built it
- 😭 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📝 what we learned
- 🔮 what's next for mp-end2end

## Body

Title Page Generated mesh and contour map SIFT generated keypoints Translation screw created in CAD Classification pipeline Hardware Process Microscope data segmented using EGBIS Focus map generated at different magnifications Inspiration 💡 Inspiration As our school is close to the River Itchen, recent papers surrounding microplastic pollution in the river sparked our interest. Additionally, we were very interested in recent developments in computer vision AI research, like neural rendering. We then discovered the importance of the shape of microplastics. Firstly, larger and more voluminous MPs break down into smaller MPs. If we only record the number of MPs, we may mistakenly identify MP types that are more prone to breaking down as being more prevalent. This could shift efforts away from addressing the primary sources of MP pollution, leading to ineffective mitigation. Secondly, according to Barchiesi et al., "The effects and risks of MPs correlate with three-dimensional (3D) properties, such as the volume and surface area of the biologically accessible fraction of the diverse particle mixtures as they occur in nature." 3D data is clearly significant in analysing the specific effects of MPs on ecosystems. For example, Ward et al. found that "the extent of microplastic transport and deposition varied significantly by shape". Furthermore, they even found that "accurately modelling the shape of ... microplastic transport is crucial to determining the range and amount of deposition globally". The shape of microplastics are also significant in biological processes: according to Han et al., "Nonspherical particles... cylindrical polymer brushes ... and wirelike objects ... each [have] a unique influence on the cell". Upon finding the significance of the shape of microplastics (e.g. impact on cells, effects on deposition), merging the two together seemed only natural. 👍What it does We built a hardware-integrated software solution to reconstruct 3D models of microplastics. The methodology requires the user to place a sample sediment under a microscope and take images from various angles. The program will then reconstruct an accurate 3D model of microplastics within the sample. The hardware involved modifying an off-the-shelf, cheap, digital microscope to be actuated automatically and the software involved using the low-resolution image to extract meaningful information. 🛠️ How we built it In terms of hardware, we designed a custom toothed translation screw to convert the rotary motion of a 12V stepper motor to linear motion of the objective lens. This component was created via resin 3D-printing. The motor is controlled by an Arduino UNO, running the power input through a 12V relay. In terms of software, we designed a pipeline to perform end to end analysis: that is, given the microplastic sample, the program performs all the required steps to generate a 3D model. The first step involves segmentation. Segmentation While many teams may gravitate to new computer vision advancements to perform the segmentation (e.g. the newly released YOLOv10 or CNN-based region proposal networks), we realised that these methodologies would be inaccurate on our data. This is as these models are trained on datasets on everyday objects, which would make the irregular geometries, resolution and colours of microscopic particles inaccurate. Our suspicion was proved right when we tested the algorithm and was unable to identify objects within the scene. Instead, we used the EGBIS algorithm. Proposed by Felzenszwalb et al., the algorithm uses simple graph theory principles to perform semantic segmentation. This is much more effective than previous AI-based implementations, especially as microscope images have clearly defined backgrounds and foregrounds. Classification We employ a few-shot learning methodology. Specifically, we implement a prototypical network implementation of few-shot learning. This involves learning an embedding function f(x) that projects input images into a high dimensional space. We aim to learn an embedding function where projected points of microplastics are close together and those that are not microplastics are projected far away from microplastic. We initialise the parameters by using a ResNet50 model trained on the ImageNet dataset. This is as we expect this model to be an efficient feature extractor: that is, the filters within the model are likely good at extracting semantic information. We then fine-tune the model based on the dataset given: we project images of known microplastics into the high embedding space and then used backpropagation to adjust the loss to move projected points closing together. With this, we achieve 96.1% accuracy in classifying microplastics. Point Cloud Generation Depth from focus is a technique used in computer vision and image processing to estimate the depth information of a scene based on the concept of focus. Here's how it works: In photography and imaging, when an object is in focus, it appears sharp and clear, while objects at different distances from the focal plane appear blurred or out of focus. By determining the distance at which a point is most focused, we can determine its depth. We therefore use a novel blur detection algorithm (proposed by Golestaneh et al.) to detect focused areas within images of different magnifications. This methodology is far more effective than Laplacian based approaches as it can recover fine details on the object, thus allowing for accurate reconstruction of individual points. However, the object is at different positions at images captured at different magnifications. We therefore use the SIFT methodology (proposed by David Lowe) to perform alignment. We first identify keypoints on the image. Using the FLANN submodule in OpenCV, we identify neighbours in other images. We then estimate a homography matrix that maps points onto their neighbors. By performing the matrix transformation, we align all focus maps generated. We then find when each point is at maximal focus. Using the thin-lens formula, we can determine the distance of the point from the camera. We then save this as a point cloud and visualise the output. We can perform volume estimation by using 3D convex hull or Delaunay triangulation. 😭 Challenges we ran into Limited data for microplastics We expected to find a large amount of data for microplastic images, but were surprised to find only one dataset that used light microscopes. Although this posed a significant challenge to our project, this proved to us the importance of our project: if the project is to work, we could contribute to research by providing more free data on the internet. Hardware difficulties We (as always) underestimated the difficulty in the hardware, which resulted in a large amount of time reiterating and going "back to the drawing board". This was particularly damaging as slowed development of hardware bottlenecked software development Complicated Theory The methodologies that we used were often terse and presumed mastery of machine learning and optics. We therefore had to work to understand and simplify the concepts presented so we could effectively utilise these tools. 🏆 Accomplishments that we're proud of We are proud to have completed a finished product: upon seeing the generated mesh for the first time, we were incredibly excited. We are also proud of our self-discipline in using classical computer vision tools: we believe that we avoided many pitfalls by using classical computer vision algorithms instead of just defaulting to AI immediately. Lastly, we are proud to have tackled such an ambitious project idea! 📝 What we learned We learnt the importance of communication (genuinely): in a project where different members work on sections of a linear pipeline, communication do requirements objectives and trust is necessary to make meaningful progress. We learnt, first hand, that social impact is not restricted by age. Anyone can make an impact. 🔮 What's next for MP-End2End We plan to further develop our project after the end of the hackathon. We plan to enter our project for the Earth Prize this year (in hopes of winning $100,000 for the project) as well as submit our project to journals and conferences (notably, ECCV workshop 2024, WACV 2024 and AAAI 2025). <div