# model-validation-example
This is an example of the model validation repository for the Outreachy contributors 2024. 	In this task, the aim is to validate the accuracy of predictive model for Kinetic Aqueous Solubility. Our focus will be on validating the eos74bo model for predicting the  probability of a compound having poor solublibity (< 10 µg/ml). This is crucial for understanding the behavior of molecules in aqueous environments.
This will be achieved in the following steps:
•	Import necessary libraries
•	Data preprocessing
•	Model bias evaluation
The model was tested on 1000 molecules from public repositories they are represented as standard SMILES

## Model Information
Kinetic aqueous solubility (μg/mL) was experimentally determined using the same SOP in over 200 NCATS drug discovery projects. A final dataset of 11780 non-redundant molecules and their associated solubility was used to train a SVM classifier. Approximately half of the dataset has poor solubility (< 10 Aqueous Kinetic Solubility
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