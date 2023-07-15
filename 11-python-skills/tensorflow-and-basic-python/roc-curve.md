# ROC 커브 곡선

```python
from sklearn.metrics import roc_curve, roc_auc_score

test_images = []
test_labels = []

# Extract images and labels from the test_dataset
for image, label in test_dataset:
    test_images.append(image)
    test_labels.append(label)

test_images = np.concatenate(test_images)
test_labels = np.concatenate(test_labels)

# Generate predictions
y_pred_prob = model.predict(test_images)

# Generate ROC curve values: fpr, tpr, thresholds
fpr, tpr, thresholds = roc_curve(test_labels, y_pred_prob)

# Plot ROC curve
plt.figure()
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()

# AUC score
print('AUC: ', roc_auc_score(test_labels, y_pred_prob))
```

---
