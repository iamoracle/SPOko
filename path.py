import os

from typing import Dict

class PathExtractor():

    def __init__(self, start_directory, file_extension_label: Dict):

        """
            automatically discovers files with certain extension and label them\n

            file_extention_label = {file_extension: file_label, file_extension2: file_label2}\n

            e.g file_extention_label = {'py': 'python', 'cpp': 'c++', 'php': 'php'}
        """

        self.files = []

        self.known_paths = [os.path.realpath(start_directory)]

        self.file_extension_label = file_extension_label



    def add_to_path(self, path):

        if os.path.isfile(path):

            for file_extension_label in self.file_extension_label:

                if path.endswith('.'+file_extension_label):

                    self.files.append((path, self.file_extension_label[file_extension_label]))

                    return True
                    
        elif os.path.isdir(path):

            paths = [os.path.join(path, _path) for _path in os.listdir(path)]

            self.known_paths = self.known_paths + paths

        return False



if __name__ == "__main__":

    # starting point of the file extractor

    start_from = 'C:/Users/files'

    labels = {'php': 'php', 'py': 'python'}

    paths = PathExtractor(start_from, labels)

    index = 0

    # loop through directories

    while index < len(paths.known_paths):

        # add new path to the list

        paths.add_to_path(paths.known_paths[index])

        index = index + 1

    # prints all known files with their label

    print(paths.files)


