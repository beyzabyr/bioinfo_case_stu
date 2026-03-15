# Mini-Bioinformatics QC Pipeline

## Project Overview
This repository contains a reproducible bioinformatics pipeline for Quality Control (QC) of raw long-read sequencing data. The pipeline is built using **Snakemake** and managed via **Conda**.

### Final Statistics (Full Dataset):
* **Mean Quality Score:** 17.90
* **Mean Read Length:** 1038.24 bp
* **GC Content:** 53.00%

### Tools Used:
* **Workflow Manager:** Snakemake
* **Environment:** Conda (`environment.yml`)
* **QC Tool:** NanoPlot
* **Custom Scripts:** Python (Biopython, Pandas, Seaborn, Matplotlib)

---

## How to Run
1. Create environment: `conda env create -f environment.yml`
2. Activate: `conda activate longread_qc_env`
3. Run: `snakemake --cores 1`

---

## Email Draft to Professor Kılıç
(Email content is included here for evaluation purposes)
Subject: Sequencing Run QC Results & Next Steps Recommendation
... [Içeriği buraya daha sonra mailden de kopyalayabilirsin] ...
