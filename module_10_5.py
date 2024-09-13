import glob
import datetime
import multiprocessing


def read_lines(f_path):
    with open(f_path, "r", encoding='utf-8') as file:
        for line in file:
            yield line

def read_info(name):
    all_data = []
    for line in read_lines(name):
        all_data.append(line)

if __name__ == '__main__':
    start = datetime.datetime.now()
    filenames = glob.glob("files/*.txt")
    for name in filenames:
        read_info(name)
    end = datetime.datetime.now()
    print(f'Линейный вызов:\t\t{end - start}')

    start = datetime.datetime.now()
    filenames = glob.glob("files/*.txt")
    with multiprocessing.Pool(processes=3) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'Многопроцессорный:\t{end - start}')
