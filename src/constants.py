
import os
import platform

RPI_PLATFORM = False

#if platform.machine() == "aarch64":
#	RPI_PLATFORM = True

MILLIS_INCREMENT = 30  # 30 * 100 == 3000 millis is equal to 3 seconds

SCREEN_WELCOME = 0
SCREEN_PREDICT = 1
SCREEN_PROGRESS = 2

DEFAULT_CAMERA_IDX = 2

IMG_SIZE = (320, 240)

QUIT = 69
CAPTURE_IMG = 70
CAPTURE_IMG_DONE = 71
CLASSIFY_IMG = 72
CLASSIFICATION_DONE = 73

DATETIME_FORMAT = "%Y%m%d_%H%M%S"

BASE_DIR = os.getcwd()

SAVED_PREDICTIONS = os.path.sep.join([BASE_DIR, "saved_predictions"])
TEMP_IMG = os.path.sep.join([BASE_DIR, "src", "temp_img.jpg"])
MEAT_MODEL = os.path.sep.join([BASE_DIR, "models", "barong_svm_cnn_model3.h5"])
MEAT_LABELS = os.path.sep.join([BASE_DIR, "models", "barong_labels.txt"])
