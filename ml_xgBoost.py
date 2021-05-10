from xgboost import XGBClassifier
from xgboost import plot_importance
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd

iris = pd.read_csv("./data/iris.csv")
iris.info()

cols = list(iris.columns)
print(cols)

cols_x = cols[:4]
cols_y = cols[-1]

#   ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
print(cols_x)
# 'Species'
print(cols_y)

iris_train, iris_test = train_test_split(iris, test_size=0.2, random_state=123)

#(120, 5)
iris_train.shape
#(30, 5)
iris_test.shape

# n_estimators(매개변수) = 100: 트리플 100개 사용
# min_child_weight = 1 : 노드를 분할할때 사용한 설명변수 개수
# object='multi:softprob' : 다항분류 (자동으로 설정되는 값)
model = XGBClassifier()
model.fit(X=iris_train[cols_x], y=iris_train[cols_y])

fscore = model.get_booster().get_fscore()

plot_importance(model)