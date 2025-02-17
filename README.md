<h1 align="center"> 
   REMED-T2D
    <br>
<h1>

<h4 align="center">Standalone program for the paper "REMED-T2D: A robust ensemble learning model for early detection of type 2 diabetes using healthcare dataset"</h4>

<p align="center">
<a href=""><img src="https://img.shields.io/github/stars/Cobonla/REMED-T2D?" alt="stars"></a>
<a href=""><img src="https://img.shields.io/github/forks/Cobonla/REMED-T2D?" alt="forks"></a>
<a href="https://github.com/Cobonla/REMED-T2D/blob/main/LICENSE">
  <img src="https://img.shields.io/github/license/Cobonla/REMED-T2D" alt="license">
</a>

</p>

<p align="center">
  <a href="#introduction">Abstract</a> •
  <a href="#introduction">Introduction</a> •
  <a href="#installation">Installation</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#citation">Citation</a> •
</p>

<p align="center">
    <img src="https://github.com/user-attachments/assets/7c4671c9-2fb2-4df8-b6cc-36f3ec9fc209" width="1280"/>
</p>

## Abstract
Early diagnosis and timely treatment of diabetes are critical for effective disease management and the prevention of complications. Undiagnosed diabetes can lead to an increased risk of several health issues. Although numerous machine learning (ML) models have been designed to detect diabetes, many exhibit unsatisfactory performance, are not publicly available, and lack validation on external datasets. To address these limitations, we have developed REMED-T2D, an advanced ensemble ML approach that enhances predictive accuracy and robustness through the integration of diverse ML algorithms. Our approach involves a rigorous data preprocessing process and systematic evaluation of 20 different algorithms, encompassing both conventional ML and deep learning for diabetes prediction. Firstly, we applied an under-sampling approach to an imbalanced Pima Indian Diabetes dataset and generated five balanced datasets. Using these datasets, we investigated various computational strategies to select the optimal model for accurate diabetes classification. Our results demonstrate that REMED-T2D outperformed state-of-the-art methods on the training dataset, with notable improvements in ACC (1.40–4.60%) and MCC (3.50–9.80%). Extensive external validations revealed that the model trained on a five-feature subset achieved ACC of 92.61 % and 92.26 % on the RTML1 and Pabna datasets, respectively. Moreover, a model based on a seven-feature subset improved ACC by 2.80 % and MCC by 13.27 % on the RTML2 dataset. These results suggest the potential of REMED-T2D to predict diabetes in Asian females. Notably, this is the first study to conduct such a comprehensive analysis using the Pima dataset, incorporating a diverse set of ML algorithms. Furthermore, we have developed a publicly accessible web server (https://balalab-skku.org/REMED-T2D/) to facilitate self-monitoring and timely medical interventions. We believe REMED-T2D will assist healthcare professionals in detecting diabetes earlier and implementing preventive measures, ultimately improving health outcomes for those at risk.

## Introduction
This repository provides the standalone program that was added to REMED-T2D web server at https://balalab-skku.org/REMED-T2D. 

## Installation

### Software requirements
Python 3.9

### Creating conda environments
```shell
conda create -n REMED-T2D python=3.9.18
```
```shell
conda activate REMED-T2D
```
### Installing required specific packages
```shell
python -m pip install numpy==1.33.4 pandas==2.0.3 --no-cache-dir
```
```shell
python -m pip install catboost==1.2 lightgbm==3.3.5 scikit-learn==0.24.2 xgboost==0.82 --no-cache-dir
```
### Getting started
```
git clone https://github.com/Cobonla/REMED-T2D.git
```
```
cd REMED-T2D
```
```
python prediction.py
```
## Citation
If you use this code or part of it, please cite the following papers:
```
@article{phan2025remed,
  title={REMED-T2D: A robust ensemble learning model for early detection of type 2 diabetes using healthcare dataset},
  author={Phan, Le Thi and Rakkiyappan, Rajan and Manavalan, Balachandran},
  journal={Computers in Biology and Medicine},
  volume={187},
  pages={109771},
  year={2025},
  publisher={Elsevier}
}
```

