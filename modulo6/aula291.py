''' Pathlib '''
from pathlib import Path


project_path = Path()  # retorna caminho completo do projeto

# print(project_path.absolute())

file_path = Path(__file__)  # retorna caminho completo do arquivo atual
# print(file_path)

# print(file_path.parent)  # retorna sempre a pasta acima

# a barra serve pra concatenar path
new_filepath = file_path.parent / 'new.txt'

# print(new_filepath)

# print(Path.home())  # retorna o home do sistema
file = Path.home() / 'Desktop' / 'arquivo.txt'
# file.touch()  # criou o arquivo
# file.write_text('Hello World')  # escreve no arquivo
# print(file.read_text())  # le o arquivo

file.write_text('')  # escreve no arquivo

with file.open('a+') as file_:
    file_.write('Uma linha \n')
    file_.write('Outra linha \n')

file.unlink()  # deleta o arquivo

archive = Path.home() / 'Desktop' / 'aula291'
archive.mkdir(exist_ok=True)

subfolder = archive / 'subfolder'
subfolder.mkdir(exist_ok=True)

other_file = subfolder / 'file.txt'
other_file.touch()
other_file.write_text('Heeey')

# archive.rmdir()  # remove pasta, mas só se tiver vazio
