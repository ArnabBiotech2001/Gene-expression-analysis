### Automated RNA-Seq Quality Control & Differential Expression Workflow

### 📌 Project Overview

This repository contains a structural, end-to-end computational pipeline designed to preprocess, analyze, and visualize public RNA-seq datasets from the **Gene Expression Omnibus (GEO)**. The workflow specifically profiles transcriptomic data across multi-sample clinical cohorts, including **pneumonia, COPD, and COVID-19**, to isolate significant differential gene expressions (DEGs) and map biological interactomes. 

### 🛠️ Tech Stack & Tools

* **Programming:** Python 3.x (Pandas, NumPy, BioPython, Matplotlib, Seaborn)
* **Frameworks & Core Tools:** FastQC, GEO2R (limma framework), Google Colab
* **Network Biology:** STRING Database, Cytoscape (v3.x)
* **Version Control:** Git

### ⚙️ Workflow Architecture

1. **Data Retrieval & Preprocessing:** Automated parsing of large-scale genomic data tables and CSV outputs from public GEO cohorts using Python .
2. **Quality Control (QC):** Execution of per-base sequence quality scoring and adapter contamination assessments via FastQC across multi-sample patient matrices.
3. **Differential Expression Analysis:** Utilizing the limma linear modeling framework via GEO2R to statistically determine significantly up-regulated and down-regulated biomarkers.
4. **Network Interactome Modeling:** Exporting statistically filtered DEGs into the STRING database to build confidence-view protein-protein interaction (PPI) networks, followed by topological visualization in Cytoscape.

### 📊 Key Results & Visualizations

* Clean segregation of up-regulated and down-regulated gene targets compiled into structured data frames.
* Functional interactome networks identifying high-degree hub proteins involved in pulmonary inflammation pathways.

*📈 [Optional: Upload a JPEG/PNG image of a Volcano Plot, Bar Chart, or your Cytoscape Network directly into your repository and embed it here!]* 

### 🚀 How to Run the Pipeline

1. Clone the repository: 

bash

git clone https://github.com/ArnabBiotech2001/RNAseq-Transcriptomics-Workflow.git

Use code with caution.
2. Open the .ipynb file in Google Colab or your local Jupyter environment.
3. Install necessary dependencies: 

bash

pip install pandas numpy biopython matplotlib seaborn

Use code with caution.
4. Run the code blocks sequentially to execute data sorting and automated plotting.

**Author:** Arnab Koley
**Contact:** arnabkoley18@gmail.com | [LinkedIn](https://linkedin.com/in/arnab-koley-150b68237)
