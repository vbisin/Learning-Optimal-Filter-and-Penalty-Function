#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:03:28 2017

@author: vittoriobisin
"""
from functionEval import functionEval

def backtrackArmijoAlpha (W,sampleY,alpha,alphaGrad):
    stepSize=1
    tao=.5   
    counter=0
    
    xk1=functionEval(W,sampleY,alpha)
    xk2=functionEval(W,sampleY,alpha-stepSize*alphaGrad)
    RHS=xk1-.5*stepSize*sum(alphaGrad**2)
    while  not (xk2<=RHS).all():
        stepSize=stepSize*tao


        counter+=1
        print("Alpha "+str(counter))
    return stepSize


def backtrackArmijoTrial (x,sampleY,alpha,alphaGrad):
    stepSize=10
    tao=.5   
    counter=0
    
    xk1=x
    xk2=(xk1-stepSize*2*xk1)**2
    RHS=xk1**2-.5*stepSize*(2*xk1)**2
    #while  (xk2<=RHS).all():
    while (xk2>RHS):
        stepSize=stepSize*tao
        xk2=(x-stepSize*2*x)**2
        RHS=xk1-.5*stepSize*(2*x**2)

        counter+=1
        print("Alpha "+str(counter))
    return stepSize