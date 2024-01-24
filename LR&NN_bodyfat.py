import numpy as np
#پیاده_سازی_فرمول_همبستگی
import scipy.stats as stt
#مدل خطی
import sklearn.linear_model as li
#ایجاد شبکه عصبی
import sklearn.neural_network as nn
#برای نرمالایز نمودن
import sklearn.preprocessing as pp
#جدانمودن x ها
import sklearn.model_selection as ms
#حذف correlation
import sklearn.decomposition as dec
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
#برسی کل موارد نمودار
def result(model,trX,teX,trY,teY):
    #ضریب تعین (مقدار درستی  رگرسیون خطی)
    r2tr=model.score(trX,trY)
    r2te=model.score(teX,teY)

    print(f'Train R2 score: {round(r2tr,6)}')
    print(f'Test R2 score: {round(r2te,6)}')

    # برای  8 مقدار pca پیش بینی مدل با استفاده از یک ضرایبی
    #print(lr.coef_)
    #print(lr.intercept_)
    #نمودار پیش بینی
    tr_pred=model.predict(trX)
    te_pred=model.predict(teX)

    a=min([np.min(tr_pred),np.min(te_pred),0])
    b=max([np.max(tr_pred),np.max(te_pred),1])
    plt.subplot(1,2,1)
    plt.scatter(trY2,tr_pred,s=12,c='teal')
    plt.plot([a,b],[a,b],c='crimson',lw=1.2,label='y=x')
    plt.title(f'Train [R2= {round(r2tr,4)}]')
    plt.xlabel('Targte Values')
    plt.ylabel('Predicted Values')
    plt.legend()

    plt.subplot(1,2,2)
    plt.scatter(teY2,te_pred,s=12,c='teal')
    plt.plot([a,b],[a,b],c='crimson',lw=1.2,label='y=x')
    plt.title(f'Test [R2= {round(r2te,4)}]')
    plt.xlabel('Targte Values')
    plt.ylabel('Predicted Values')
    plt.legend()

    plt.show()

#برسی داده های جدول body fat
data_frame=pd.read_csv('bodyfat.csv',sep=',',header=0,encoding='utf-8')
#print(data_frame.describe())
#print(data_frame.head(10))
#نمایش هبستگی
#correlation=data_frame.corr()
#نمایش همبستگی بصورت تصویر
#plt.imshow(correlation)
#نمایش  بین -1 و 1scle
#sb.heatmap(correlation ,vmin=-1 ,vmax=+1)
#plt.show()
#نمایش بصورت نمودار
#data_frame.plotting.scatter_matrix()

#مقادیر x و y
Y=data_frame['BodyFat'].to_numpy().reshape((-1 , 1))
data_frame.drop(['BodyFat'],inplace=True,axis=1)
X=data_frame.to_numpy()
#تبدیل کردن به shape
#print(f'{X.shape=}')
#print(f'{Y.shape=}')
#نرمالایز نمودن
trX,teX,trY,teY=ms.train_test_split(X,Y,train_size=0.7,random_state=0)
#  y and xها جدا نمودن
scalerX=pp.MinMaxScaler()
trX2=scalerX.fit_transform(trX)
tex2=scalerX.transform(teX)
scalerY=pp.MinMaxScaler()
trY2=scalerY.fit_transform(trY)
teY2=scalerY.transform(teY)
#حذف corretion
pca=dec.PCA(n_components=0.95)
trX3=pca.fit_transform(trX2)
teX3=pca.transform(tex2)
print(f'{trX.shape=}')
print(f'{teX.shape=}')
#مشخص شدن تعداد corr
#C=np.zeros((8,8))
#for i in range (8):
#    for j in range(8):
#        C[i,j]=stt.pearsonr(trX3[:,i],trX3[:j])[0]
#sb.heatmap(C , vmin= -1 , vmax= +1)
#plt.show()

#ایجاد مدل خطی برای  y and x
lr=li.LinearRegression()
lr.fit(trX3,trY2)
result(lr,trX3,teX3,trY2,teY2)
#ایجاد شبکه عصبی
mlp=nn.MLPRegressor(hidden_layer_sizes=(30,40),activation='relu',random_state=0)
mlp.fit(trX3,trY2)
result(mlp,trX3,teX3,trY2,teY2)