import numpy as np
import random

class Network():
    # the list sizes contains the number of neurons in the respective layers
    def __init__(self, sizes: list[int]):
        self.num_layers: int = len(sizes)
        self.sizes: list[int] = sizes
        # inizializzazione dei pesi e bias casuale
        # - per i bias costruisco un vettore colonna casuale per ogni layer della rete tranne quello di input
        # - per i pesi costruisco una matrice per le connessioni tra le coppie di layer
        #   - x = numero di neuroni nel layer precedente
        #   - y = numero di neuroni nel layer successivo
        self.biases: list[np.ndarray] = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights: list[np.ndarray] = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    # a is an (n, 1) Numpy ndarray, not a (n,) vector. Here, n is the number of inputs to the network.
    # If you try to use an (n,) vector as input you'll get strange results. 
    def feedforward(self, a):
        """Return the output of the network if "a" is input."""
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        return a

    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        """Train the neural network using mini-batch stochastic gradient descent.
        The "training_data" is a list of tuples "(x, y)" representing the training
        inputs and the desired outputs.  The other non-optional parameters are
        self-explanatory (eta is the learning rate).  
        If "test_data" is provided then the network will be evaluated against the test
        data after each epoch, and partial progress printed out.  This is useful for
        tracking progress, but slows things down substantially."""
        if test_data:
            n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs):
            # recupera mini batch scelti a caso dal training set
            random.shuffle(training_data)
            mini_batches = [training_data[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)]
            # per ogni mini batch calcoliamo un singolo step di gradient descent
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print("Epoch {0}: {1} / {2}".format(j, self.evaluate(test_data), n_test))
            else:
                print("Epoch {0} complete".format(j))

    def update_mini_batch(self, mini_batch, eta):
        """Update the network's weights and biases by applying
        gradient descent using backpropagation to a single mini batch.
        The "mini_batch" is a list of tuples "(x, y)", and "eta"
        is the learning rate. nabla è il simbolo del gradiente"""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            # this computes the gradient of the cost function for a particular input in the batch
            x_nabla_b, x_nabla_w = self.backprop(x, y)
            # queste list comprehension accumulano i passi di ogni input per fare la media del
            # minibatch dopo. Notare che stiamo sommando vettori e matrici
            nabla_b = [nb+xnb for nb, xnb in zip(nabla_b, x_nabla_b)]
            nabla_w = [nw+xnw for nw, xnw in zip(nabla_w, x_nabla_w)]
        # modifichiamo pesi e bias secondo la media dei gradienti calcolati sopra
        self.weights = [w-(eta/len(mini_batch))*nw for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb for b, nb in zip(self.biases, nabla_b)]

    def backprop(self, x, y):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        ### feedforward
        activation = x
        activations = [x] # list to store all the activations, layer by layer
        zs = [] # list to store all the z vectors, layer by layer
        for b, w in zip(self.biases, self.weights):
            # Nota che np dot fa anche matmul.
            # Qua stiamo moltiplicando la matrice dei pesi con il
            # vettore delle attivazione del livello precedente
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        ### backward pass
        delta = self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        # Qua sotto il range mi produce numeri da 2 a num_layers (escluso)
        # Siccome stiamo partendo dal fondo, e abbiamo già calcolato l'ultimo
        # layer, stiamo scorrendo dal penultimo layer fino al secondo (l'ultimo
        # che ha dei pesi e bias associati)
        # l = L-1, ..., 2
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            # nota che qua sto riassegnando delta dopo aver utilizzato quello
            # dell'iterazione precedente
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        # Argmax restituisce l’indice dell’elemento con il valore massimo.
        # Qua sotto otteniamo una lista di tuple formate da classificazione
        # della nostra rete e classificazione corretta
        test_results = [(np.argmax(self.feedforward(x)), y) for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives 
        \\partial C_x / \\partial a for the output 
        activations."""
        return (output_activations-y)

    ### metodi per salvare e caricare la rete
    def save(self, filename: str):
        """Salva la rete in un file .npz"""
        np.savez(filename,
             sizes=np.array(self.sizes),
             biases=np.array(self.biases, dtype=object),
             weights=np.array(self.weights, dtype=object))
        print(f"Rete salvata in '{filename}'")

    # Questo sotto è un costruttore alternativo
    # In python a quanto pare si fa così 
    @classmethod
    def load(cls, filename: str):
        """Carica una rete da un file .npz"""
        data = np.load(filename, allow_pickle=True)
        net = cls(data['sizes'].tolist())  # ricrea la struttura
        net.biases = data['biases'].tolist()
        net.weights = data['weights'].tolist()
        return net


# Numpy automatically applies the function sigmoid elementwise
def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))

