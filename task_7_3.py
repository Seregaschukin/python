# 3. Создать структуру файлов и папок, «руками» в проводнике.
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html

# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
#
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
# Примечание: исходные файлы необходимо оставить;
# обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.

import os
from os.path import join
import shutil

main_dirs = 'my_project'
save_dirs = 'my_project/templates'
way = 'templates'

for root, dirs, files in os.walk(main_dirs):
    if way in dirs:
        shutil.copytree(join(root, way), save_dirs, dirs_exist_ok=True)