# Para salvar no banco de dados, execute:
# python manage.py shell
# exec(open('../scripts/salvar_banco.py').read())
import csv
from main.models import Tree
trees_in_db = set(Tree.objects.values_list('id', flat=True).all())
with open('../trees_all.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader, None)  # pular cabeçalho
    trees = []
    for row in csv_reader:
        try:
            ID = int(row[0]) + 2000  # pular os ids que já estão no banco
            nome_popular = row[1]
            nome_cientifico = row[2]
            dap = int(row[3].split(' ')[0])
            altura = float(row[4].split(' ')[0].replace(',', '.'))
            latitude = float(row[6].replace(',', '.'))
            longitude = float(row[7].replace(',', '.'))
            laudos = row[8]
            imagens = row[9]
            plantado_por = "Prefeitura"
            if ID not in trees_in_db:
                trees.append(Tree(id=ID, N_placa=ID, nome_popular=nome_popular, nome_cientifico=nome_cientifico, dap=dap, altura=altura, latitude=latitude,
                                  longitude=longitude, laudo=laudos, imagem=imagens, plantado_por=plantado_por))
        except ValueError:
            print('Unable to convert row', row)
    print('salvando', len(trees), 'arvores')
    Tree.objects.bulk_create(trees)
