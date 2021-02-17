# DEFAULT BASE DIRS
GENERAL_DISPLAY=":0"
PYTHON_PATH="/opt/conda/envs/cidia19/bin/python"
CONDA_ENV_NAME="cidia19"

# LOG AND RESULTS CSV FILE
BASE_LOG_CSV_PATH = '/data/status.csv'
LOG_CSV_COLUMNS = ['name', 'study_id', 'to_nifti', 'segmented', 'to_slices_3d', 'to_video', 'predicted', 'percentage', 'axis_detail', 'axis_qty']
AXIS = 2

# DICOM -> NIFTI
BASE_DICOM_INPUT_DIR = '/data/dicom-original/exame-pulmao'
BASE_NII_ORIGINAL_OUTPUT_DIR = '/data/nii-original/exame-pulmao'

# PHNN SEGMENTATION
PHNN_EXECUTABLE_PATH = '/opt/p-hnn/segment_lung_phnn.py' 
BASE_SEGMENTED_OUTPUT_DIR = '/data/nii-segmented/exame-pulmao'
PHNN_THRESHOLD = 0.75
PHNN_BATCH_SIZE = 10

# MITK
# DEFAULT VALUES FOR VIDEO CREATION
BASE_MITK_VIDEO_OUTPUT_DIR = '/data/videos'
BASE_MITK_VIEWS_OUTPUT_DIR = '/data/slices2d/exame-pulmao'
MITK_TRANSFER_FUNCTION_PATH = '/data/tf/tf12_2.xml'
MITK_VIDEO_EXECUTABLE_PATH = '/opt/video-maker-mitk/build/videomaker' 
MITK_VIDEO_WIDTH = 512 #px
MITK_VIDEO_HEIGHT = 450 #px
MITK_VIDEO_TIME = 10.0 # In seconds
MITK_VIDEO_FPS = 30

# DEFAULT VALUES FOR SLICES CREATION
MITK_VIEWS_EXECUTABLE_PATH = '/opt/screenshot-axis-views/build/screenshot-axis-views' 
MITK_VIEWS_WIDTH = 448 #px
MITK_VIEWS_HEIGHT = 448 #px
MITK_VIEWS_LENGTH = 82 # If not even is going to add 1 till MITK_VIEWS_LENGTH/2 is odd
MITK_VIEWS_AXIS = 2 # The view from 1 till 4

# RESNET DEFAULT VALUES FOR LOAD AND EXECUTE MODEL FOR PREDICTIONS
PREDICTION_MODEL_PATH = '/data/resnet101/model'
PREDICTION_MODEL = 'resnet101'
PREDICTION_LEGEND_PATH = '/data/resnet101/legend'
PREDICTION_AXIS = 2
PREDICTION_CLASSES = 2
PREDICTION_WIDTH = 448
PREDICTION_HEIGHT = 488

# ACCESS TO API
API_URL = 'https://cidia.ufrgs.dev/api/v1/exam-classifications'
API_USERNAME = 'username'
API_PASSWORD = 'password'

