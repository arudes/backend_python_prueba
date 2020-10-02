"""import json
from podcast import podcast

resultado = podcast[0]['feed']['results']
try:
    with open('C:\\Users\\Maldonado\\Desktop', 'w', encoding='utf-8') as file:
        json.dump(resultado, file, indent=4, ensure_ascii=False)
except KeyError:
    print("Error con la clave")"""

from pathlib import WindowsPath
from podcast import podcast
import json

dir = WindowsPath('C:\\Users\\Maldonado\\Desktop')
dir2 = dir / "data.json"
fichero = podcast[0]['feed']['results']

with dir2.open("w", encoding='utf-8') as fp:
    json.dump(fichero, fp, indent=4, ensure_ascii=False)
#fichero.write_text(json.dumps(fichero), encoding="utf8")