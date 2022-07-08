import json
f = open('trial_stats.json')
data = json.load(f)

alpha=[]
booster=[]
colsample_bylevel=[]
colsample_bytree=[]
gamma=[]
lambda=[]
learning_rate=[]
max_depth=[]
min_child_weight=[]
n_estimators=[]
n_jobs=[]
subsample=[]
tree_method=[]


acc_ar=[]
roc_ar=[]

rec0=[]
rec1=[]
prec0=[]
prec1=[]


for i in data:
        
        alpha.append( i['config']['model']['alpha'] )
        booster.append( i['config']['model']['booster'] )
        colsample_bylevel.append( i['config']['model']['colsample_bylevel'] )
        colsample_bytree.append( i['config']['model']['colsample_bytree'] )
        gamma.append( i['config']['model']['gamma'] )
        lambda.append( i['config']['model']['lambda'] )
        learning_rate.append( i['config']['model']['learning_rate'] )
        max_depth.append( i['config']['model']['max_depth'] )
        min_child_weight.append( i['config']['model']['min_child_weight'] )
        n_estimators.append( i['config']['model']['n_estimators'] )
        n_jobs.append( i['config']['model']['n_jobs'] )
        subsample.append( i['config']['model']['subsample'] )
        tree_method.append( i['config']['model']['tree_method'] )
        
        acc_ar.append(  i['metrics']['test']['score']  )
        roc_ar.append(  i['metrics']['test']['roc_auc']  )

        rec0.append(  i['metrics']['test']['0.0']['recall']  )
        prec0.append(  i['metrics']['test']['0.0']['precision']  )
        rec1.append(  i['metrics']['test']['0.1']['recall']  )
        prec1.append(  i['metrics']['test']['0.1']['precision']  )

        
        
print('alpha =',alpha)
print('booster=',booster)
print('colsample_bylevel=',colsample_bylevel)
print('colsample_bytree=',colsample_bytree)
print('gamma=',gamma)
print('lambda=',lambda)
print('learning_rate=',learning_rate)
print('max_depth=',max_depth)
print('min_child_weight=',min_child_weight)
print('n_estimators=',n_estimators)
print('n_jobs=',n_jobs)
print('subsample=',subsample)
print('tree_method=',tree_method)


print('acc_ar=',acc_ar)
print('roc_ar=',roc_ar)

print( 'rec0 =',rec0)
print( 'prec0 =',prec0)
print( 'rec1 =',rec1)
print( 'prec0 =',rec1)
