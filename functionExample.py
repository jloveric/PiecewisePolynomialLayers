'''
This example is meant to demonstrate how you can map complex
functions using a single input and single output with polynomial
synaptic weights
'''
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import snovalleyai_piecewise_polynomial_layers.PolynomialLayers as poly

offset = -0.1
factor = 1.5 * 3.14159
xTest = np.arange(100) / 50 - 1.0
yTest = 0.5 * np.cos(factor * (xTest - offset))

xTrain = tf.random.uniform([1000], minval=-1.0, maxval=1, dtype=tf.float32)
yTrain = 0.5 * tf.math.cos(factor * (xTrain - offset))

modelSetF = [
    {'name': 'Fourier 1', 'func': poly.b1F},
    {'name': 'Fourier 2', 'func': poly.b2F},
    {'name': 'Fourier 3', 'func': poly.b3F},
    {'name': 'Fourier 4', 'func': poly.b4F},
    {'name': 'Fourier 5', 'func': poly.b5F}
]

modelSetD = [
    {'name': 'Discontinuous 1', 'func': poly.b1D},
    {'name': 'Discontinuous 2', 'func': poly.b2D},
    {'name': 'Discontinuous 3', 'func': poly.b3D},
    {'name': 'Discontinuous 4', 'func': poly.b4D},
    {'name': 'Discontinuous 5', 'func': poly.b5D}
]

modelSetC = [
    {'name': 'Continuous 1', 'func': poly.b1C},
    {'name': 'Continuous 2', 'func': poly.b2C},
    {'name': 'Continuous 3', 'func': poly.b3C},
    {'name': 'Continuous 4', 'func': poly.b4C},
    {'name': 'Continuous 5', 'func': poly.b5C}
]

modelSet = [
    {'name': '1st order', 'func': poly.b1},
    {'name' : '2nd order', 'func' : poly.b2},
    {'name': '3rd order', 'func': poly.b3},
    {'name' : '4th order', 'func' : poly.b4},
    {'name': '5th order', 'func': poly.b5}]


colorIndex = ['red', 'green', 'blue', 'purple', 'black']
symbol = ['+', 'x', 'o', 'v', '.']

thisModelSet = modelSet

for i in range(0, len(thisModelSet)):

    model = tf.keras.models.Sequential([
        poly.Polynomial(1, basis=thisModelSet[i]['func']),
    ])

    model.compile(optimizer='adam',
                  loss='mean_squared_error',
                  metrics=['mean_squared_error'])

    model.fit(xTrain, yTrain, epochs=10, batch_size=1)
    model.evaluate(xTrain, yTrain)

    predictions = model.predict(xTest)

    plt.scatter(
        xTest,
        predictions.flatten(),
        c=colorIndex[i],
        marker=symbol[i],
        label=thisModelSet[i]['name'])

plt.plot(xTest, yTest, '-', label='actual', color='black')
plt.title('fourier synapse - no hidden layers')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
