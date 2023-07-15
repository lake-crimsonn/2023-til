# XGBoost

- Extreme Gradient Boosting
- 그래디언트 부스팅에서 오버피팅 기법 추가
- 그래디언트 부스트 병렬 처리 -> XGboost
- 기본 학습기를 결정트리를 이용
- 그래디언트처럼 잔차를 이용하여 약점 보완
---
- 230620 추가
- 파이썬 래퍼 XGB와 사이킷런 래퍼 XGB가 있다. 싸이킷런 XGB가 더 최근의 XGB다. 그래서 성능이 더 좋고, 이용하는 파라미터 역시 다르다. 
- 구분하는 방법은 주로 파이썬 래퍼는 import xgboost as xgb로 불러와서 사용한다. xgb.fit()
- 사이킷런 XGB는 분류일시 XGBClassifier(), 회귀면 XGRegressor().변수에 인스턴스를 담아 사용한다. model = XGBClassifier() model.fit()
- 대표적인 파라미터의 차이점은 eta->learning_rate, sub_sample->subsample, lambda->reg_lambda, alpha->reg_alpha, num_boost_round->n_estimators
- https://injo.tistory.com/44
---
estimator: It represents the model or estimator object, in this case, the XGBoost classifier (model).

param_grid: It specifies the grid of hyperparameter values to be searched. param_xgb should be a dictionary containing the hyperparameter names as keys and the corresponding lists of values to be tried.

scoring: It specifies the scoring metric used to evaluate the performance of the model. In this case, 'accuracy' is used.

cv: It determines the cross-validation splitting strategy. Here, cv=3 indicates 3-fold cross-validation will be performed.

refit: It is set to True by default, indicating that the best estimator found by GridSearchCV will be refitted on the entire dataset.

n_jobs: It specifies the number of CPU cores to be used for parallelizing the grid search. In this case, n_jobs=1 indicates only one core will be used.

verbose: It controls the verbosity level of the grid search process. A higher value (e.g., verbose=2) provides more detailed output during the search.
After running gscv_xgb.fit(X, y), the GridSearchCV object will perform the hyperparameter search using cross-validation and identify the best combination of hyperparameters based on the specified scoring metric. The best model can be accessed using gscv_xgb.best_estimator_.

---
