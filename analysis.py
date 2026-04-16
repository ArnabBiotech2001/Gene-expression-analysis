import pandas as pd
import matplotlib.pyplot as plt

# Sample gene expression data
data = {
    "Gene": ["GeneA", "GeneB", "GeneC", "GeneD", "GeneE"],
    "Sample1": [10, 50, 30, 20, 60],
    "Sample2": [15, 55, 35, 25, 65]
}

df = pd.DataFrame(data)
df.set_index("Gene", inplace=True)

# Calculate mean expression
df["Mean_Expression"] = df.mean(axis=1)

# Sort genes
top_genes = df.sort_values(by="Mean_Expression", ascending=False)

print(top_genes)

# Plot
top_genes["Mean_Expression"].plot(kind="bar")
plt.title("Gene Expression Levels")
plt.xlabel("Genes")
plt.ylabel("Expression")
plt.tight_layout()
plt.show()
