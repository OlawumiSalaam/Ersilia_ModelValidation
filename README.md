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









## Repository organisation
The repository is organised in folders:
- '/notebooks' contains the jupyter notebooks where most of the work is being developed
- '/data' contains all the .csv files. Model predictions are obtained outside this repository and saved in this folder. Subfolders might be created if needed
- '/src' contains important functions I will re-use throughout the repository, to avoid typing them each time
- '/figures' contains the plots I have produced during the model validation process
- 'requirements.txt' lists all the required packages to run the notebooks in this repository. If possible I also specify the version of the package I am using.



## Where to get more help:
- Read Outreachy's contribution [tasks](https://ersilia.gitbook.io/ersilia-book/contributors/internships/outreachy-summer-2024)
- Read Ersilia's [documentation](https://ersilia.gitbook.io/ersilia-book)
- Get inspiration from Ersilia's work, for example on this repository for [data processing](https://github.com/ersilia-os/open-data-cleaning)
- Use Slack to ask the mentors and the other interns for help!

## License
All the code in this repository is licensed under a GPLv3 License.