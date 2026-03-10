import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import traceback

# Chemin vers ton notebook
notebook_path = "Project.ipynb"

# Charger le notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Créer l'exécuteur de notebook
ep = ExecutePreprocessor(timeout=600, kernel_name="python3")

# Fonction pour exécuter chaque cellule et afficher rendu
def run_notebook(nb):
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            print(f"\n--- Cellule {i} (Markdown) ---")
            print(cell.source[:500])  # aperçu Markdown
            continue
        
        print(f"\n--- Cellule {i} (Code) ---")
        print(cell.source[:500])  # aperçu du code
        
        try:
            # Exécution de la cellule
            ep.preprocess_cell(cell, {"metadata": {}, "cell_index": i}, nb)
            print("✅ Exécutée avec succès !")
            
            # Affichage des sorties (texte ou images)
            for output in cell.get("outputs", []):
                if output.output_type == "stream":
                    print(output.text)
                elif output.output_type == "error":
                    print("\n💥 Erreur détectée :", "\n".join(output.traceback))
                elif output.output_type == "display_data":
                    print("📊 Données affichées (images/HTML)...")
                
        except Exception as e:
            print(f"\n❌ Exception capturée : {e}")
            traceback.print_exc()
            # Option : ici tu peux ajouter un auto-correcteur simple
            # Exemple : installer automatiquement une librairie manquante
            if "ModuleNotFoundError" in str(e):
                missing_module = str(e).split("'")[1]
                print(f"💡 Tentative d'installation de {missing_module}...")
                import os
                os.system(f"pip install {missing_module}")
                print("🔁 Ré-exécution de la cellule après installation...")
                try:
                    ep.preprocess_cell(cell, {"metadata": {}, "cell_index": i}, nb)
                    print("✅ Exécutée après correction !")
                except Exception as e2:
                    print(f"⚠️ Toujours une erreur : {e2}")

# Lancer l'exécution
run_notebook(nb)