# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os


name_dir = 'my_project'
names_folder = ['settings', 'mainapp', 'adminapp', 'authapp']

for i in names_folder:
    dir_name = os.path.join(name_dir, i)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


