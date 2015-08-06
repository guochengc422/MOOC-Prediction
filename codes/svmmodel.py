import numpy as np
import mungetools as mg
from sklearn.svm import SVC

weight_dict = {}


def trainClassifier(DF,paramc,paramg,split=0.7):

    nvals = len(DF)
    splitind=np.floor(nvals*split)
    nparams = len(paramc)*len(paramg)
    scores = np.zeros(nparams)
    counter=0
    paramholder=np.zeros([nparams,2])
    # randomize trainingset and split to train and CV set
    rp = np.random.permutation(nvals)
    survt=np.array(DF.iloc[rp[0:splitind],0])
    survcv=np.array(DF.iloc[rp[splitind:nvals],0])
    # note: SVM takes -1 and 1 for single class labels
    survt[~survt]=-1
    survcv[~survcv]=-1
    tset = DF.iloc[rp[0:splitind],1:]
    cvset = DF.iloc[rp[splitind:nvals],1:]
    bestscore=-1
    # loop through the values of c and g
    for c in paramc:
        for g in paramg:
            model=SVC(C=c,kernel='linear',probability = True)
            model=model.fit(tset,survt)
            try:
                scorei=model.score(cvset,survcv)
            except:
                scorei=0 # something went wrong...
            scores[counter]=np.mean(scorei)
            paramholder[counter,0]=c
            paramholder[counter,1]=g
            if scorei>bestscore:
                bestscore=scorei
                bestmodel=model
            counter+=1
            print('Score = %f with c: %f, g: %f' %(scorei,c,g))
    bestc=paramholder[scores.argmax(),0]
    bestg=paramholder[scores.argmax(),1]
    print('Best score of %f with c: %f, g: %f' %(bestscore,bestc,bestg))
    return bestmodel

    

trdata,testdata=mg.loadData()

testid = np.array(testdata.UserID)

# trdata = trdata.drop(['coursecount'],axis=1)

testdata = testdata.drop(['UserID'],axis=1)

print trdata
print testdata

# initialize classifier
# try several values of c (prediction error weight) and g (kernel width)
testc = [0.05, 0.1, 0.3, 0.6, 1, 3, 5, 10 ]
testg = [0, 0.01, 0.05, 0.1, 0.5, 1, 1.5]

# testc = [0.3]
# testg = [0.01]

# find the best model
model= trainClassifier(trdata,testc,testg)

model = model.fit(trdata.iloc[:,1:],trdata.iloc[:,0])

# generate predictions
preds = np.array(model.predict_proba(testdata))[:,-1]
mg.writeout(preds,testid,'predictions/svmmodel_test.csv')
