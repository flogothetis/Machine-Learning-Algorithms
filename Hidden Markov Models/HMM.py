import numpy as np
#Viterbi algorithm
def Viterbi(V, a , b , initial_prob):
	number_of_observations= V.shape[0]
	number_of_hidden_states=a.shape[0]

	#table to save probabilities
	omega=np.zeros((number_of_observations,number_of_hidden_states))
	#initial probabilities
	omega[0,:]=initial_prob   * b[:,V[0]]

	#table to keep the transition path with the maximum prob.
	prev =np.zeros((number_of_observations-1,number_of_hidden_states))

	for t in range(1,number_of_observations):
		for j in range (number_of_hidden_states):
			probability = omega[t-1,:] *a[:,j] *b[j,V[t]]
			prev[t-1]= np.argmax(probability)
			omega[t,j]=np.max(probability)
	#Path Array
	S= np.zeros(number_of_observations)
	#Find most probable last hidden state
	last_state= np.argmax(omega[number_of_observations-1,:])
	S[0]=last_state

	#BackTracking
	backtrack_index=1
	for i in range (number_of_observations-2,-1,-1):
		S[backtrack_index]=prev[i,int(last_state)]
		last_state=prev[i,int(last_state)]
		backtrack_index+=1

	#Flip to take the correct path
	S=np.flip(S,axis=0)

	return S

if __name__== "__main__":

	# Initial probabilities of Sun /Cloud /Rain
	initial_probs = np.array([0.6,0.1,0.3])

	#Transition probabilities| rows [Sun Cloud Rain] | columns [Sun  Cloud Rain]
	a = np.array([[0.5,0.25,0.25],
		[0.375,0.125,0.375],
		[0.125,0.675,0.375]])
	#Emission probabilities | rows [ Sun Cloud Rain] | columns [Dry Dryish Damp Foggy]
	b= np.array([[0.6, 0.2, 0.15,0.05],
				[0.25,0.25,0.25,0.25],
		        [0.05,0.1,0.35,0.5]])
	# Observations and their labels
	obs = np.array([0,1,2,3])
	labels ={0:'Sun', 1: 'Cloud', 2: 'Rain'}
	sequence=[]
	# Run Viterbi algorithm
	for i in Viterbi(obs,a,b,initial_probs):
		sequence.append(str(labels[i]))
	#Print most probable sequence
	print(' '.join(sequence))
