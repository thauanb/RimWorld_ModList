# RimWorld Mod List

Lists all the mods installed in the specified folder, returning [mod_name, author, packageId].

## Installation

Make sure you have Python installed in your environment. You will also need to install the following libraries:
- lxml

```bash
pip install lxml
```

## Usage

The "List Mods" function is configured to count the number of occurrences as well as save the output to a `.txt` file.

```python
list_mods(RIMWORLD_PATH)
```

## Application Examples

Suppose you have the following mod folder structure:

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

When you run the `list_mods(RIMWORLD_PATH)` function, it will traverse all the folders, read the information from each `About.xml`, count the occurrences, and save the output to a `mod_list.txt` file in the following format:

```
Mod: ModName1, Author: Author1, PackageId: PackageId1, Occurrences: 1
Mod: ModName2, Author: Author2, PackageId: PackageId2, Occurrences: 1
...
```