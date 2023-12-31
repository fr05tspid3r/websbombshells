import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


def create_data_files(project_name, base_url):   
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
        write_file(crawled, '')


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def appand_to_file(path, data):
  with open(path, 'a') as file:
    file.write(data + '\n')

def delete_file_contents(path):
  with open(path, 'w'):
    pass

# Read a file and convert each line to a set items
def file_to__set(file_name):
  results = set()
  with open()file_name, 'rt') as f:
    for line in f:
      results.add(line.replace('\n', ''))
  return results

# Iterate through a set, each item will be a new line in the file.
def set_to_file(links, file):
  delete_file_content(file)
  for link in sorted(links):
    append_to_file(file, link)

















