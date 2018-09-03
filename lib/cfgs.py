from easydict import EasyDict as edict

##############################################################################
# Load this dictionary with the layer names and the desired number of
# retained channels per layer.
c=edict()# TODO: easy dict does not have order. Try using Ordered Dict to print dc cfgs in order
c.noLastConv = False #In some models like vgg-cifar.prototx, the last-layer pruning yeilds an implemetnation error, Set this flag to True to avoid last layer pruning.

# dcdic holds the number of retained channels
# For example, for VGG net we can use the pruning degree suggested in (Li et.al., 2017)
c.dcdic = {'conv1_1': 32,
'conv1_2': 32,
'conv2_1': 128,
'conv2_2': 128,
'conv3_1': 256,
'conv3_2': 256,
'conv3_3': 256,
'conv4_1': 256,
'conv4_2': 256,
'conv4_3': 256,
'conv5_1': 256,
'conv5_2': 256,
'conv5_3': 256}

#############################################################################################
## NOTE: Is not necessary to alter the following configuration for runing the filter pruning 
## demo code!
#############################################################################################
gpu=False
dataset="imagenet" # cifar10
caffe_vis = '0,1,2,3'
tf_vis = '4,5,6,7'
accname = None
frozenname= None
layer = False # this might be for single layer evalation? Is called in several methods, including c3.solve() -by Mario
gt_feats = False # gt stands for ground truth -by Mario
_points_dict_name = "points_dict"
noTF = False
noTheano = True
imagenet_val = "path/to/caffe/examples/imagenet/ilsvrc12_val_lmdb"
cifar10_val = 'path/to/cifar-10-batches-py/test'
caffe_path = "path/to/caffe/build/tools/caffe"
mp=0
alpha=1e-3 #2e-5 # 1e-2
# resnet56 14% 7e-4
class Action:
    train='train'
    layer='layer'
    cifar='cifar'
    addbn='addbn'
    splitrelu='splitrelu'
    c3='c3'
    combine='combine'
class datasets:
    cifar='cifar10'
    imagenet='imagenet'
class kernels:
    dic='dic'
    pruning='pruning'
class resnet:
    solve_sum=True
    solve_conv=True
class Feats:
    decompose_method = 1
    inplace = False
class solvers:
    lightning='lightning'
    sk = 'sklearn'
    lowparams = 'lowparams'
    gd = 'gd'
    keras = 'keras'
    tls = "tls"
class pruning_options: # TODO: Consider adding another pruning option for alexnet, i.e. alexnet=2 -by Mario
    prb=0
    vgg=3
    resnet=4
    single=10
class Data:
    lmdb='lmdb'
    pro='pro'


class Models: # TODO: Consider adding a new attribute to the this class for alexnet -by Mario
    alexnet='alexnet'
    vgg='vgg'
    xception='xception'
    resnet='resnet'
    rescifar='rescifar'

class vgg:
    model='temp/vgg.prototxt'
    weights='temp/vgg.caffemodel'
    accname='accuracy@5'
    flop=15346630656
    #TODO: fill this list automatically reading from the prototxt (the authors do not include the con5_x layers becuase they have fewcontribution to FLOP)
    """
    alldic = ['conv1_1',
              'conv2_1',
              'conv3_1',
              'conv3_2',
              'conv4_1',
              'conv4_2',
              'conv4_3',
              'conv5_1',
              'conv5_2']
    """
    #NOTE!!!: delete conv4_3 and following for pruning with R3
    #         delete conv5_1 and following for pruning with R1
    #         extended list is for pruning with F1
    #pooldic= ['conv1_2', 'conv2_2','conv3_3'] #TODO: fill this list automatically reading from the prototxt( the authors say we might want to avoid pruning conv3_3 (sensitivity?))
    """
    rankdic = {'conv1_1': 17,
               'conv1_2': 17,
               'conv2_1': 37,
               'conv2_2': 47,
               'conv3_1': 83,
               'conv3_2': 89,
               'conv3_3': 106,
               'conv4_1': 175,
               'conv4_2': 192,
               'conv4_3': 227,
               'conv5_1': 398,
               'conv5_2': 390,
               'conv5_3': 379}"""
    #TODO: fill this dict based on our research
    #dcdic = {'conv1_1': 24, 'conv1_2': 22, 'conv2_1': 41,'conv2_2': 51,'conv3_1': 108,'conv3_2': 89,'conv3_3': 111,'conv4_1': 233,'conv4_2': 256,'conv4_3': 302, 'conv5_1': 398, 'conv5_2': 390,'conv5_3': 379}#for a x5 speed-up

class alexnet:
    model='temp/alexnet.prototxt'
    weights='temp/alexnet.caffemodel'
    accname='accuracy@5'
    flop=1080502272
    """
    alldic = ['conv1',
              'conv2',
              'conv3',
              'conv4'] """#TODO: fill this list automatically reading from the prototxt
    #pooldic= ['conv1','conv2','conv5'] #TODO: fill this list automatically reading from the prototxt
    #rankdic = {}  #TODO: fill this dict based on our research
    #dcdic = {'conv1': 48,'conv2': 152,'conv3': 192,'conv4': 192,'conv5': 192}#x2 naive assignation)

c.dic = edict()
c.dic.option=pruning_options.prb
c.dic.layeralpha=1
c.dic.debug=0
c.dic.afterconv=False
c.dic.fitfc=0
c.dic.keep = 3.
c.dic.rank_tol = .1
c.dic.prepooling = 1
c.dic.alter=0
c.dic.vh=1  # The excution of purning depends on this flag. However it also determines the execution of VH decomposition -by Mario
           # How to unlink the execution of both algoritms? -by Mario
# single layer
c.an = edict()
c.an.l1 = '' #'conv1_1'
c.an.l2 = '' #'conv1_2'
c.an.ratio = 2
c.an.filter = 0

# resnet
c.res=edict()
c.res.short = 0
c.res.bn = 1

# vh
#c.vh=edict()
#c.vh.ls=0

c.Action = Action.train
c.mp=True
c.kernelname='dic'
c.fc_ridge = 0
c.ls='linear'
c.nonlinear_fc = 0
c.nofc=0
c.splitconvrelu=True
c.nBatches=500
c.ntest = 0
c.nBatches_fc=c.nBatches * 10
c.frozen=0
c.nPointsPerLayer=10
c.fc_reg=True
c.autodet = False
c.solver=solvers.sk
c.shm='/tmp' #'/dev/shm'
c.log='logs/'
c.data=Data.lmdb
c.model=''
c.weights= ''
c.prototxt= ''


def set_nBatches(n):
    c.nBatches = n
    c.nBatches_fc=c.nBatches# * 10
