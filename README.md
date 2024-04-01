# model-validation
##  TASK 1: CHECK FOR MODEL BIAS
The task for this week is to get familiar with Machine Learning for chemistry data, which is going to be the focus of the internship. This is to ensure the models are accurate and reproducible. EOS model ID: eos74bo was selected as the model to work with. I chose the model because Aqueous solubility is an important physicochemical property that influences pharmacokinetic properties of compounds and a very important factor in drug discovery. In this task, the aim to validate the accuracy of predictive models for Kinetic Aqueous Solubility. Our focus will be on validating the eos74bo model for predicting the probability of a compound having poor solubility (< 10 µg/ml). This is crucial for understanding the behavior of molecules in aqueous environments. This will be achieved in the following steps using google Colab environment. Our focus will be on validating the eos74bo model for predicting the  probability of a compound having poor solublibity (< 10 µg/ml). This is crucial for understanding the behavior of molecules in aqueous environments.

## Model Information
Kinetic aqueous solubility (μg/mL) was experimentally determined using the same SOP in over 200 NCATS drug discovery projects. A final dataset of 11780 non-redundant molecules and their associated solubility was used to train a SVM classifier. Approximately half of the dataset has poor solubility < 10 Aqueous Kinetic Solubility
Kinetic aqueous solubility (μg/mL) was experimentally determined using the same SOP in over 200 NCATS drug discovery projects. A final dataset of 11780 non-redundant molecules and their associated solubility was used to train a SVM classifier. Approximately half of the dataset has poor solubility (< 10 μg/mL), and two-thirds of these low soluble molecules report values of < 1 μg/mL. A subset of the data used is available at PubChem (AID 1645848).
Identifiers
•	EOS model ID: eos74bo
•	Slug: ncats-solubility
Characteristics 
•	Input: Compound
•	Input Shape: Single
•	Task: Classification
•	Output: Probability
•	Output Type: Float
•	Output Shape: Single
•	Interpretation: Probability of a compound having poor solublibity (< 10 µg/ml)

This will was achieved in the following steps:
•	Import necessary libraries
•	Data preprocessing
•	Model bias evaluation


• I installed and Imported necessary libraries such as miniconda, rkidit, pandas, numpy, matplotlib and specified neccessary folder path in my mounted google drive.

• Data preprocessing The model was tested on 1000 molecules from public repositories they are represented as standard SMILES. The data is in the input folder in the data folder I loaded a list of molecules I obtained from ChEMBL and processed them to make sure I have Standard SMILES representation of the compound and InChIKey associated to the compound. This was done by applying the standardise_smile function and inchikey function i defined in my src folder. After that, the standardise smiles was converted into a list.This was necessary because that is accepted data format of the model

• Model bias evaluation.
The model was fetched and served from the ersilia model hub and ready to be used for predictions on a new data. The "predict api" was used and output was generated. The model was tested on 1000 molecules from public repositories they are represented as standard SMILES.The predictions (output) was saved into a csv file in the output folder located in the data folder and visualisation was done with plotting histogram, distplot and barchart using matplotlib and seaborn library respectively. 

# Conclusion

Comparing the model information with predictions the model generated, it can be inferred that the model is not biased from the visualisation above. The model was able generate that half of the dataset has poor solubility i.e almost equal percentage of the two classes


# Task 2

MODEL REPRODUCIBILITY
The task is to identify a result I can reproduce from the publication of the ADME model I chose which is NCATS@ADME.
The task is to reproduce the result of ADME@NCATS Solubility model as described by the author in this Publication. I will be worked on a subset of training data and is made available in the PubChem database. The experimental data associated with the compounds are open for public access. The dataset has 2532 records and the details can be found in [PubChem AID 1645848](https://pubchem.ncbi.nlm.nih.gov/bioassay/1645848) . I aim to reproduce this result- AUC-ROC: 0.93 +/– 0.00 from the 5 fold cross validation in [author publication](https://slas-discovery.org/article/S2472-5552(22)06765-X/fulltext#t2). The detailed notebook for implementation is found [here.](https://github.com/OlawumiSalaam/Ersilia_ModelValidation/blob/main/notebooks/GCNN_implement.ipynb)

Also, The second task is to check that the author's model which is ADME@NCATS provides the same results when running via the Ersilia Model Hub(eos74bo) which was done by running predictions with a subset of NPC marketed drug that was downloaded from attached [supplemental material.](https://slas-discovery.org/article/S2472-5552(22)06765-X/fulltext#t2). A detailed notebook is found [here.](https://github.com/OlawumiSalaam/Ersilia_ModelValidation/blob/main/notebooks/Ersilia_Model_eos74bo.ipynb).
To improve the quality of my contributions, I need to ensure the result is accurate and reliable. I ensured the data was cleaned to achieve data quality in this [notebook](https://github.com/OlawumiSalaam/Ersilia_ModelValidation/blob/main/notebooks_updated/eos74bo_validation_data_cleaning.ipynb) before reproducing the result.

# Conclusion

I was able to achieve the same result with the eos74bo model on Ersilia Model Hub and ADME@NCATS model by the author.










## Repository organisation
The repository is organised in folders:
- '/notebooks' contains the jupyter notebooks where most of the work is being developed
- '/notebook_updated contains jupyter notebook for getting predictions on the author's model and eos74bo model with cleaned NPC data. It also contain jupyter notebook for cleaning the NPC data.
- '/data' contains all the .csv files. Model predictions are obtained outside this repository and saved in this folder. Input folder has model_bias_input that contains csv data used for model bias checking(Week 2 Task 1) and csv files for model reproducibility are in eos74bo_author_validation subfolder(week2 Task 2). The output folder contains the corresponding subfolder for outputs in csv format. 
- '/src' contains important functions I will re-use throughout the repository, to avoid typing them each time
- '/Plots' contains the plots I have produced during the model validation process
- 'requirements.txt' lists all the required packages to run the notebooks in this repository. If possible I also specify the version of the package I am using.



## Where to get more help:
- Read Outreachy's contribution [tasks](https://ersilia.gitbook.io/ersilia-book/contributors/internships/outreachy-summer-2024)
- Read Ersilia's [documentation](https://ersilia.gitbook.io/ersilia-book)
- Get inspiration from Ersilia's work, for example on this repository for [data processing](https://github.com/ersilia-os/open-data-cleaning)
- Use Slack to ask the mentors and the other interns for help!

## License
All the code in this repository is licensed under a GPLv3 License.