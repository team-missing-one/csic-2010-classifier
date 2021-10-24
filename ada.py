import csic_parser
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
anomaly_train_raw = "anomal_train.txt"
anomaly_test_raw = "anomal_test.txt"
normal_train_raw = "norm_train.txt"
normal_test_raw = "norm_test.txt"

csic_parser.parse(normal_train_raw, "normal_train.txt")
csic_parser.parse(normal_test_raw, "normal_test.txt")
csic_parser.parse(anomaly_train_raw, "anomaly_train.txt")
csic_parser.parse(anomaly_test_raw, "anomaly_test.txt")

normal_train = csic_parser.load_parsed("normal_train.txt")
normal_train = csic_parser.make_data_set(normal_train, 0)
anomaly_train = csic_parser.load_parsed("anomaly_train.txt")
anomaly_train = csic_parser.make_data_set(anomaly_train, 1)
train_data = csic_parser.combine_data_set(normal_train, anomaly_train)

normal_test = csic_parser.load_parsed("normal_test.txt")
normal_test = csic_parser.make_data_set(normal_test, 0)
anomaly_test = csic_parser.load_parsed("anomaly_test.txt")
anomaly_test = csic_parser.make_data_set(anomaly_test, 1)
test_data = csic_parser.combine_data_set(normal_test, anomaly_test)

vectorizer = TfidfVectorizer(
    min_df=0,
    analyzer="char",
    sublinear_tf=True,
    ngram_range=(3, 3)
)

X_train = train_data["data"]
y_train = train_data["target"]
X_test = test_data["data"]
y_test = test_data["target"]

vectorizer.fit(X_train)
X_train = vectorizer.transform(X_train)
X_test = vectorizer.transform(X_test)

base_model = DecisionTreeClassifier(
    max_depth = 1,
    max_features=0.3,
    class_weight='balanced',
    random_state=1
)
ada_model = AdaBoostClassifier(
    base_estimator = base_model,
    n_estimators = 1000,
    learning_rate=1.,
    random_state=1
)

ada_model.fit(X_train, y_train)

y_pred_ada = ada_model.predict(X_test)
score = accuracy_score(y_pred_ada, y_test)
print("ada 모델의 정확도:", score)
