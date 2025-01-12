# -*- coding:utf-8 -*-
import os


def remove_htmls(source_dir: str = "."):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                os.remove(file_path)


if __name__ == "__main__":
    remove_htmls()
