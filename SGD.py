
## Stochastic Gradient Descent Loop for Algorithm 


import numpy as np
from gradients import alphaGradient, wGradient
from estimateSignal import estimateSignal



def multiSGDthres(x,y,alpha,W): 
    
##Recover variable dimensions
    samples=x.shape[1]
    samplesIterator=np.arange(samples)
## Initializations 

    #Learning Rates
    learningRateAlpha=.00005
    learningRateW=.000005     
    
    # Divergence criterion 
    divergenceThreshold=10
    
    
    # Error criterion needed to exit Stochastic Gradient descent 
    threshold=.1
    

## Graph Variables to return 
    
    #Average error over samples per epoch 
    errorEpoch=list()
    errorEpoch.append(np.mean(np.mean((x-y)**2,axis=0)))
    
    #Historical values of alpha and W
    alphaHistory=list()
    WHistory=list()
    alphaHistory.append(alpha)
    WHistory.append(W)
    
    # Lists containing average gradient per epoch for alpha and W
    alphaGradEpoch=list()
    WGradEpoch=list()
    
    #Learning Rates
    learningRates=list()
    learningRates.append(learningRateAlpha)
    learningRates.append(learningRateW)
      

        
## Stochastic Gradient Descent loop, completes at least two epochs 
    # and exits if alpha and W grads' sum is less than the threshold
    
    while (len(errorEpoch)<3 or (abs(alphaGradEpoch[len(alphaGradEpoch)-1])+abs(WGradEpoch[len(WGradEpoch)-1]))>threshold) and len(errorEpoch)<20:
    #while (len(errorEpoch)<3 or (abs(alphaGradEpoch[len(alphaGradEpoch)-1]))>threshold) and len(errorEpoch)<20:
        
       
        returnMatrix=np.zeros((samples+1,5),dtype=object)
        returnMatrix[0,:]=[alpha,W,0,0,0]  
        returnMatrix[sample+1,:]=np.asarray([samplesSGDLoop(returnMatrix[sample,0],returnMatrix[sample,1],x[:,sample],y[:,sample],learningRateAlpha,learningRateW) for sample in samplesIterator])    
   
        alpha=returnMatrix[samples,0]
        W=returnMatrix[samples,1]
        # For each epoch record average error of each sample
        errorEpoch.append(np.average(returnMatrix[:,2]))
        
        # Compute average per epoch alpha and W gradients 
        alphaGradEpoch.append(np.average(returnMatrix[:,3]))
        WGradEpoch.append(np.average(returnMatrix[:,4]))
        
        # Update function error between consecutive epochs 
        functionError=errorEpoch[len(errorEpoch)-1]-errorEpoch[len(errorEpoch)-2]
        
        print("Threshold SGD " + str(len(errorEpoch)-1))
        
        
   ## Divergence criterion     
       # If algorithm has completed more than 2 epochs and is greater than the divergence 
       # threshold then exit 
        if len(errorEpoch)>2 and functionError>divergenceThreshold:
            print("diverged")
            break
                
        
        
    return (alpha, W, errorEpoch,np.array(alphaHistory),np.array(WHistory),learningRates,alphaGradEpoch,WGradEpoch)            
    
    
def samplesSGDLoop(alpha,W,sampleX,sampleY,learningRateAlpha,learningRateW):
         
    
    
    ##Calculate gradients for alpha and W
    alphaGrad=alphaGradient(sampleX,sampleY,alpha,W)
    WGrad=wGradient(sampleX,sampleY,alpha,W)
    
    
    ## Update alpha and W                 
    alpha=alpha-learningRateAlpha*alphaGrad
    W=W-learningRateW*WGrad
    
    # Record MSE for each sample
    errorSample=(sampleX-estimateSignal(W,sampleY,alpha))**2
    
    return (alpha,W,errorSample,alphaGrad,WGrad)
    
    
     

                        
 
