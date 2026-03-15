# bioinfo_case_stu
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

### How to Run the Pipeline:
1. **Clone the Repo:**
```bash
git clone https://github.com/beyzabyr/bioinfo_case_stu
cd bioinfo_case_stu
```

2. **Setup the Environment: (Requires Conda/Miniconda)**
```bash
conda env create -f environment.yml
conda activate longread_qc_env
```

3. **Execute: Place your FASTQ file in data/sample.fastq and run:**
```bash
snakemake --cores 1
```
---

## Email Draft to Professor Kılıç
---

> **Context:** This section contains the professional communication sent to the lead researcher regarding the data quality and project status.

**Subject:** [Massive Bioinformatics] Summary of Sequencing Results and Quality Assessment

**Dear Professor Kılıç,**

As part of the **Massive Bioinformatics** team, I have completed the initial assessment of the raw long-read sequencing data you provided. 

My goal was to "clean and check" the data to ensure it is of high enough quality before we spend time and resources on the full alignment process. I have processed the file through our automated pipeline, and here is a clear summary of what the data looks like:

### **1. How Good is the Quality? (Read Accuracy)**
The average quality score is **17.90**. In simple terms, this is an **excellent result** for long-read technology. It means that the sequencing machine was very confident in identifying each letter of the DNA, with an accuracy rate of over 98%. This is a "green light" for us.

### **2. How Long are the Reads? (Read Length)**
On average, each piece of DNA we sequenced is about **1,038 letters (bp)** long. 
* **Observation:** This is slightly shorter than what we usually expect from a perfect long-read run.
* **Interpretation:** It suggests that the DNA might have been slightly fragmented during the lab preparation. However, since the quality of these pieces is so high, this should not cause major issues in the next steps.

### **3. Biological Consistency (GC Content)**
The "GC Content" is at **53%**. This is very stable and follows a normal pattern, meaning there are no signs of contamination or technical errors.

### **Recommendation: Proceed with Alignment**
Even though the DNA pieces are shorter than ideal, their **high accuracy** makes this data very viable. We believe the results of the alignment will be highly reliable.

**Next Steps:**
We are ready to move forward with the full alignment. You can find the visual charts (histograms) in the `results/` folder of this repository, and the automated pipeline logic in the `Snakefile`.

Please let me know if you would like me to trigger the next phase of the analysis or if you have any questions regarding these metrics.

Best regards,

**Beyza Bayır** 
*Bioinformatics Analysis Specialist* 
**Massive Bioinformatics**
