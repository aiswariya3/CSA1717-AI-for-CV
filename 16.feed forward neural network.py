import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of Sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Mean Squared Error (MSE) Loss Function
def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Neural Network class
class FeedforwardNN:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        # Initialize weights and biases
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # Random initialization of weights and biases
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)  # (input_size, hidden_size)
        self.bias_hidden = np.random.randn(hidden_size)  # (hidden_size,)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)  # (hidden_size, output_size)
        self.bias_output = np.random.randn(output_size)  # (output_size,)

    def feedforward(self, X):
        # Hidden layer
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)

        # Output layer
        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.output = sigmoid(self.output_input)

        return self.output

    def backpropagate(self, X, y):
        # Compute the error
        output_error = y - self.output
        output_delta = output_error * sigmoid_derivative(self.output)

        # Hidden layer error and delta
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_output)

        # Update weights and biases
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * self.learning_rate
        self.bias_output += np.sum(output_delta, axis=0) * self.learning_rate
        self.weights_input_hidden += X.T.dot(hidden_delta) * self.learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0) * self.learning_rate

    def train(self, X, y, epochs=1000):
        for epoch in range(epochs):
            self.feedforward(X)
            self.backpropagate(X, y)

            # Print the loss every 100 epochs
            if epoch % 100 == 0:
                loss = mse_loss(y, self.output)
                print(f"Epoch {epoch}/{epochs}, Loss: {loss:.4f}")

# Example usage: XOR problem
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0],  # XOR(0, 0) = 0
              [1],  # XOR(0, 1) = 1
              [1],  # XOR(1, 0) = 1
              [0]]) # XOR(1, 1) = 0

# Initialize and train the neural network
nn = FeedforwardNN(input_size=2, hidden_size=4, output_size=1, learning_rate=0.1)
nn.train(X, y, epochs=10000)

# Test the neural network
output = nn.feedforward(X)
print("Predictions after training:")
print(output)
