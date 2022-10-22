# Coded by W_K.O
# https://github.com/wko8

# Import the necessary modules
from cmath import sqrt
import csv
import matplotlib.pyplot as plt
import pandas as pd


# ============================================================================


def reducedAvocado():
    # Reduce the database to just essential records
    # ---------

    with open("./csv/avocado.csv", 'r') as file:
      csvreader = csv.reader(file)
      with open("./csv/reduced_avocado.csv", 'w') as reducedFile:
        for row in csvreader:
            reducedFile.write(f"{row[2]},{row[12]},{row[13]}\n")


# ============================================================================

# Exploratory data analysis
# ---------

# ============================================================================


def mean():
    # Mean
    # ---------

    count_rows = 1
    count_regions = -1
    region_sum = []

    with open("./csv/reduced_avocado.csv", 'r') as file:
      csvreader = csv.reader(file)
      for row in csvreader:
        if row[2] == "END":
                region_sum[count_regions] = float(region_sum[count_regions])/count_rows
                break
        if row[2] not in region_sum:
            if count_regions > 0:
                region_sum[count_regions] = float(region_sum[count_regions])/count_rows
                count_rows = 1

            count_regions += 2

            region_sum.insert(count_regions - 1, row[2])
            region_sum.insert(count_regions, float(row[0]))

        else:
            region_sum[count_regions] += float(row[0])

        count_rows += 1

    # Writting the average in the avg_avocado.csv file
    # ---------

    with open("./csv/avg_avocado.csv", 'w') as file:
        file.write(f"average, region\n")
        for c in range(0, count_regions, 2):
            file.write(f"{region_sum[c + 1]:.2f},{region_sum[c]}\n")


# ============================================================================


def graphAvgPriceByRegion():
    # Plotting a horizontal bar graph (AveragePrice x region)
    # ---------

    # Initialize the lists for X and Y
    data = pd.read_csv('./csv/avg_avocado.csv')
    
    df = pd.DataFrame(data)


    font = {'family': 'sans-serif',
            'color':  'darkred',
            'weight': 'normal',
            'size': 8,
            }
    
    X = list(df.iloc[:, 1])
    Y = list(df.iloc[:, 0])
    
    # Plot the data using bar() method
    plt.barh(X, Y)

    for index, value in enumerate(Y): 
        plt.text(value, index, str(value), fontdict=font)

    plt.title("AveragePrice x Region")
    plt.ylabel("Region")
    plt.xlabel("AveragePrice")
    
    # Show the plot
    plt.show()


# ============================================================================


def median():
    # Median
    # ---------

    # Assign dataset
    csvData = pd.read_csv("./csv/reduced_avocado.csv")
    
    # Sort data frame 
    csvData.sort_values([csvData.columns[2], csvData.columns[0]], 
                        axis=0,
                        ascending=[True, True], 
                        inplace=True)

    df = pd.DataFrame(csvData)
    df.to_csv("./csv/sorted_avocado.csv", index=False)

    # Counting the records lines of each region

    regions = []
    recordsLines = 1
    linesByRegions = []

    with open("./csv/sorted_avocado.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[2] not in regions:
                if recordsLines > 1:
                    linesByRegions.append(recordsLines)
                    recordsLines = 1
                regions.append(row[2])
            recordsLines += 1

    # print(regions)
    # print(linesByRegions)

    # Save the median of the averagePrice by each region

    regionsB = []
    recordsLinesB = 1
    medians = []

    with open("./csv/sorted_avocado.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[2] not in regionsB:
                regionsB.append(row[2])
            if recordsLinesB == 170:
                medians.append(row[0])
            if recordsLinesB == 339:
                recordsLinesB = 1

            recordsLinesB += 1

    # Remove region record of the list
    # regionsB.remove('region')
    regionsB.remove('END')

    # Writting the medians in the medians_avocado.csv file
    # ---------

    print(len(regionsB))

    with open("./csv/medians_avocado.csv", 'w') as file:
        file.write(f"medians, regions\n")
        for c in range(0, len(regionsB)):
            file.write(f"{medians[c]},{regionsB[c]}\n")


# ============================================================================


def graphMedianByRegion():
    # Plotting a horizontal bar graph (median x region)
    # ---------

    # Initialize the lists for X and Y
    data = pd.read_csv('./csv/medians_avocado.csv')
    
    df = pd.DataFrame(data)


    font = {'family': 'sans-serif',
            'color':  'darkred',
            'weight': 'normal',
            'size': 8,
            }
    
    X = list(df.iloc[:, 1])
    Y = list(df.iloc[:, 0])
    
    # Plot the data using bar() method
    plt.barh(X, Y)

    for index, value in enumerate(Y): 
        plt.text(value, index, str(value), fontdict=font)

    plt.title("Median x Region")
    plt.ylabel("Region")
    plt.xlabel("Median")
    
    # Show the plot
    plt.show()


# ============================================================================


def mode():
    # Mode
    # ---------

    # Getting the most repeated averagePrice in each region

    regions = []
    avgPrice = []
    tmpMode = []
    mode = []

    with open("./csv/sorted_avocado.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[3] not in regions:
                if len(regions) > 0:
                    quantityMode = 0
                    for num in tmpMode:
                        if num > quantityMode:
                            quantityMode = num

                    idxMode = tmpMode.index(quantityMode)

                    mode.append(avgPrice[idxMode])
                    avgPrice = []
                    tmpMode = []

                regions.append(row[3])
            if row[0] not in avgPrice:
                avgPrice.append(row[0])
                tmpMode.append(0)
            else:
                idx = avgPrice.index(row[0])
                tmpMode[idx] += 1

    # Remove 'END' record of the list
    regions.remove('END')

    # Writting the mode in the mode_avocado.csv file
    # ---------

    with open("./csv/mode_avocado.csv", 'w') as file:
        file.write(f"mode, region\n")
        for c in range(0, len(regions)):
            file.write(f"{mode[c]},{regions[c]}\n")


# ============================================================================

def graphModeByRegion():

    # Plotting a horizontal bar graph (mode x region)
    # ---------

    # Initialize the lists for X and Y
    data = pd.read_csv('./csv/mode_avocado.csv')
    
    df = pd.DataFrame(data)


    font = {'family': 'sans-serif',
            'color':  'darkred',
            'weight': 'normal',
            'size': 8,
            }
    
    X = list(df.iloc[:, 1])
    Y = list(df.iloc[:, 0])
    
    # # Plot the data using bar() method
    plt.barh(X, Y)

    for index, value in enumerate(Y): 
        plt.text(value, index, str(value), fontdict=font)

    plt.title("Mode x Region")
    plt.ylabel("Region")
    plt.xlabel("Mode")
    
    # Show the plot
    plt.show()


# ============================================================================


def standardDeviation():
    # Standard deviation
    # ---------

    # Getting the standard deviation of the averagePrice in each region

    regions = [] # OK
    avg = [] # OK
    avgPrice = [] # OK
    qnt = 338
    sumData = [] # OK
    tmpSumData = [] # ~
    countLines = 0
    stdDeviation = [] # ~

    # Filling the avg list
    with open("./csv/avg_avocado.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            avg.append(row[0])

        # Remove average record of the list
        avg.remove('average')


    # Filling the avgPrice and regions lists
    with open("./csv/sorted_avocado.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[3] not in regions:
                regions.append(row[3])
                avgPrice.append(float(row[0]))
            else:
                avgPrice.append(float(row[0]))

        # Remove 'END' and 0.0 records of the lists
        regions.remove('END')
        avgPrice.remove(0.0)


    # Filling the sumData list
    for c in range(len(avg)):
        for k in range(qnt):
            power = pow(float(avgPrice[k]) - float(avg[c]), 2)
            sumData.append(power)


    # Filling the stdDeviation list
    for c in range(len(sumData)):
        if countLines == 337:
            squareRoot = sqrt(sum(tmpSumData)/qnt-1)
            # Remove the letter j at the end of the numbers and leave them with just two digits after the floating point
            squareRoot = float(f"{float(str(squareRoot).replace('j', '')):.2f}")
            stdDeviation.append(squareRoot)
            tmpSumData = []
            countLines = 0
        tmpSumData.append(sumData[c])
        countLines += 1

    # print(regions)
    # print(stdDeviation)


    # Writting the standard deviation in the std_deviation_avocado.csv file
    # ---------

    with open("./csv/std_deviation_avocado.csv", 'w') as file:
        file.write(f"stdDeviation,region\n")
        for c in range(len(regions)):
            file.write(f"{stdDeviation[c]},{regions[c]}\n")


# ============================================================================


def graphStdDeviationByRegion():
    # Plotting a horizontal bar graph (standard deviation x region)
    # ---------

    # Initialize the lists for X and Y
    data = pd.read_csv('./csv/std_deviation_avocado.csv')
    
    df = pd.DataFrame(data)


    font = {'family': 'sans-serif',
            'color':  'darkred',
            'weight': 'normal',
            'size': 8,
            }
    
    X = list(df.iloc[:, 1])
    Y = list(df.iloc[:, 0])
    
    # Plot the data using bar() method
    plt.barh(X, Y)

    for index, value in enumerate(Y): 
        plt.text(value, index, str(value), fontdict=font)

    plt.title("Standard Deviation x Region")
    plt.ylabel("Region")
    plt.xlabel("Standard Deviation")
    
    # # Show the plot
    plt.show()


# ============================================================================

def avgPriceOfRegionByYear():
    # Separating the average avocado price of each region by year and saving in their respective files
    # ---------

    regions = ['Albany', 'Atlanta', 'BaltimoreWashington', 'Boise', 'Boston', 'BuffaloRochester', 'California', 'Charlotte', 'Chicago', 'CincinnatiDayton', 'Columbus', 'DallasFtWorth', 'Denver', 'Detroit', 'GrandRapids', 'GreatLakes', 'HarrisburgScranton', 'HartfordSpringfield', 'Houston', 'Indianapolis', 'Jacksonville', 'LasVegas', 'LosAngeles', 'Louisville', 'MiamiFtLauderdale', 'Midsouth', 'Nashville', 'NewOrleansMobile', 'NewYork', 'Northeast', 'NorthernNewEngland', 'Orlando', 'Philadelphia', 'PhoenixTucson', 'Pittsburgh', 'Plains', 'Portland', 'RaleighGreensboro', 'RichmondNorfolk', 'Roanoke', 'Sacramento', 'SanDiego', 'SanFrancisco', 'Seattle', 'SouthCarolina', 'SouthCentral', 'Southeast', 'Spokane', 'StLouis', 'Syracuse', 'Tampa', 'TotalUS', 'West', 'WestTexNewMexico']
    years = ['2017']
    avg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    with open("./csv/reduced_avocado.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[1] in years and row[2] in regions:
                avg[regions.index(row[2])] += float(row[0])

    for c in range(len(avg)):
        res = float(f"{float(str(avg[c] / 54)):.2f}")
        avg[c] = res

    # Writting the standard deviation in the 201?_avocado.csv file
    # ---------

    with open("./csv/2017_avocado.csv", 'w') as file:
        file.write(f"region, 2017\n")
        for c in range(len(regions)):
            file.write(f"{regions[c]},{avg[c]}\n")


# ============================================================================