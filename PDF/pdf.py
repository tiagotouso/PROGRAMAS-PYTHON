
from PIL import Image
from pathlib import Path
from PyPDF2 import PdfMerger


path = Path('.')
INT_IMAGEM = path / 'INT_IMAGEM'
INT_PDF_MERGE = path / 'INT_PDF_MERGE'
OUT_PDF = path / 'OUT_PDF'


def merge_pdfs(pdf_list, output_path):
    try:
        merger = PdfMerger()
        for pdf in pdf_list:
            merger.append(pdf)
        
        merger.write(output_path)
        merger.close()
        print(f"PDFs concatenados com sucesso: {output_path}")
    except Exception as e:
        print(f"Erro ao concatenar PDFs: {e}")


def image_to_pdf(image_path, output_path):

    try:
        # Abre a imagem
        image = Image.open(image_path)
        
        # Converte para modo RGB (caso seja PNG ou tenha transparência)
        if image.mode in ("RGBA", "P" ):
            image = image.convert("RGB")
        
        # Salva como PDF
        image.save(output_path, "PDF", resolution=100.0)
        print(f"Arquivo salvo com sucesso: {output_path}")

    except Exception as e:
        print(f"Erro ao converter imagem para PDF: {e}")


def converter_imagens():

    for caminho_int in INT_IMAGEM.glob('*.*'):
        caminho_out = OUT_PDF / f'{caminho_int.stem}.pdf'

        image_to_pdf(caminho_int, caminho_out)


def juntar_pdfs():

    for pasta in INT_PDF_MERGE.glob('*'):

        pdfs = pasta.glob('*.*')
        caminho_out = OUT_PDF / f'{pasta.name}.pdf'
        merge_pdfs(pdfs, caminho_out)


# Exemplo de uso
if __name__ == "__main__":

    print('-' * 20)
    menu = '''
Digete
1 - Para converter Imagem em PDF
2 - Para Juntar varios PDF em um arquivo
'''
    print(menu)

    print('-' * 20)

    opcao = input('Informe uma opção: ')

    match opcao:
        case 1:
            converter_imagens()
        case 2: 
            juntar_pdfs()
        case _:
            print('Opção inválida!')
            print('')








