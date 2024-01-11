import os

def get_subdirs(b='.'):
    '''
        Returns all sub-directories in a specific Path
    '''
    result = []
    for d in os.listdir(b):
        bd = os.path.join(b, d)
        if os.path.isdir(bd):
            result.append(bd)
    return result

def get_detection_folder():
    '''
        Returns the latest folder in a runs\detect
    '''
    detect_path = os.path.join('runs', 'detect')
    detect_path_absolute = os.path.abspath(detect_path)

    # Get the absolute paths of all subdirectories
    subdirs_absolute = [os.path.abspath(subdir) for subdir in get_subdirs(detect_path)]

    return max(subdirs_absolute, key=os.path.getmtime)

def check_folders():
    paths = {
        'data_path' : 'data',
        'images_path' : 'data/images',
        'videos_path' : 'data/videos'
    }
    
    # Check whether the specified path exists or not
    notExist = list(({file_type: path for (file_type, path) in paths.items() if not os.path.exists(path)}).values())
    
    if notExist:
        print(f'Folder {notExist} does not exist. We will create it.')
        # Create a new directory because it does not exist
        for folder in notExist:
            os.makedirs(folder)
            print(f"The new directory {folder} is created!")

# Uncomment the next line to check folders when this script is executed
# check_folders()
