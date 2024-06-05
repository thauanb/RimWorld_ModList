# RimWorld Mod List 

Lista todos os mods instalados na pasta apontada , retornando [ nome_mod , autor , packageId ]


## Instalação

Certifique-se de ter o Python instalado em seu ambiente. Você também precisará instalar as seguintes bibliotecas:
 - lxml

```python
pip install lxml
```

## Uso

A função "Listar Mods" está configurada para contar o número de ocorrências , assim como salvar a saida em um arquivo `.txt`

```python
list_mods(RIMWORLD_PATH)
```

## Exemplos de Aplicação

Suponha que você tenha a seguinte estrutura de pasta de mods:

```
RIMWORLD_PATH/
├── Mod1/
│   └── About/
│       └── About.xml
├── Mod2/
│   └── About/
│       └── About.xml
└── Mod3/
    └── About/
        └── About.xml
```

        
Quando você executar a função list_mods(RIMWORLD_PATH), ela vai percorrer todas as pastas, ler as informações de cada About.xml, contar as ocorrências e salvar a saída em um arquivo mod_list.txt com o formato:


```
Mod: NomeDoMod1, Autor: AutorDoMod1, PackageId: PackageIdDoMod1, Ocorrências: 1
Mod: NomeDoMod2, Autor: AutorDoMod2, PackageId: PackageIdDoMod2, Ocorrências: 1
...
```




