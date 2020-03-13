import settings
import path
import data

import os

"""
    This file helps you extract your own dataset
"""


# The file extractor search directories for files that matches the label

# starting point of the file extractor

paths = path.PathExtractor(settings.crawl_from, settings.labels)

index = 0

# loop through directories

while index < len(paths.known_paths):

    # add new path to the list

    paths.add_to_path(paths.known_paths[index])

    index = index + 1


# where the data should be saved to

file_extractor = data.DataExtractor(settings.keywords, 'python')

for input_file, file_label in paths.files:

    # reads the file

    file_extractor.read_file(input_file)

    # remove comment

    file_extractor.remove_comment()

    # extract keywords

    file_extractor.extract_keywords()

    # save output

    file_extractor.write_file(settings.output_file)
