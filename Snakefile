# --- Mini-Bioinformatics Pipeline ---
FASTQ_IN = "data/sample.fastq"

rule all:
    input:
        "results/nanoplot/NanoPlot-report.html",
        "results/custom_qc_stats.csv",
        "results/qc_plots.png",
        "results/summary_stats.csv"

# 1: Nanoplot
rule run_nanoplot:
    input:
        FASTQ_IN
    output:
        "results/nanoplot/NanoPlot-report.html"
    shell:
        """
        NanoPlot --fastq {input} -o results/nanoplot/
        """

#  2: QC Statistics
rule run_custom_qc:
    input:
        script = "scripts/qc_stats.py",
        fastq = FASTQ_IN
    output:
        "results/custom_qc_stats.csv"
    shell:
        """
        python {input.script} {input.fastq} {output}
        """

# Süreç 3:Visualisation and summary
rule plot_qc:
    input:
        script = "scripts/plot_stats.py",
        csv = "results/custom_qc_stats.csv"
    output:
        plot = "results/qc_plots.png",
        stats = "results/summary_stats.csv"
    shell:
        """
        python {input.script} {input.csv} {output.plot} {output.stats}
        """
