"""
Script de teste para o web scraping de árvores
Testa algumas páginas específicas antes de executar o scraping completo
"""

import sys
from pathlib import Path

# Adiciona o diretório do script ao path
sys.path.insert(0, str(Path(__file__).parent))

from scrape_trees import extract_tree_data

def test_tree_ids():
    """Testa alguns IDs conhecidos"""
    test_ids = [71000, 1, 15000, 50000, 80000]
    
    print("=" * 70)
    print("TESTE DO WEB SCRAPER - ÁRVORES DE SÃO JOSÉ DOS CAMPOS")
    print("=" * 70)
    print("\nTestando extração de dados de algumas árvores...\n")
    
    successful = 0
    failed = 0
    
    for tree_id in test_ids:
        print(f"\n{'='*70}")
        print(f"Testando ID: {tree_id}")
        print('-' * 70)
        
        data = extract_tree_data(tree_id)
        
        if data:
            successful += 1
            print("✓ Sucesso!")
            print(f"Nome Popular: {data['nome_popular']}")
            print(f"Nome Científico: {data['nome_cientifico']}")
            print(f"DAP: {data['dap']}")
            print(f"Altura: {data['altura']}")
            print(f"Data Coleta: {data['data_coleta']}")
            print(f"Latitude: {data['latitude']}")
            print(f"Longitude: {data['longitude']}")
            print(f"Laudos: {data['laudos'][:50]}..." if len(data['laudos']) > 50 else f"Laudos: {data['laudos']}")
            print(f"Imagens: {data['image_sources'][:50]}..." if len(data['image_sources']) > 50 else f"Imagens: {data['image_sources']}")
        else:
            failed += 1
            print("✗ Falhou - Árvore não encontrada ou erro na extração")
    
    print(f"\n{'='*70}")
    print("RESULTADO DOS TESTES")
    print(f"{'='*70}")
    print(f"Sucessos: {successful}/{len(test_ids)}")
    print(f"Falhas: {failed}/{len(test_ids)}")
    
    if successful > 0:
        print("\n✓ O scraper está funcionando!")
        print("\nPara executar o scraping completo:")
        print("  python scripts\\scrape_trees.py")
    else:
        print("\n✗ Problemas detectados. Verifique sua conexão e o site.")
    
    print("=" * 70)

if __name__ == "__main__":
    test_tree_ids()

