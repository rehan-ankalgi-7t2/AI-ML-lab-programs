import numpy as np

x = np.array(([2,9], [1,5], [3,6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)

X = x/np.amax(x, axis=0)
Y = y / 100

# sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# derivative of sigmoid function
def derivative_sigmoid(x):
    return x * (1 - x)

# Variable initialization
epoch = 7000                    #Setting training iterations 
lr = 0.1                        #Setting learning rate 
inputlayer_neurons = 2          #number of features in data set 
hiddenlayer_neurons = 3         #number of hidden layers neurons 
output_neurons = 1              #number of neurons at output layer 

# weight and bias initialization 
wh = np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh = np.random.uniform(size=(1,hiddenlayer_neurons)) 
wout = np.random.uniform(size=(hiddenlayer_neurons,output_neurons)) 
bout = np.random.uniform(size=(1,output_neurons)) 

# draws a random range of numbers uniformly of dim x*y 
for i in range(epoch): 
    
    # Forward Propogation 
    hinp1=np.dot(X,wh) 
    hinp=hinp1 + bh 
    hlayer_act = sigmoid(hinp) 
    
    outinp1=np.dot(hlayer_act,wout) 
    outinp= outinp1+ bout 
    output = sigmoid(outinp) 
    
    # Backpropagation 
    EO = y-output 
    outgrad = derivative_sigmoid(output)
    d_output = EO* outgrad 
    
    EH = d_output.dot(wout.T) 
    hiddengrad = derivative_sigmoid(hlayer_act)
    d_hiddenlayer = EH * hiddengrad 
    
    wout += hlayer_act.T.dot(d_output) *lr 
    wh += X.T.dot(d_hiddenlayer) *lr 
    
print("Input: \n" + str(X)) 
print("Actual Output: \n" + str(Y)) 
print("Predicted Output: \n" ,output)


