---
slug: "machine-learning-for-non-datascientists"
url: "https://devpost.com/software/machine-learning-for-non-datascientists"
title: "HandyML: Machine learning for non-datascientists"
hackathon: "Power Up Automation"
organization: "UiPath"
winner: true
words: 1127
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/structured_db"
---

# HandyML: Machine learning for non-datascientists

> Non-datascientists users can now train machine learning models by simply asking their robot to do it for them

[Devpost](https://devpost.com/software/machine-learning-for-non-datascientists) · hackathon [[Power Up Automation]]

## Facets

**domain** [[education]] [[supply_logistics]]
**user** [[educator_student]] [[researcher]]
**substrate** [[structured_db]]

**stack** anaconda, css3, html5, javascript, json, npm, numpy, pandas, python, sass, scikit-learn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we are proud of
- what we learned
- what's next for machine learning for non-datascientists
- quick installation guide

## Body

Logo 1. Where is your data? 2. Select your features 3. Select your target 4. Select your algorithm (Part 1) 4. Select your algorithm (Part 2) 5. Summary (Part 1) 5. Summary (Part 2) 6. Report (Part 1) 6. Report (Part 2) Inspiration This project comes from an idea I had while I was learning AI techniques in addition to my robotics skills, indeed I'm using UiPath for 3 years now. I recently take courses on Udemy about Machine Learning and Deep Learning to get familiar with these whole new subjects for me. Although, I took some tutorials to learn how to code in Python . All this together, I ended up with the idea of creating a robot allowing non-datascientists to create Machine Mearning models easily and as quickly as possible. Moreover, I welcomed an AI student for an internship of 4 months , so I definitely associated him to the project and we made this together . What it does It takes data from an Excel file and trains a Machine Learning model according to the type of problem to solve (regression or classification) and the algorithm used (linear regression, polynomial regression, logistic regression, etc.). Eventually, the trained models can be used to make predictions on new data. How we built it We first created configuration files using JSON language to specify all kind of parameters: one as a resource in order to list all algorithms and parameters handled by the tool one for the dataset, in which you can specify the path of the Excel file, the sheet to use, which columns are corresponding to the features, and which one is corresponding to the target, the algorithm to use and its parameters Then, we made the Python script to preprocess the data (dataset creation, label encoding) and train the model using pandas, numpy and scikit-learn libraries. Next, we created another Python script to use a saved model in order to make predictions on new data. Finally, we designed a user-friendly web application allowing users to follow all the steps from selecting the data to evaluate the accuracy of the trained model. There are 6 different steps : Where is your data? Select your features Select your target Select your algorithm and specify its parameters Review all your configuration and start the training Evaluate your model by its score, some plots, a confusion matrix and generate a template to make predictions with new data Eventually, we created two UiPath robots : a first one to interact with users through Custom Input activity displaying the different pages of the web application a second one based allowing users to make predictions with their trained models Challenges we ran into Create a fresh installation of Anaconda3 / Python 3.6 on a Windows 10 machine. Code a python script managing multiple types of algorithm and 2 types of machine learning problems (regression and classification). Link UiPath to Python using standard available activities. Use Custom Input activity to really enhance user experience and ease the use of the tool. Exchange data between Python, UiPath and an embedded web application through Custom Input activity. Accomplishments that we are proud of Give the ability to create a supervised machine learning model with a simple Excel file as input data. Connect UiPath Studio to an Anaconda environment and manipulate Python objects with standard activities. Develop a user-friendly web application with modern CSS3 and HTML5 along with Javascript ES6. Integrate this web application inside a UiPath Robot and find a way to exchange data with high performance. What we learned We learned that UiPath solution is really designed to talk to various types of applications and can be definitely used for a tremendous number of use cases. We also learned a lot about how and when to use Machine Learning algorithms to fix different types of Machine Learning problems, either classification or regression. Eventually, that mixing different skills can make you produce things you're not able to create alone. What's next for Machine learning for non-datascientists We can hope adding more supervised learning algorithms and add more parameters to existing ones. Create an unattended version of HandyML Predictor. Also, why not integrate Deep Learning? Quick installation guide 1. Prerequisites Project developed and tested on a Windows 10 machine. 1.1. UiPath version This project has been developed under UiPath Studio 2019.4.3. So you will need a Studio/Robot with version 2019.4.3+. 1.2. Python version This project uses Python 3.6.8+. It has been tested and developed on a x64 architecture. You can easily have a working Python 3.6 environment by installing Anaconda 2019.03 version ( download Anaconda ). Then you will need to create an Anaconda environment specifying Python 3.6.8+ version by executing the following in Anaconda Prompt (replace [environment-name] by the name you want, eg. env-3.6): conda create-env -n [environment-name] python=3.6 1.3. Python packages You will also need to install the following packages using either conda (if Anaconda installed) or pip to be able to use this tool. If using Anaconda, launch Anaconda Prompt and execute following commands: activate [environment-name] conda install numpy pandas scikit-learn pip install matplotlib scikit-plot pip install win10toast (add options --user --ignore-installed when installed on a Windows 7 machine) 1.3.1. NumPy Developed with NumPy 1.16.4. 1.3.2. Pandas Developed with Pandas 0.24.2. 1.3.3. Scikit-Learn Developed with Scikit-Learn 0.21.2. 1.3.4. Matplotlib Developed with Matplotlib 3.1.1. (Note: needs to be installed using pip , not working correctly using conda ) 1.3.5. Win10toast Developed with Win10toast 0.9. (Note: needs to be installed using pip , not working correctly using conda ) 1.3.6. Scikit-Plot Developed with Scikit-Plot 0.3.7. (Note: needs to be installed using pip , not working correctly using conda ) 1.4. Environment variables In order for the UiPath Robot to know where is Python installed and on which architecture you'll have to create 2 environment variables: HANDYML_PYTHON_PATH , indicating the folder on which python.exe file can be found > With Anaconda installed you can know where the python.exe file is by following this: https://docs.anaconda.com/anaconda/user-guide/tasks/integration/python-path/ HANDYML_PYTHON_TARGET , indicating the machine architecture (should be x64 or x86) 2. Create and train a supervised machine learning model Just launch HandyML_Trainer and follow the steps! Of course, to start you'll need an Excel file holding your data, everything is explained at step 1. Where is your data? . 3. Make predictions on new data using a trained model This time launch HandyML_Predictor and specify the path of the Excel configuration file generated by HandyML_Trainer indicating the model to use, the JSON configuration file associated to this model. A sheet named data is available for holding new data. Important note: New data must have exactly the same format as the one used during training. 4. Let us know if you have any issues Github: https://github.com/masiref/HandyML Email: masire.fofana@natixis.com | chabnichab@eisti.eu <div