import os
def get_sub_files(file_directory):
    """
    Get the list of all files in the given directory.
    Parameters:
        file_directory (str): The path to the directory.
    Returns:
        list: A list containing the full paths of all files in the directory.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(file_directory):
            print(f"Directory {file_directory} does not exist.")
            return []
        
        # Get the list of all files and build their full paths
        sub_files = [os.path.join(file_directory, file_name) for file_name in os.listdir(file_directory)]
        
        # Print the number of files and the type of the 'sub_files' variable
        print(f"Number of files in this dir: {len(sub_files)}")
        # print(f"Type of sub_files: {type(sub_files)}")
        
        # Return the first 10 files for review (if there are that many)
        return sub_files
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
import numpy as np

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # 地球半径（单位：千米）
    
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    
    a = np.sin(dlat/2) * np.sin(dlat/2) + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon/2) * np.sin(dlon/2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    
    distance = R * c * 1000  # 转换为米
    return distance
    
