from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

### 处理分类变量
def cate_enc(df, cate_vars):
    for var in cate_vars:
        enc = LabelEncoder()
        df[var] = df[var].astype('str')
        df[var] = enc.fit_transform(df[var])
    return df
	
## 分割数据集
def split_data(df,features,target):
	X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)
	return X_train, X_test, y_train, y_test