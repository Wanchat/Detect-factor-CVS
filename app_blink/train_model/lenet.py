from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.layers import Flatten, Dense
from tensorflow.python.keras.layers import Dropout, AveragePooling2D
from tensorflow.python.keras.models import Sequential


class LeNet:

    @staticmethod
    def build_1(width, height, depth, classes):
        inputShape = (width, height, depth)
        model = Sequential()

        model.add(Conv2D(16, (3, 3), padding="same", input_shape=inputShape, activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(64, (3, 3), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Flatten())
        model.add(Dense(512, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(classes, activation='softmax'))

        model.summary()

        return model

    @staticmethod
    def build_2(width, height, depth, classes):
        inputShape = (width, height, depth)
        model = Sequential()

        model.add(Conv2D(16, (5, 5), padding="same", input_shape=inputShape, activation='relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(64, (5, 5), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(128, (5, 5), padding="same", activation='relu'))

        model.add(Flatten())
        model.add(Dense(512, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(classes, activation='softmax'))

        model.summary()

        return model

    @staticmethod  # << best network
    def build_2_new(width, height, depth, classes):
        inputShape = (width, height, depth)
        model = Sequential()
        model.add(Conv2D(32, (5, 5), padding="same", input_shape=inputShape, activation='relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
        model.add(Dropout(.25))

        model.add(Conv2D(64, (5, 5), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
        model.add(Dropout(.25))

        model.add(Conv2D(124, (5, 5), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
        model.add(Dropout(.25))

        model.add(Flatten())
        model.add(Dense(256, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(classes, activation='softmax'))

        model.summary()

        return model

    @staticmethod
    def build_2_new_inference(width, height, depth, classes):
        inputShape = (width, height, depth)
        model = Sequential()
        model.add(Conv2D(32, (5, 5), padding="same", input_shape=inputShape, activation='relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))

        model.add(Conv2D(64, (5, 5), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))

        model.add(Conv2D(124, (5, 5), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))

        model.add(Flatten())
        model.add(Dense(256, activation='relu'))
        model.add(Dense(classes, activation='softmax'))

        return model

    @staticmethod
    def build_3(width, height, depth, classes):
        inputShape = (width, height, depth)
        model = Sequential()

        model.add(Conv2D(16, (7, 7), padding="same", input_shape=inputShape, activation='relu'))
        model.add(MaxPooling2D(pool_size=(5, 5), strides=(3, 3)))
        model.add(Dropout(0.25))

        model.add(Conv2D(64, (7, 7), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(5, 5), strides=(3, 3)))
        model.add(Dropout(0.25))

        model.add(Flatten())
        model.add(Dense(512, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(classes, activation='softmax'))

        model.summary()

        return model

    @staticmethod
    def build_4(width, height, depth, classes):
        inputShape = (width, height, depth)
        model = Sequential()

        model.add(Conv2D(16, (9, 9), padding="same", input_shape=inputShape, activation='relu'))
        model.add(MaxPooling2D(pool_size=(7, 7), strides=(5, 5)))
        model.add(Dropout(0.25))

        model.add(Conv2D(64, (9, 9), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(5, 5), strides=(3, 3)))
        model.add(Dropout(0.25))

        model.add(Flatten())
        model.add(Dense(512, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(classes, activation='softmax'))

        model.summary()

        return model

    @staticmethod
    def build_tf(width, height, depth, classes):
        inputShape = (width, height, depth)

        model = Sequential()

        model.add(Conv2D(32, (5, 5), input_shape=inputShape))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (5, 5), input_shape=inputShape))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())
        model.add(Dense(1024, activation='relu'))
        model.add(Dense(classes, activation='softmax'))

        model.summary()

        return model

    @staticmethod
    def build_mobile(width, height, depth, classes):
        inputShape = (width, height, depth)
        model = Sequential()
        model.add(Conv2D(32, (3, 3), padding="same", input_shape=inputShape, activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(Dropout(.25))

        model.add(Conv2D(64, (1, 1), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(Dropout(.25))

        model.add(Conv2D(128, (3, 3), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(Dropout(.25))

        model.add(Conv2D(128, (1, 1), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(Dropout(.25))

        model.add(Flatten())
        model.add(Dense(84, activation='relu'))
        model.add(Dropout(0.5))

        model.add(Dense(classes, activation='softmax'))

        model.summary()

        return model

    @staticmethod
    def build_mobile_inference(width, height, depth, classes):
        inputShape = (width, height, depth)
        model = Sequential()
        model.add(Conv2D(32, (3, 3), padding="same", input_shape=inputShape, activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        model.add(Conv2D(64, (1, 1), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        model.add(Conv2D(128, (3, 3), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        model.add(Conv2D(128, (1, 1), padding="same", activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        model.add(Flatten())
        model.add(Dense(84, activation='relu'))

        model.add(Dense(classes, activation='softmax'))

        model.summary()

        return model

    @staticmethod
    def lenet5(width, height, depth, classes):
        inputShape = (width, height, depth)
        model = Sequential()

        model.add(Conv2D(6, (5, 5), padding="same", input_shape=inputShape, activation='tanh'))
        model.add(AveragePooling2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
        model.add(Dropout(0.25))

        model.add(Conv2D(16, (5, 5), padding="valid", activation='tanh'))
        model.add(AveragePooling2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
        model.add(Dropout(0.5))

        model.add(Conv2D(120, (5, 5), padding="valid", activation='tanh'))

        model.add(Flatten())
        model.add(Dense(84, activation='tanh'))
        model.add(Dropout(0.25))

        model.add(Dense(classes, activation='softmax'))

        model.summary()

        return model

    @staticmethod
    def lenet5_inference(width, height, depth, classes):
        inputShape = (width, height, depth)
        model = Sequential()

        model.add(Conv2D(6, (5, 5), padding="same", input_shape=inputShape, activation='tanh'))
        model.add(AveragePooling2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))

        model.add(Conv2D(16, (5, 5), padding="valid", activation='tanh'))
        model.add(AveragePooling2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))

        model.add(Conv2D(120, (5, 5), padding="valid", activation='tanh'))

        model.add(Flatten())
        model.add(Dense(84, activation='tanh'))

        model.add(Dense(classes, activation='softmax'))

        model.summary()

        return model
