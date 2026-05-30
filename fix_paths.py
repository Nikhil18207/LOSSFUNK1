import json
import os
import subprocess
import shutil
from pathlib import Path

# 1. Update the Notebooks
bootstrap_cell = {
 'cell_type': 'code',
 'execution_count': None,
 'metadata': {},
 'outputs': [],
 'source': [
  'from _bootstrap import PROJECT_ROOT\\n',
  '# The _bootstrap import changes the working directory to the project root.\\n',
  '# This ensures that ./data, ./models, and ./results are saved in the correct place.'
 ]
}

notebooks = [
    'notebooks/01_training_pipeline.ipynb', 
    'notebooks/02_statistics_analysis.ipynb', 
    'notebooks/03_sublora_attack.ipynb'
]

for nb_file in notebooks:
    with open(nb_file, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Check if already added
    first_cell = nb['cells'][0]
    if 'source' in first_cell and len(first_cell['source']) > 0 and 'from _bootstrap import PROJECT_ROOT' in first_cell['source'][0]:
        continue
        
    nb['cells'].insert(0, bootstrap_cell)
    
    with open(nb_file, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

print('Notebooks updated successfully.')
