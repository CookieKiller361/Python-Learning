import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

xpoints=np.array([0,17])
ypoint=np.array([0,10])
plt.plot(xpoints,ypoint)
plt.show()

xpoint=[0,17]
ypoint=[0,10]
plt.plot(xpoint,ypoint,'|')
plt.show()
plt.plot(xpoint,ypoint,'_')
plt.show()

'''#x= np.random.normal(size=(100))
#sns.displot(x)
x = np.random.normal(loc=1, scale=2, size=(2, 3))
#x=np.array(x)
sns.displot(x)
plt.show()
'''
sns.histplot(np.random.normal(size=1000))

plt.show()


