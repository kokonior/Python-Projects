import numpy as np
from utils.io_preprocessing import get_data_from_mnist
from utils.augmentation import (
    train_val_generator_with_flow,
    data_generator_with_augmentation,
)
from utils.plotting import plot_acc_loss
import os

# this suppresses the logs from tensorflow - needs to be set before tf is imported
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf

path_sign_mnist_train = f"data/tmp/mnist/sign_mnist_train.csv"
path_sign_mnist_test = f"data/tmp/mnist/sign_mnist_test.csv"


def build_multiclass_cnn_model_layers(input_shape):
    """
    Define the model with 2 Conv2D and 2 MaxPooling2D
    """
    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Conv2D(32, (3, 3), input_shape=input_shape),
            tf.keras.layers.MaxPool2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3)),
            tf.keras.layers.MaxPool2D((2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512, activation="relu"),
            tf.keras.layers.Dense(26, activation="softmax"),
        ]
    )
    return model


def compile_model_with_rmsprop(model, alpha):
    model.compile(
        optimizer=tf.keras.optimizers.RMSprop(learning_rate=alpha),
        loss="sparse_categorical_crossentropy",
        metrics=["acc"],
    )


if __name__ == "__main__":
    training_images, training_labels = get_data_from_mnist(path_sign_mnist_train)
    testing_images, testing_labels = get_data_from_mnist(path_sign_mnist_test)

    # add another dimension to the data, example (10000, 28, 28) --> (10000, 28, 28, 1)
    training_images = np.expand_dims(training_images, axis=3)
    testing_images = np.expand_dims(testing_images, axis=3)

    print(training_images.shape)
    print(testing_images.shape)

    # Their output should be:
    # (27455, 28, 28, 1)
    # (7172, 28, 28, 1)
    train_generator, validation_generator = train_val_generator_with_flow(
        training_images,
        training_labels,
        testing_images,
        testing_labels,
        data_generator_with_augmentation(),
        data_generator_with_augmentation(),
    )

    model = build_multiclass_cnn_model_layers((28, 28, 1))
    compile_model_with_rmsprop(model, 0.001)
    history = model.fit(train_generator, epochs=2, validation_data=validation_generator)
    """
    # should see the output like below:
    
    Epoch 1/2
    2746/2746 [==============================] - 42s 15ms/step - loss: 2.0565 - acc: 0.3664 - val_loss: 0.9141 - val_acc: 0.6887
    Epoch 2/2
    2746/2746 [==============================] - 43s 16ms/step - loss: 0.7183 - acc: 0.7638 - val_loss: 0.7463 - val_acc: 0.7574
    """
    model.evaluate(testing_images, testing_labels, verbose=0)
    plt = plot_acc_loss(history)
    plt.show()
