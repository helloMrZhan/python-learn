# 使用shutil对文件夹进行zip压缩，压缩过程显示进度条

import os
import shutil
import logging
from progress.bar import IncrementalBar

logger = logging.getLogger(__name__)


def count_files_in_dir(dir):
    totalFiles = 0
    for base, dirs, files in os.walk(dir):
        totalFiles += len(files)
    return totalFiles


def zip_with_progress(dir_path, zip_file):
    bar = None
    total_files = count_files_in_dir(dir_path)

    # 进度条显示
    def progress(*args, **kwargs):
        if not args[0].startswith('adding'):
            return

        nonlocal bar, total_files
        if bar is None:
            print('@开始压缩:{}'.format(zip_file))
            bar = IncrementalBar('正在压缩:', max=total_files)
        bar.next(1)

    # 调用shutil.make_archive时，临时替换其 logger 参数，用来显示进度条
    old_info = logger.info
    logger.info = lambda *args, **kwargs: progress(*args, **kwargs)
    shutil.make_archive(dir_path, 'zip', dir_path, logger=logger)
    logger.info = old_info

    if bar is not None:
        bar.finish()


if __name__ == '__main__':
    zip_with_progress('./', '/tmp/test_file_zip.zip')
    print()