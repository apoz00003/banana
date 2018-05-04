import sys
from mbianalysis.study.mri.motion_detection_mixin_new import (  # @IgnorePep8 @Reimport
    create_motion_detection_class)

ref = 'reference_dicom'
t1s = ['t1_1_dicom']
t2s = ['t2_1_dicom']
epis = ['epi_dicom']
dmris = [['b0_plus', '1'], ['dwi_main', '0']]

class A(object):
    pass

MotionDetection, inputs = create_motion_detection_class(
    'MotionDetection', ref, 't1', t1s=t1s, t2s=t2s, epis=epis)

# m = sys.modules[__name__]

MotionDetection.__module__ = A.__module__
