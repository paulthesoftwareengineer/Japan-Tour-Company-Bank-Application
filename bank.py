import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project " + directory)
        os.makedirs(directory)

def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def main():
    create_project_dir(PROJECT_NAME)
    create_data_files(PROJECT_NAME, BASE_URL)

if __name__ == "__main__":
    main()
