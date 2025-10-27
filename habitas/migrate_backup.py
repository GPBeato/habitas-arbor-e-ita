#!/usr/bin/env python3
"""
Script para migrar dados do banco antigo para o novo
"""
import sqlite3
import sys

def migrate_data():
    # Conectar aos bancos
    old_db = sqlite3.connect('db.sqlite3.backup')
    new_db = sqlite3.connect('db.sqlite3')
    
    old_cursor = old_db.cursor()
    new_cursor = new_db.cursor()
    
    try:
        # Migrar Species
        print("Migrando Species...")
        old_cursor.execute("SELECT id, name, bio_index FROM main_species")
        species = old_cursor.fetchall()
        for sp in species:
            try:
                new_cursor.execute(
                    "INSERT INTO main_species (id, name, bio_index) VALUES (?, ?, ?)",
                    sp
                )
            except sqlite3.IntegrityError:
                print(f"Species {sp[0]} já existe, pulando...")
        
        print(f"✓ {len(species)} espécies migradas")
        
        # Migrar Trees
        print("Migrando Trees...")
        old_cursor.execute("""
            SELECT id, N_placa, nome_popular, nome_cientifico, dap, altura, 
                   latitude, longitude, laudo, imagem, plantado_por, species_id
            FROM main_tree
        """)
        trees = old_cursor.fetchall()
        
        for tree in trees:
            try:
                new_cursor.execute("""
                    INSERT INTO main_tree 
                    (id, N_placa, nome_popular, nome_cientifico, dap, altura, 
                     latitude, longitude, laudo, imagem, plantado_por, species_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, tree)
            except sqlite3.IntegrityError:
                print(f"Tree {tree[0]} já existe, pulando...")
        
        print(f"✓ {len(trees)} árvores migradas")
        
        # Migrar Posts (comentários)
        print("Migrando Posts...")
        old_cursor.execute("""
            SELECT id, author, content, created_on, specialized, tree_id
            FROM main_post
        """)
        posts = old_cursor.fetchall()
        
        for post in posts:
            try:
                new_cursor.execute("""
                    INSERT INTO main_post 
                    (id, author, content, created_on, specialized, tree_id)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, post)
            except sqlite3.IntegrityError:
                print(f"Post {post[0]} já existe, pulando...")
        
        print(f"✓ {len(posts)} posts migrados")
        
        # Commit e fechar
        new_db.commit()
        print("\n✅ Migração concluída com sucesso!")
        
    except Exception as e:
        print(f"\n❌ Erro durante migração: {e}")
        new_db.rollback()
        return False
    finally:
        old_db.close()
        new_db.close()
    
    return True

if __name__ == '__main__':
    print("=" * 60)
    print("MIGRAÇÃO DE DADOS DO BACKUP")
    print("=" * 60)
    print()
    
    if migrate_data():
        print("\n✅ Dados restaurados com sucesso!")
        sys.exit(0)
    else:
        print("\n❌ Falha na migração!")
        sys.exit(1)
