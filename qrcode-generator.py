import qrcode
import argparse

# Configurar o parser de argumentos
parser = argparse.ArgumentParser(description="Gerador de QR Code")
parser.add_argument("--url", type=str, required=True, help="URL ou texto para codificar no QR Code")
parser.add_argument("--output", type=str, required=True, help="Nome do arquivo de saída (ex: qrcode.png)")
args = parser.parse_args()

# Dados que você quer codificar no QR Code (passados como argumento)
data = args.url

# Criar um objeto QR Code
qr = qrcode.QRCode(
    version=1,  # Controla o tamanho do QR Code (1 é o menor, 40 é o maior)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro
    box_size=10,  # Tamanho de cada "caixa" do QR Code
    border=4,  # Tamanho da borda (em caixas)
)

# Adicionar os dados ao QR Code
qr.add_data(data)
qr.make(fit=True)

# Criar uma imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salvar a imagem com o nome passado como argumento
img.save(args.output)

print(f"QR Code gerado e salvo como '{args.output}'")