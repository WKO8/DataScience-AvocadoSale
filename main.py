# Import the necessary modules
import csv
from tkinter import W
from traceback import print_tb
import matplotlib.pyplot as plt
import pandas as pd



# ============================================================================

# https://acervolima.com/como-tracar-o-grafico-de-barras-em-python-usando-um-arquivo-csv/

# ============================================================================
# Reduce the database to just essential records
# ---------

# with open("./csv/avocado.csv", 'r') as file:
#   csvreader = csv.reader(file)
#   with open("./csv/reduced_avocado.csv", 'w') as reducedFile:
#     for row in csvreader:
#       reducedFile.write(f"{row[2]},{row[3]},{row[12]},{row[13]}\n")

# ------------------------
# AveragePrice,Total Volume,year,region
# ------------------------
# AveragePricew -> row[2]
# Total Volume  -> row[3]
# Year          -> row[12]
# Region        -> row[13]
# ------------------------

# ============================================================================
# Reading all data in the reduced_avocado.csv file
# ---------

# with open("./csv/reduced_avocado.csv", 'r') as file:
#   csvreader = csv.reader(file)
#   for row in csvreader:
#     print(row[0], row[1], row[2], row[3])

# ============================================================================


# Plotting a graph  (sold x year)
# ---------

# Initialize the lists for X and Y
# data = pd.read_csv('./csv/reduced_avocado.csv')
  
# df = pd.DataFrame(data)
  
# Y = list(df.iloc[:, 0])
# X = list(df.iloc[:, 1])
  
# # Plot the data using bar() method
# # plt.bar(Y, X, width=0.5, color='g')
# plt.scatter(Y, X, linewidths=0.5, c='k')
# plt.ticklabel_format(style='plain', axis='y')
# plt.title("Taxa x Venda")
# plt.ylabel("Vendas")
# plt.xlabel("Taxas")
  
# # Show the plot
# plt.show()

# ============================================================================

# Exploratory data analysis
# ---------

# Mean
# ---------

# sum = 0
# count_rows = 1
# count_regions = -1
# region_sum = []

# with open("./csv/reduced_avocado.csv", 'r') as file:
#   csvreader = csv.reader(file)
#   for row in csvreader:
#     if row[3] == "END":
#             region_sum[count_regions] = float(region_sum[count_regions])/count_rows
#             break
#     if row[3] not in region_sum:
#         if count_regions > 0:
#             region_sum[count_regions] = float(region_sum[count_regions])/count_rows
#             count_rows = 1

#         count_regions += 2

#         region_sum.insert(count_regions - 1, row[3])
#         region_sum.insert(count_regions, float(row[0]))

#     else:
#         region_sum[count_regions] += float(row[0])

#     count_rows += 1

# Writting the average in the avg_avocado.csv file
# ---------

# with open("./csv/avg_avocado.csv", 'w') as file:
#     file.write(f"average, region\n")
#     for c in range(0, count_regions, 2):
#         file.write(f"{region_sum[c + 1]:.2f},{region_sum[c]}\n")


# ============================================================================

# Plotting a graph  (AveragePrice x region)
# ---------

# Reading all data in the reduced_avocado.csv file
# ---------

# with open("./csv/avg_avocado.csv", 'r') as file:
#   csvreader = csv.reader(file)
#   for row in csvreader:
#     print(row[0],row[1])

# ============================================================================


# Plotting a horizontal bar graph (AveragePrice x region)
# ---------

# # Initialize the lists for X and Y
# data = pd.read_csv('./csv/avg_avocado.csv')
  
# df = pd.DataFrame(data)


# font = {'family': 'sans-serif',
#         'color':  'darkred',
#         'weight': 'normal',
#         'size': 8,
#         }
  
# X = list(df.iloc[:, 1])
# Y = list(df.iloc[:, 0])
  
# # # Plot the data using bar() method
# plt.barh(X, Y)

# for index, value in enumerate(Y): 
#     plt.text(value, index, str(value), fontdict=font)

# plt.title("AveragePrice x Region")
# plt.ylabel("Region")
# plt.xlabel("AveragePrice")
  
# # # Show the plot
# plt.show()

# ============================================================================

# Median
# ---------

# Assign dataset
# csvData = pd.read_csv("./csv/reduced_avocado.csv")
  
# # Sort data frame 
# csvData.sort_values([csvData.columns[3], csvData.columns[0]], 
#                     axis=0,
#                     ascending=[True, True], 
#                     inplace=True)

# df = pd.DataFrame(csvData)
# df.to_csv("./csv/sorted_avocado.csv", index=False)

# Counting the records lines of each region

# regions = []
# recordsLines = 1
# linesByRegions = []

# with open("./csv/sorted_avocado.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         if row[3] not in regions:
#             if recordsLines > 1:
#                 linesByRegions.append(recordsLines)
#                 recordsLines = 1
#             regions.append(row[3])
#         recordsLines += 1

# print(regions)
# print(linesByRegions)

# Save the median of the averagePrice by each region

# regions = []
# recordsLines = 1
# medians = []

# with open("./csv/sorted_avocado.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         if row[3] not in regions:
#             regions.append(row[3])
#         if recordsLines == 170:
#             medians.append(row[0])
#         if recordsLines == 339:
#             recordsLines = 1

#         recordsLines += 1

# Remove region record of the list
# regions.remove('region')
# regions.remove('END')

# Writting the medians in the medians_avocado.csv file
# ---------

# with open("./csv/medians_avocado.csv", 'w') as file:
#     file.write(f"medians, regions\n")
#     for c in range(0, len(regions)):
#         file.write(f"{medians[c]},{regions[c]}\n")


# # ============================================================================


# Plotting a horizontal bar graph (median x region)
# ---------

# Initialize the lists for X and Y
# data = pd.read_csv('./csv/medians_avocado.csv')
  
# df = pd.DataFrame(data)


# font = {'family': 'sans-serif',
#         'color':  'darkred',
#         'weight': 'normal',
#         'size': 8,
#         }
  
# X = list(df.iloc[:, 1])
# Y = list(df.iloc[:, 0])
  
# # # Plot the data using bar() method
# plt.barh(X, Y)

# for index, value in enumerate(Y): 
#     plt.text(value, index, str(value), fontdict=font)

# plt.title("Median x Region")
# plt.ylabel("Region")
# plt.xlabel("Median")
  
# # # Show the plot
# plt.show()

# ============================================================================

# Mode
# ---------

# Save the mode of the averagePrice by each region

regions = []
avgPrice = []
mode = []

with open("./csv/sorted_avocado.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if row[3] not in regions:
            regions.append(row[3])
        if row[0] not in avgPrice:
            avgPrice.append(row[0])
            mode.append(0)
        if row[0] in avgPrice:
            idx = regions.index(row[3])
            mode[idx] += 1

# Remove region record of the list
# regions.remove('region')
# regions.remove('END')

print(regions)
print(avgPrice)
print(mode)


# Writting the medians in the medians_avocado.csv file
# ---------

# with open("./medians_avocado.csv", 'w') as file:
#     file.write(f"medians, regions\n")
#     for c in range(0, len(regions)):
#         file.write(f"{medians[c]},{regions[c]}\n")


