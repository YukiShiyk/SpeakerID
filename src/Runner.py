import os
import sys
from src.Classifier import Classifier
from src.PreProcessing import PreProcessing
import numpy as np

classifier_classes = Classifier.classifier_dict()
abspath = os.path.abspath(sys.path[0])
CONFIG = {
    'frame size': 512,
    'overlap': 128,
    'is training': True,
    'is streaming': False,
    'data list': '../DataSet/DataList_all.txt',
    'classifier': ['all'],
    'argumentation': False
}


def main():
    preprocessor = PreProcessing(frame_size=CONFIG['frame size'],
                                 overlap=CONFIG['overlap'])
    if CONFIG['is streaming']:
        # Todo: Add streaming support.
        raise NotImplementedError
    else:
        wav_list, frame_list, energy_list, \
        zcr_list, endpoint_list, label_list = preprocessor.process(CONFIG['data list'])
        print('Data set Size:', len(wav_list))
        eff_zcr_list = np.zeros((1, 25))
        # Todo: Rewrite the relating preprocessor code.
        # Multiple data type mixed. Change the list of np array to pure np array.
        for i in range(len(zcr_list)):
            temp = preprocessor.effective_feature(zcr_list[i], endpoint_list[i])
            temp = preprocessor.reshape(temp, 25)
            if len(temp) == 0:
                label_list = label_list[0: i - 1] + label_list[i:]
                continue
            eff_zcr_list = np.concatenate((eff_zcr_list, temp), axis=0)
        eff_zcr_list = eff_zcr_list[1:]

        if CONFIG['argumentation']:
            # Todo: Add data argumentation
            raise NotImplementedError
        if 'all' in CONFIG['classifier']:
            for classifier_class in classifier_classes.values():
                if CONFIG['is training']:
                    # Todo: Print classifier name
                    # Todo: Print training result and validation result
                    # Todo: Save the model to a dir.
                    classifier = classifier_class(None)
                    classifier.train(eff_zcr_list, label_list)


if __name__ == '__main__':
    main()
