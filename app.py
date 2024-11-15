from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
from sklearn.manifold import LocallyLinearEmbedding
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from gooey import Gooey

@Gooey # The Decorator goes here
def parse_args():
	parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
	                        conflict_handler='resolve')
	parser.add_argument('--dim_red_type', default='PCA', choices=[
	  		              'PCA','LLE'], help='The dim red. types')
	parser.add_argument('--n_comp', default=10, type=int, choices=[
	 		                 5,10], help='output dimensions')
	parser.add_argument('--classifier', default='LR', choices=[
		            	    'LR','SVC','RF'], help='Classifiers')
	args = parser.parse_args()
	return args

def main(args):
  X, y = make_classification(n_samples=1000, n_features=30,
                             n_informative=15, n_redundant=15, 
                             random_state=42)
  X_train,X_test,y_train,y_test = train_test_split(X, y,stratify=y,
                                                  test_size=0.3, 
                                                  random_state=42)

  # dimensionality reduction
  def dim_reduction(X_train,X_test,dim_red_type,n_comp):
    if dim_red_type == 'pca':
      dim_red = PCA(n_components=int(n_comp))
    elif dim_red_type == 'lle':
      dim_red = LocallyLinearEmbedding(n_components=int(n_comp))
    dim_red.fit(X_train)
    X_train_dim = dim_red.transform(X_train)
    X_test_dim = dim_red.transform(X_test)
    return X_train_dim, X_test_dim

  # model training and eval
  def train(classifier,X_train,y_train,X_test,y_test):
    if classifier == 'lr':
      clf = LogisticRegression()
    elif classifier == 'svc':
      clf = SVC()
    elif classifier == 'rf':
      clf = RandomForestClassifier()
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    acc_score = accuracy_score(y_test,y_pred).round(3)
    return acc_score * 100

  X_train, X_test = dim_reduction(X_train,X_test,'lle',2)
  acc_score = train('lr',X_train,y_train,X_test,y_test)
  print(f'Dimensionality reduction: {args.dim_red_type}')
  print(f'Number of components: {args.n_comp}')
  print(f'Classifier: {args.classifier}')
  print('Accuracy Score: ',acc_score)
  print('*'*10)
  
def more_main():
	args = parse_args()
	main(parse_args())
  
if __name__ == "__main__":
	more_main()