import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('plots', exist_ok=True)
df = pd.read_csv('data/insurance.csv', header=0)

# Plotting line chart with charges
plt.plot(df['charges'])
plt.title('Charges')
plt.ylabel('Charges')
plt.savefig(f'plots/charges_plot.png', format='png')
plt.clf()

# Plotting histogram for bmi
plt.hist(df['bmi'])
plt.title('BMI')
plt.xlabel('BMI')
plt.ylabel('bmi')
plt.savefig(f'plots/bmi_hist.png', format='png')
plt.clf()

# Plotting scatterplot of age vs charges
plt.scatter(df['age'], df['charges'])
plt.title('Age to Charges')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.savefig(f'plots/age_to_charges.png', format='png')

plt.close()
