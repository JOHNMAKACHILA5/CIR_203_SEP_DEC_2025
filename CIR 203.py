
import numpy as np

# Sample transaction volumes (rows: branches, columns: months)
transactions = np.array([
    [1200, 1350, 1600, 1450, 1700, 1550],  # Branch 1
    [1100, 1250, 1400, 1300, 1500, 1350],  # Branch 2
    [1000, 1150, 1300, 1200, 1400, 1250],  # Branch 3
    [900, 1050, 1200, 1100, 1300, 1150]    # Branch 4
])
# Total Transactions per Branch (4 marks)
total_per_branch = np.sum(transactions, axis=1)
print("Total transactions per branch:", total_per_branch)

# Branch with Highest Total Transactions (4 marks)
highest_branch_index = np.argmax(total_per_branch)
print("Branch with highest total transactions:", highest_branch_index + 1)
# Average Monthly Transaction Volume Across All Branches (4 marks)
average_monthly_volume = np.mean(transactions, axis=0)
print("Average monthly transaction volume:", average_monthly_volume)
# Reshape to 3x8 and Explain (4 marks)
reshaped = transactions.reshape(3, 8)
print("Reshaped array (3x8):\n", reshaped)
# Implications of Reshaping:
#
# Reshaping changes the structure but not the data.
#
# The original 4x6 array (24 elements) is reorganized into 3 rows and 8 columns.
#
# This may obscure the original branch/month meaning unless reinterpreted.
#
# Useful for feeding data into models that expect different input shapes.