import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def dig_sep(i):
    return('{0:,.3f}'.format(i).replace(',', ' '))

if __name__ == '__main__':

    df = pd.read_csv('data.csv')

    X = df.km.values
    y = df.price.values

    X_norm = (X - X.min()) / (X.max() - X.min())

    slope_normalize, intercept = 0.0, 0.0

    plt.ion()
    # for i in range(50):
    #     plt.plot(np.random.random([10, 1]))
    #     plt.draw()
    #     plt.pause(0.0001)
    #     plt.clf()

    SS_tot = sum( (y - y.mean()) ** 2 ) / len(y)

    for _ in range(100000):

        slope_normalize -= 0.001 * sum(
            (estimate_price - fact_price) * milleage
            for (milleage, estimate_price, fact_price) in zip(X_norm, intercept + slope_normalize * X_norm, y)
        ) / len(X_norm)

        intercept -= 0.001 * sum(
            (estimate_price - fact_price)
            for (milleage, estimate_price, fact_price) in zip(X_norm, intercept + slope_normalize * X_norm, y)
        ) / len(X_norm)

        if (0 == _ % 1000):

            slope = slope_normalize / df.km.max()

            estimates = [estimate_price for estimate_price in intercept + slope * X];
            SS_res = sum((estimates - y) ** 2) / len(y)

            plt.scatter(X, y, color='black', alpha=0.7, label='фактические цены продажи')
            plt.plot(X, estimates, color='red', label='линия регрессии')
            plt.xlabel("пробег")
            plt.ylabel("цена")
            plt.legend(loc='upper right')
            plt.draw()
            plt.pause(0.0000001)
            plt.clf()

            plt.text(30000, 4000, 'iter: ' + str(_) + '/ R^2: ' + dig_sep(1 - SS_res/SS_tot),
                     style='italic',
                     bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

    slope = slope_normalize / df.km.max()

    print("intercept (tetha0):", dig_sep(intercept))
    print("slope     (tetha1):   ", dig_sep(slope))

    print()

    # найдем коэффициент детерминации
    y_predict_arr = intercept + slope * X
    SS_res = sum( (y_predict_arr - y)**2 ) / len(y)
    print("SS_res:  ", dig_sep(SS_res))
    SS_tot = sum( (y - y.mean()) ** 2 ) / len(y)
    print("SS_tot:", dig_sep(SS_tot))
    print("R^2   :", 1 - SS_res/SS_tot)

    try:
        with open ('coefficient.txt', 'w') as file:
            file.write(str(intercept) + " " + str(slope))
    except Exception as e:
        print("Error with file of coefficient:", e)
        sys.exit(0)

    print()
    print("Coefficients had writen in file coefficient.txt")