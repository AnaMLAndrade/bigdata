import pandas as pd
import matplotlib.pyplot as plt

dictHappyScore = {'CH': 7.24,
                  'US': 6.89,
                  'DE': 7.59,
                  'FR': 6.66,
                  'GB': 6.80,
                  'BR': 6.12,
                  'IN': 4.04,
                  'CN': 5.82}

happyCountriesScore = [7.24, 6.89, 7.59, 6.66, 6.80, 6.12, 4.04, 5.82]

happycountries = ['CH', 'US', 'DE', 'FR', 'GB', 'BR', 'IN', 'CN']

serie2 = pd.Series(happyCountriesScore, index=happycountries)

serie2.plot(marker='o', linestyle='-')
plt.xlabel('Country')
plt.ylabel('Happiness Score (2022)')
plt.title('Happiness Score by Country (2022)')
plt.show()
