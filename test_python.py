import matplotlib.pyplot as plt #used for plotting
from scipy import stats #used for linear rergression
from scipy.stats import norm


# initialise variables

Y=[] #Value to be predicted (Dependent Variable)
X=[] #Value to determine expected movement of Y (Independent Variable)

#import data from source

e.g
-sqlite
-mysql
-url

# Simple Linear Regression

lin_vars = slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y) #perform linear regression model to get Intercept and Slope
Y_Hat = X * liv_vars.slope + intercept #use Intercept and Slope to output expected Y ("Y Hat")

#visualise the expected outputs 

plt.plot(Y_Hat) #plot Y Hat
plt.show() #show plot
