import re, csv
from os import path
from typing import List
import settings

class DataExtractor(object):

    def __init__(self, keywords: List, label=None):

        self.keywords = keywords

        self.label = label


    def extract_keywords(self):

        keywords = '|'.join(self.keywords)

        regex = r'%s' % keywords

        self.content = ' '.join(re.findall(regex, self.content))


    def remove_comment(self):

        # remove comments from content

        self.content = re.sub(r'\"\"\"[\s\S]*?\"\"\"', '',
                                self.content)  # for python multi-line comments

        self.content = re.sub(r'#(.*)', '',
                            self.content)  # for python single-line comments

        self.content = re.sub(r'\/\*[\s\S]*\*\/?', '',
                                self.content)  # for c style multi-line comments

        self.content = re.sub(r'\/\/(.*)', '',
                                self.content)  # for python single line comments

        self.content = re.sub(r'\<\!\-\-[\s\S]*\-\-\>', '',
                                self.content)  # for html comments


    def write_file(self, output_file):

        with open(output_file,'a+') as output_file:

            csv_file = csv.writer(output_file)

            if self.content == '':

                return

            csv_file.writerow([self.content, self.label])

    def read_file(self, input_file):

        with open(input_file, 'r') as file_content:

            self.raw_content = self.content = file_content.read()


if __name__ == "__main__":

    data_path = path.dirname(path.realpath(__file__))

    file_path_in = path.join(data_path, 'combiner.py')

    file_path_out = path.join(data_path, 'dataset.csv')

    file_extractor = DataExtractor(settings.keywords, 'python')

    file_extractor.read_file(file_path_in)

    file_extractor.remove_comment()

    file_extractor.extract_keywords()

    file_extractor.write_file(file_path_out)