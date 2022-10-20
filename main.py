# Import the necessary modules
import csv
import matplotlib.pyplot as plt
import pandas as pd

# ============================================================================

# https://acervolima.com/como-tracar-o-grafico-de-barras-em-python-usando-um-arquivo-csv/

# ============================================================================
# Reduce the database to just essential records
# ---------

# with open("./avocado.csv", 'r') as file:
#   csvreader = csv.reader(file)
#   with open("reduced_avocado.csv", 'w') as reducedFile:
#     for row in csvreader:
#       reducedFile.write(f"{row[2]},{row[3]},{row[12]},{row[13]}\n")

# ------------------------
# AveragePricew -> row[2]
# Total Volume  -> row[3]
# Year          -> row[12]
# Region        -> row[13]
# ------------------------

# ============================================================================
# Read all data in the reduced_avocado.csv file
# ---------

# with open("./reduced_avocado.csv", 'r') as file:
#   csvreader = csv.reader(file)
#   for row in csvreader:
#     print(row[0], row[1], row[2], row[3])

# ============================================================================


# Plot a graphic sold x year

  
# Initialize the lists for X and Y
data = pd.read_csv('reduced_avocado.csv')
  
df = pd.DataFrame(data)
  
Y = list(df.iloc[:, 1])
X = list(df.iloc[:, 2])
  
# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.ticklabel_format(style='plain', axis='y')
plt.title("Vendas por Ano")
plt.xlabel("Ano")
plt.ylabel("Vendas")
  
# Show the plot
plt.show()

