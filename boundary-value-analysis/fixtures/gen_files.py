import math
import os

class TestFile:
    def __init__(self, description, label, size_in_bytes, chunk_size=50 * math.pow(2, 20)):
        self.description = description
        self.label = label
        self.size_in_bytes = int(size_in_bytes)
        self.chunk_size = int(chunk_size)

    def gen(self):
        path = f'{os.path.dirname(__file__)}/{self.label}.txt'
        print(f'generating {path}')

        if os.path.exists(path):
            os.remove(path)

        file = open(path, 'a')
        if self.size_in_bytes == 0:
            file.close()
            return

        bytes = []
        for i in range(self.size_in_bytes):
            # end of chunk
            if i > 0 and i % self.chunk_size == 0:
                file.write(''.join(bytes))
                bytes = []
                bytes.append('1')
                continue

            bytes.append('1')
            
            if i == self.size_in_bytes - 1:
                file.write(''.join(bytes))

        file.close()

        print(f'completes {path}')


def main():
    _1MB_in_bytes = math.pow(10, 6)
    _1MiB_in_bytes = math.pow(2, 20)

    files = [
        TestFile('x(min-1)', '0B', 0),
        TestFile('x(min)', '1B', 1),
        TestFile('x(min+1)', '2B', 2),

        TestFile('x(normal)', '1MB', _1MB_in_bytes),

        TestFile('x(max-1)', '500MiB-1B', 500 * _1MiB_in_bytes - 1),
        TestFile('x(max)', '500MiB', 500 * _1MiB_in_bytes),
        TestFile('x(max + 1)', '500MiB+1B', 500 * _1MiB_in_bytes + 1),
    ]

    for test_file in files:
        test_file.gen()


if __name__ == '__main__':
    main()
