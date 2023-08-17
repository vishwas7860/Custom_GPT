import pandas as pd
# Load and preprocess the dataset
dataset_path = "dataset.csv"
data = pd.read_csv(dataset_path)

# Combine columns to create prompts
texts = []
for i in range(len(data)):
    texts.append("NAME: "+str(data['Name'][i])+"\nDEPARTMENT: "+str(data['Department Profile'][i])+"\nSPECIALTIES: "+str(data['Specialties'][i])+"\nEDUCATION: "+str(data['Education'][i])+"\nLOCATION: "+str(data['Location'][i])+"\nABOUT: "+str(data['About'][i])+"\nPROFILE LINK: "+str(data['Profile Link'][i]))
    
with open("SOURCE_DOCUMENTS/inputfile.txt", "w") as outfile:
    outfile.write("\n\n\n".join(texts))