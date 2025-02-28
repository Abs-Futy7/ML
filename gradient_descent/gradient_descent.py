import numpy as np

def gradient_descent(x, y):
    # Initialize slope (m) and intercept (b) to zero
    m_curr = b_curr = 0
    iterations = 10000  # Number of times the algorithm will run
    n = len(x)  # Number of data points
    learning_rate = 0.08  # Step size for updating m and b

    for i in range(iterations):  # Loop for performing gradient descent
        y_predicted = m_curr * x + b_curr  # Calculate the predicted y values based on current m and b
        
        # Compute the cost function (Mean Squared Error - MSE)
        cost = (1/n) * sum([val**2 for val in (y - y_predicted)])
        
        # Compute gradients (partial derivatives of cost function w.r.t m and b)
        md = -(2/n) * sum(x * (y - y_predicted))  # Gradient of m (slope)
        bd = -(2/n) * sum(y - y_predicted)  # Gradient of b (intercept)
        
        # Update m and b using gradient descent formula
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        
        # Print the values of m, b, and cost in each iteration
        print("Iteration {}: m = {:.4f}, b = {:.4f}, cost = {:.4f}".format(i, m_curr, b_curr, cost))

# Define input data points
x = np.array([1, 2, 3, 4, 5])  # Independent variable (features)
y = np.array([5, 7, 9, 11, 13])  # Dependent variable (labels)

# Call the gradient descent function
gradient_descent(x, y)