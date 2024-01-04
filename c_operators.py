file_path = r'....\hello_world.txt'

# Записываем построчно в txt
with open(file_path, 'w') as file:
    file.write('"Hello"\n\n"world"')

# Очишаем txt
open(file_path, 'w').close()
