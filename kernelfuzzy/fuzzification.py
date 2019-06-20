"""

    Class FuzzyData

"""

import numpy as np
from kernelfuzzy.fuzzyset import FuzzySet
from kernelfuzzy.memberships import gaussmf

class FuzzyData:
    
    _data             = None # I dont know if we want to keep this
    _fuzzydata        = None
    _epistemic_values = None # only for epistemic fuzzy sets
    _target           = None

    def __init__(self, data=None, target=None):
        if data is not None:
            self._data = data
            self._target = target
            self._data.columns = self._data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    def quantile_fuzzification_classification(self):
        
        '''
        
        Algorithm 1 from https://hal.archives-ouvertes.fr/hal-01438607/document

        '''

        grouped = self._data.groupby([self._target])

        self._epistemic_values = grouped.transform(lambda x:
                                             np.exp(-np.square(x - x.quantile(0.5))
                                                    /
                                                    (np.abs(x.quantile(0.75) - x.quantile(0.25)) / (
                                                            2 * np.sqrt(2 * np.log(2)))) ** 2
                                                    ))

        # join data and epistemistic values
        num_rows = self._epistemic_values.shape[0]
        num_cols = self._epistemic_values.shape[1]

        self._fuzzydata=np.asarray([[FuzzySet(elements=self._data.iloc[j, i],
                                  md=self._epistemic_values.iloc[j, i])
                         for i in range(num_cols)]
                        for j in range(num_rows)])


    def get_fuzzydata(self):
        return self._fuzzydata

    def get_data(self):
        return self._data

    def get_epistemic_values(self):
        return self._epistemic_values

    def get_target(self):
        return self._data[self._target]

    def show_class(self):

        """

        Print in the stdout the all the contents of the class, for debugging

        """

        print("(_data)             \n", _data, "\n")
        print("(_fuzzydata)        \n", _fuzzydata, "\n")
        print("(_epistemic_values) \n", _epistemic_values, "\n")
        print("(_target)           \n", _target, "\n")

    # TOYS DATASETS
    @staticmethod
    def create_toy_fuzzy_dataset(num_rows=10, num_cols=2):
        
        '''
        
        Creates a matrix of fuzzy datasets, each row represent a tuple of fuzzy sets
        each column is a variable. Each fuzzy set is a fuzzy set with gaussian membership function
        
        '''

        return np.asarray([[FuzzySet(elements=np.random.uniform(0, 100, 2),
                                     mf=gaussmf,
                                     params=[np.mean(np.random.uniform(0, 100, 2)),
                                             np.std(np.random.uniform(0, 100, 2))])
                            for i in range(num_cols)]
                           for j in range(num_rows)])

    # TODO profile and compare with
    '''fuzzy_dataset_same = np.full((num_rows, num_cols), 
                              dtype=FuzzySet, 
                              fill_value=FuzzySet(elements=np.random.uniform(0, 100, 10),
                                                  mf=gaussmf,
                                                  params=[np.mean(np.random.uniform(0, 100, 10)),
                                                          np.std(np.random.uniform(0, 100, 10))]))
                                                          '''

    # TODO better parsing
