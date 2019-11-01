import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
 


def plot_ROC(y_test, y_pred, title):
    false_positive_rate, recall, thresholds = roc_curve(y_test, y_pred)
    roc_auc = auc(false_positive_rate, recall)
    fig = plt.gcf()
    plt.title(title, fontsize=15)
    #ks_index = np.argmax(recall-false_positive_rate)
    #plt.plot([false_positive_rate[ks_index],false_positive_rate[ks_index]],
     #        [false_positive_rate[ks_index], recall[ks_index]],'r')
    plt.plot(false_positive_rate, recall, 'b', label='AUC = %0.2f' % roc_auc)  # AUC值
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.ylabel('Recall', fontsize=15)
    plt.xlabel('Fall-out', fontsize=15)
    fig.set_size_inches(10, 6)
    plt.savefig('./figures/'+title+'.png')
    plt.show()
    
    print('AUC: ',roc_auc)
    print('KS: ',max(recall-false_positive_rate))