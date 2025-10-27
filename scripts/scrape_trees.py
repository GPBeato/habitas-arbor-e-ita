import requests
from bs4 import BeautifulSoup
import csv
import time
from pathlib import Path
import re

# Configurações
BASE_URL = "https://arvores.sjc.sp.gov.br/"
CSV_FILE = Path(__file__).parent.parent / "trees_all.csv"
START_ID = 1  # Será ajustado automaticamente
END_ID = 85000  # Pode ir além de 80k para garantir
DELAY_BETWEEN_REQUESTS = 0.5  # segundos (para não sobrecarregar o servidor)
SAVE_INTERVAL = 50  # salvar a cada 50 registros

def get_last_id_from_csv():
    """Obtém o último ID já coletado no CSV"""
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) > 1:
                last_line = lines[-1]
                last_id = int(last_line.split(';')[0])
                return last_id
    except Exception as e:
        print(f"Erro ao ler CSV: {e}")
        return 0
    return 0

def clean_text(text):
    """Limpa e normaliza o texto"""
    if text:
        return text.strip().replace('\n', ' ').replace('\r', '')
    return ""

def extract_tree_data(tree_id):
    """Extrai dados de uma árvore específica"""
    url = f"{BASE_URL}{tree_id}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Verifica se a página existe (não é erro 404 ou redirecionamento)
        if response.status_code != 200:
            return None
            
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Verifica se é uma página válida de árvore
        title = soup.find('h3')
        if not title or 'Árvore:' not in title.text:
            return None
        
        data = {
            'id': tree_id,
            'nome_popular': '',
            'nome_cientifico': '',
            'dap': '',
            'altura': '',
            'data_coleta': '',
            'latitude': '',
            'longitude': '',
            'laudos': '',
            'image_sources': ''
        }
        
        # Extrai os dados da página
        content = soup.get_text()
        
        # Nome Popular
        nome_popular_match = re.search(r'Nome Popular:\s*([^\n]+)', content)
        if nome_popular_match:
            data['nome_popular'] = clean_text(nome_popular_match.group(1))
        
        # Nome Científico
        nome_cientifico_match = re.search(r'Nome Científico:\s*([^\n]+)', content)
        if nome_cientifico_match:
            # Remove formatação de itálico se houver
            nome_cient = clean_text(nome_cientifico_match.group(1))
            data['nome_cientifico'] = nome_cient.replace('_', '').strip()
        
        # DAP
        dap_match = re.search(r'DAP[^:]*:\s*([^\n]+)', content)
        if dap_match:
            data['dap'] = clean_text(dap_match.group(1))
        
        # Altura
        altura_match = re.search(r'Altura:\s*([^\n]+)', content)
        if altura_match:
            data['altura'] = clean_text(altura_match.group(1))
        
        # Data da Coleta
        data_match = re.search(r'Data da Coleta:\s*([^\n]+)', content)
        if data_match:
            data['data_coleta'] = clean_text(data_match.group(1))
        
        # Latitude e Longitude
        lat_long_match = re.search(r'Latitude:\s*([^\s]+)\s*/\s*Longitude:\s*([^\n]+)', content)
        if lat_long_match:
            data['latitude'] = clean_text(lat_long_match.group(1))
            data['longitude'] = clean_text(lat_long_match.group(2))
        
        # Laudos (procura por links de laudos)
        laudos = []
        laudo_links = soup.find_all('a', href=re.compile(r'/Arvore/DownloadLaudo/'))
        for link in laudo_links:
            laudos.append(link['href'])
        data['laudos'] = ', '.join(laudos) if laudos else ''
        
        # Imagens
        images = []
        img_links = soup.find_all('a', href=re.compile(r'/Arvore/DownloadImg/'))
        for link in img_links:
            images.append(link['href'])
        
        # Também procura por imagens diretas
        img_tags = soup.find_all('img', src=re.compile(r'IMG-'))
        for img in img_tags:
            if img.get('src'):
                images.append(img['src'])
        
        data['image_sources'] = ', '.join(images) if images else ''
        
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar ID {tree_id}: {e}")
        return None
    except Exception as e:
        print(f"Erro ao processar ID {tree_id}: {e}")
        return None

def append_to_csv(data):
    """Adiciona uma linha ao CSV"""
    with open(CSV_FILE, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow([
            data['id'],
            data['nome_popular'],
            data['nome_cientifico'],
            data['dap'],
            data['altura'],
            data['data_coleta'],
            data['latitude'],
            data['longitude'],
            data['laudos'],
            data['image_sources']
        ])

def main():
    """Função principal do scraper"""
    print("=" * 60)
    print("Web Scraper - Árvores de São José dos Campos")
    print("=" * 60)
    
    # Determina o ID inicial
    last_id = get_last_id_from_csv()
    start_id = last_id + 1
    
    print(f"\nÚltimo ID no CSV: {last_id}")
    print(f"Iniciando coleta a partir do ID: {start_id}")
    print(f"ID final: {END_ID}")
    print(f"Total estimado de registros a coletar: {END_ID - start_id + 1}")
    print("-" * 60)
    
    collected = 0
    not_found = 0
    consecutive_not_found = 0
    max_consecutive_not_found = 100  # Para após 100 IDs consecutivos não encontrados
    
    for tree_id in range(start_id, END_ID + 1):
        print(f"\nColetando ID {tree_id}...", end=' ')
        
        data = extract_tree_data(tree_id)
        
        if data:
            append_to_csv(data)
            collected += 1
            consecutive_not_found = 0
            print(f"✓ Coletado ({collected} total)")
            
            # Log a cada 10 registros
            if collected % 10 == 0:
                print(f"\n{'='*60}")
                print(f"Progresso: {collected} árvores coletadas")
                print(f"Não encontrados: {not_found}")
                print(f"{'='*60}")
        else:
            not_found += 1
            consecutive_not_found += 1
            print(f"✗ Não encontrado")
            
            # Para se houver muitos IDs consecutivos não encontrados
            if consecutive_not_found >= max_consecutive_not_found:
                print(f"\n{'='*60}")
                print(f"AVISO: {max_consecutive_not_found} IDs consecutivos não encontrados.")
                print(f"Provavelmente chegamos ao fim do cadastro.")
                print(f"Último ID válido: {tree_id - max_consecutive_not_found}")
                print(f"{'='*60}")
                break
        
        # Aguarda entre requisições para não sobrecarregar o servidor
        time.sleep(DELAY_BETWEEN_REQUESTS)
    
    print("\n" + "=" * 60)
    print("Coleta finalizada!")
    print(f"Total de árvores coletadas: {collected}")
    print(f"IDs não encontrados: {not_found}")
    print(f"CSV salvo em: {CSV_FILE}")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nColeta interrompida pelo usuário.")
        print("O progresso foi salvo no CSV.")
    except Exception as e:
        print(f"\nErro fatal: {e}")
        import traceback
        traceback.print_exc()

