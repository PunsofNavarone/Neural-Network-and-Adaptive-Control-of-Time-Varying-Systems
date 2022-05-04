import numpy as np
import pandas as pd
import pickle
from activations import tan_h
from activations import dtan_h
from matplotlib import pyplot as plt
def Train():
	n=1;
	end=50000;
	endval=np.arange(-1*n,end);
	u=-1*np.ones((end+n,1),dtype='float')+2*np.random.rand(end+n,1);
	#print(u);
	f=u*(u+0.5)*(u-0.8);
	yp=np.empty((end+n,1),dtype='float');
	yp[0]=0;
	
	for i in range(n,end+n):
		yp[i]=0.8*yp[i-1]+f[i-1];

	yphat=np.empty((end+n,1),dtype='float');
	yphat[0]=0;

	bias=1;
	L1=20;
	#L2=10;
	eta=0.1;

	W1=np.random.normal(0,0.1,(L1,1+1));
	#W2=np.random.normal(0,0.1,(L2,L1+1));
	W2=np.zeros([1,L1+1]);
	J=0;
	epochs=1;

	val=np.empty((end+n,1),dtype='float');

	for a in range(epochs):
		for i in range(n,end+n):
			S=u[i-1];
			x=np.array([bias,S[0]]);
			A1=np.matmul(W1,x);
			A=tan_h(A1);
			y=np.insert(A,0,[bias]);
			B1=np.matmul(W2,y);
			#B=tan_h(B1);
			B=B1;
			"""
			z=np.insert(A,0,[bias]);
			C1=np.matmul(W2,z);
			C=tan_h(C1);
			"""
			yphat[i]=0.8*yphat[i-1]+B;
			val[i]=B;

			e=yphat[i]-yp[i];
			#del2=e*dtan_h(B1);
			del2=e;
			#del2=np.matmul((np.transpose(W3[...,1:])),del3)*dtan_h(B1);
			del1=np.matmul((np.transpose(W2[...,1:])),del2)*dtan_h(A1);
			#del2=del2.reshape(len(del2),1);
			del1=del1.reshape(len(del1),1);
			#y=y.reshape(1,len(y));
			x=x.reshape(1,len(x));
			#W3=W3-(eta*del3*np.transpose(z));
			W2=W2-(eta*del2*np.transpose(y));
			W1=W1-(eta*np.matmul(del1,x));
			J=J+e*e;


	J=J/(end);
	print("Training Cost for BPA 1 Layer = ",J)
	return(W1,W2);
if __name__=='__main__':
	Train();