from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from sklearn.linear_model import LinearRegression

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
def linear_regression(X, y):
    lr = LinearRegression()
    lr1 = lr.fit(X, y)
    return(lr1)
print((linear_regression(X,y)))
