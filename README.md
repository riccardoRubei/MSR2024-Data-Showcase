# About 


This repository contains the source code implementation used to replicate the experimental results obtained in the submitted to the 21st International Conference on Mining Software Repositories (MSR204). 

*"PlayMyData: a curated dataset of multi-platform videogames"*


authored by:

Andrea D'Angelo(1), Claudio Di Sipio, Cristiano Politowsky (2) and Riccardo Rubei


(1) Università degli Studi dell'Aquila, Italy

(2) University of Montreal, Canada





# Repository structure 

- `data_analysis`: It contains the Jupyter Notebooks used to compute the statistics reported in the paper and the data preparation needed to collect the `final dataset` folder

- `final dataset`: It contains all the mined data structured as described in the paper. Due to the limitation size, the screenshots are stored in the Zenodo repository available at https://zenodo.org/records/10262075 
  
- `miner_components.py`: It contains all the utilities to download the data from IGDB and HLTB websites 

---


# Installation

The requirements.txt file contains all libraries that need to be in the pip installation in order to entirely reproduce the data gathering process.

Moreover, the code for the HLTB API must be downloaded from https://github.com/dangeloandrea14/hl2b_python_API and locally installed via pip.
This is because the HLTB API version used for this project is a custom version, augmented with the possibility of retrieving more attributes.



