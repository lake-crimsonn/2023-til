# tf_numpy_function

- ```
    import tensorflow as tf
    import numpy as np

    def numpy_func(x):
        return np.sin(x)

    x = tf.constant([0.0, np.pi/2, np.pi])

    # Using tf.numpy_function to apply the NumPy function to the TensorFlow tensor.
    result = tf.numpy_function(numpy_func, [x], tf.float64)

    print(result.numpy())
  ```

- When building models or computations in TensorFlow, you sometimes need to use operations or functions that are not natively supported by TensorFlow but are available in the more general-purpose numerical library NumPy. To bridge this gap, TensorFlow provides the tf.numpy_function function, which enables you to use NumPy functions within TensorFlow graphs.

---
