# Integrated Bioinformatics and Machine Learning Pipeline for Lung Disease Biomarker Identification

## 📌 Project Overview
This repository contains a comprehensive computational bioinformatics and machine learning pipeline developed as part of the Biotecnika Bioinformatics, AI & Machine Learning Summer Internship Program (Supervised by Dr. Nilofer Shaikh)[cite: 2]. 

The project investigates the shared molecular signatures, potential biomarkers, and overlapping pathways between **COVID-19**, **Chronic Obstructive Pulmonary Disease (COPD)**, and **Pneumonia** using publicly available transcriptomics datasets from the NCBI-GEO database[cite: 2].

---

## 🗂️ Dataset Collection (NCBI-GEO)
Microarray and RNA-seq gene expression datasets were retrieved and processed:
* **COVID-19:** GSE212865, GSE164805, GSE177477[cite: 2]
* **COPD:** GSE103174, GSE76925[cite: 2]
* **Pneumonia:** GSE48080, GSE133975, GSE47962[cite: 2]

---

## ⚙️ Methodology & Workflow
1. **Differential Gene Expression (DEG) Analysis:** Executed in Python using strict statistical thresholds (Adjusted P-value < 0.05, Absolute logFC $\ge$ 1)[cite: 2].
2. **Machine Learning Regression Modeling:** Evaluated multiple regression algorithms to predict gene expression patterns and prioritize key features[cite: 2]:
   * **XGBoost Regressor:** $R^2 = 0.8242$[cite: 2]
   * **Random Forest Regressor:** $R^2 = 0.8213$[cite: 2]
   * **Gradient Boosting Regressor:** $R^2 = 0.7811$[cite: 2]
3. **Protein-Protein Interaction (PPI) Network:** Constructed using the STRING database and visualized/analyzed in Cytoscape utilizing Cytohubba (MCC algorithm) to identify hub genes[cite: 2].
4. **Functional Enrichment Analysis:** Performed Gene Ontology (GO), KEGG, and Reactome pathway analyses to uncover biological mechanisms[cite: 2].

---

## 🧬 Key Findings & Potential Biomarkers
* **Chemokines & Receptors:** `CXCL10`, `CXCL11`, `CXCL9`, `CXCL2`[cite: 2]
* **Antiviral & Interferon-stimulated Genes:** `RSAD2`, `OASL`, `IFIT1`, `IFI44L`, `MX2`, `HERC5`[cite: 2]
* **Immune Regulation:** `ISG15`, `APOBEC3A`, `CD83`[cite: 2]

---

## 📄 Project Report
* [View Final Project Report Document](./FINAL%20PROJECT%20\(ARNAB\%20KOLEY\).docx)[cite: 2, 5]
