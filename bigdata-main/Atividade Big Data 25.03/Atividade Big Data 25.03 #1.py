import pandas as pd
import matplotlib.pyplot as plt

dictCountChocPerCap = {'CH': 11.8,
                       'US': 9.0,
                       'DE': 5.8,
                       'FR': 3.6,
                       'GB': 2.9,
                       'BR': 1.4,
                       'IN': 1.0,
                       'CN': 0.2}

chocoConsupPerCap = [11.8, 9.0, 5.8, 3.6, 2.9, 1.4, 1.0, 0.2]
countries = ['CH', 'US', 'DE', 'FR', 'GB', 'BR', 'IN', 'CN']

serie1 = pd.Series(chocoConsupPerCap, index=countries)

serie1.plot(marker='o', linestyle='-')
plt.xlabel('Country Code')
plt.ylabel('Chocolate Consumption (2022)')
plt.title('Chocolate Consumption by Country (2022)')
plt.show()
