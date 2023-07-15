# binary cross entropy

- 이진분류시 사용하는 손실함수 알고리즘.
- 레이블값과 예측값의 차이의 평균을 계산한다.

```

Binary cross entropy (BCE) is a loss function commonly used in machine learning and deep learning algorithms for binary classification problems. It measures the dissimilarity or error between predicted probabilities and the true binary labels of a dataset.

In binary classification, each instance in the dataset belongs to one of two classes, typically represented as 0 and 1. The BCE loss function calculates the average difference between the predicted probabilities and the true labels. It's often used with activation functions like sigmoid, which maps the output to a probability between 0 and 1.

Mathematically, the BCE loss is defined as follows:

BCE = -(y * log(p) + (1 - y) * log(1 - p))

where:

BCE is the binary cross entropy loss.
y is the true binary label (0 or 1) of an instance.
p is the predicted probability of the positive class (between 0 and 1) for the same instance.
The BCE loss is logarithmic, penalizing confident incorrect predictions more heavily. When the predicted probability approaches the true label, the BCE loss becomes smaller, indicating a better model fit.

In practice, during the training process, the BCE loss is minimized by adjusting the model's weights and biases using optimization algorithms like gradient descent or its variations. Minimizing the BCE loss helps in finding the optimal model parameters for accurate binary classification.
```

---
