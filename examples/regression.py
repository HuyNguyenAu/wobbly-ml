# %%
import numpy as np
import matplotlib.pyplot as plt

from core import Models, Layers, ActivationFunctions, LossFunctions, Optimisers, Accuracies, Data

# Create data.
SAMPLES = 5000
AMPLITUDE = 1
x = np.arange(SAMPLES).reshape(-1, 1) / SAMPLES
y = AMPLITUDE * np.sin(4 * np.pi * x).reshape(-1, 1)

# Create training and validation dataset.
data_loader: Data.DataLoader = Data.DataLoader(x_train=x, y_train=y)

# Create a new model.
model = Models.Model()

# Add a dense layer with 1 input features and 128 output values.
model.add_layer(Layers.Dense(1, 128))

# Add a ReLU activation function.
model.add_layer(ActivationFunctions.ReLU())

# Add a dense layer with 128 input features and 128 output values.
model.add_layer(Layers.Dense(128, 128))

# Add a ReLU activation function.
model.add_layer(ActivationFunctions.ReLU())

# Add a dense layer with 128 input features and 128 output values.
model.add_layer(Layers.Dense(128, 128))

# Add a ReLU activation function.
model.add_layer(ActivationFunctions.ReLU())

# Add a dense layer with 128 input features and 128 output values.
model.add_layer(Layers.Dense(128, 128))

# Add a ReLU activation function.
model.add_layer(ActivationFunctions.ReLU())

# Add a dense layer with 128 input features and 1 output values.
model.add_layer(Layers.Dense(128, 1))

# # Add a linear activation function.
model.add_layer(ActivationFunctions.Linear())

# Set the loss function to mean squared error.
model.set_loss_function(LossFunctions.MeanSquaredError())

# Set the optimiser to ADAM.
model.set_optimiser(Optimisers.Adam(learning_rate=0.005, decay=1e-3))

# Set the accuracy.
model.set_accuracy(Accuracies.Regression(data_loader.get_y_train()))

# Finalise the model.
model.finalise()

# Perform model training.
model.train(data_loader.get_x_train(), data_loader.get_y_train(), epochs=500, print_every=100)

# Perfom model validation.
pred_y = model.prediction(data_loader.get_x_val())

plt.plot(data_loader.get_x_train(), data_loader.get_y_train(), label='Training')
plt.plot(data_loader.get_x_val(), data_loader.get_y_val(), label='Validation')
plt.plot(data_loader.get_x_val(), pred_y, label='Prediction')
plt.legend()
plt.show()
# %%
