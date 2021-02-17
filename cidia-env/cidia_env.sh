#!/bin/bash
conda init bash
source ~/.bashrc
conda activate cidia19 
conda install pytorch==1.3.0 torchvision cudatoolkit=10.0 -c pytorch 
conda install -c caffe2 caffe
conda install dicom2nifti -c conda-forge
conda install pydicom
conda install nibabel
conda install tensorflow==2.0.0
conda install tensorflow-gpu==2.0.0
conda install requests
conda install flask


# conda install jupyter 
