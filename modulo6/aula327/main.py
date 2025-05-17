'''Trabalhando com PDFs'''
from pypdf import PdfReader, PdfWriter
from pathlib import Path

PATH = Path(__file__).parent
SOURCE = PATH / 'pdfs_originais'
NEW = PATH / 'new_files'

FOCUS = SOURCE / 'R20250509.pdf'
NEW.mkdir(exist_ok=True)

reader = PdfReader(FOCUS)


page0 = reader.pages[0]
image0 = page0.images[0]

# print(page0.extract_text())

'''Extrair imagem de um pdf'''
# with open(NEW / image0.name, 'wb') as fp:
#     fp.write(image0.data)

'''Salvar cada pag num pdf'''
# for i, page in enumerate(reader.pages):
#     writer = PdfWriter()
#     with open(NEW / f'page_{i}.pdf', 'wb') as file:
#         writer.add_page(page)
#         writer.write(file)

merger = PdfWriter()

files = [
    NEW / 'page_1.pdf',
    NEW / 'page_0.pdf',
]

for file in files:
    merger.append(file) #type: ignore
    with open(NEW / 'Merged.pdf', 'wb') as file:
        merger.write(file) #type: ignore