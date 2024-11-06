from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

def criar_pdf(nome_arquivo, nome_paciente, data, exames_selecionados):
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura, altura = A4

    # Cabeçalho
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, altura - 50, "Prefeitura Municipal De Santa Rita - PB")
    c.setFont("Helvetica", 10)
    c.drawString(30, altura - 70, "Endereço: Rua Exemplo, 123 - Cidade - Estado - CEP")
    c.drawString(30, altura - 85, "Telefone: (21) 9999-9999 | Email: contato@laboratorio.com")

    # Informações do paciente
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, altura - 120, "Nome do Paciente:")
    c.setFont("Helvetica", 10)
    c.drawString(150, altura - 120, nome_paciente)
    
    c.drawString(30, altura - 140, "Data de Solicitação:")
    c.drawString(150, altura - 140, data)

    # Criar uma tabela simples para os exames
    c.drawString(30, altura - 180, "Exames Solicitados:")

    # Criar uma tabela com os exames
    dados_exames = [["Exame", "Selecionado"]]
    for exame in exames_selecionados:
        dados_exames.append([exame, "✔"])

    tabela = Table(dados_exames, colWidths=[300, 50])
    estilo = TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                         ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                         ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                         ("GRID", (0, 0), (-1, -1), 1, colors.black)])
    tabela.setStyle(estilo)

    # Posição da tabela
    tabela.wrapOn(c, largura, altura)
    tabela.drawOn(c, 30, altura - 280)

    # Salvar o PDF
    c.save()

# Exemplo de uso
exames = ["Hemograma Completo", "Glicose", "Colesterol Total"]
criar_pdf("Maria-da-Penha-Alves-Rufino.pdf", "Maria da Penha Alves Rufino", "24/10/2024", exames)
