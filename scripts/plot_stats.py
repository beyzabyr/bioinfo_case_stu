import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distributions(csv_input, output_plot, output_stats):
    # Reading CSV file
    df = pd.DataFrame(pd.read_csv(csv_input))
    
    # 1. (Mean & Median)
    stats_df = df[['GC_Content_Percent', 'Read_Length', 'Mean_Quality']].agg(['mean', 'median']).round(2)
    print("--- Temel Özet İstatistikler ---")
    print(stats_df)
    

    stats_df.to_csv(output_stats)

    # Visualisation (Graphics)
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # A. GC Content Density (Histogram + Density)
    sns.histplot(df['GC_Content_Percent'], bins=30, kde=True, ax=axes[0], color='skyblue')
    axes[0].set_title('GC Content Distribution', fontsize=14)
    axes[0].set_xlabel('GC Content (%)')
    
    # read lenght distribution
    sns.histplot(df['Read_Length'], bins=30, kde=True, ax=axes[1], color='lightgreen')
    axes[1].set_title('Read Length Distribution', fontsize=14)
    axes[1].set_xlabel('Read Length (bp)')
    
    # mean quality score distribution
    sns.histplot(df['Mean_Quality'], bins=30, kde=True, ax=axes[2], color='salmon')
    axes[2].set_title('Mean Quality Score Distribution', fontsize=14)
    axes[2].set_xlabel('Phred Quality Score')
    
    # Grafikleri sıkıştırıp estetik hale getiriyoruz ve kaydediyoruz
    plt.tight_layout()
    plt.savefig(output_plot, dpi=300)
    print(f"Grafikler başarıyla {output_plot} konumuna kaydedildi.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Kullanım: python plot_stats.py <girdi.csv> <cikti_grafik.png> <cikti_istatistik.csv>")
        sys.exit(1)
        
    input_csv = sys.argv[1]
    output_img = sys.argv[2]
    out_stats = sys.argv[3]
    
    plot_distributions(input_csv, output_img, out_stats)
