# PyMailDev
Python mail client by developpers

[![Updates](https://pyup.io/repos/github/TristanEduProjet/PyMailDev/shield.svg)](https://pyup.io/repos/github/TristanEduProjet/PyMailDev/)
[![Python 3](https://pyup.io/repos/github/TristanEduProjet/PyMailDev/python-3-shield.svg)](https://pyup.io/repos/github/TristanEduProjet/PyMailDev/)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/191dce815d614c259c0bf146d56d0a64/badge.svg)](https://www.quantifiedcode.com/app/project/191dce815d614c259c0bf146d56d0a64)

Unix : [![CircleCI](https://circleci.com/gh/TristanEduProjet/PyMailDev.svg?style=svg)](https://circleci.com/gh/TristanEduProjet/PyMailDev)  
Windows : [![Build status](https://ci.appveyor.com/api/projects/status/e560s9gsv363whkg?svg=true)](https://ci.appveyor.com/project/TristanEduProjet/pymaildev)


## Sujet
> L'objectif du projet est de réaliser une application complète en python, sur une thématique de votre choix :
> réseau (crawler web, par exemple), traitement d'image, création app web avec Django, jeu vidéo, outil de
cryptage, etc...
>
> Pour un maximum de points, le sujet devra comporter :
>   - une partie POO
>   - une interface utilisateur (graphique ou menu console)
>   - utilisation de librairies extérieures (django, beautifulsoup,
opencv, ...)
>
> Le code source devra :
>   - être organisé en packages
>   - être conforme à PEP8
>   - être intégralement en anglais
>   - contenir un README pour l'installation et l’exécution du
> programme
>   - être utilisable sous Windows 10
>
>Le rapport devra :
>   - contenir la répartition des taches dans le groupe (pas de "on a tout fait ensemble")
>   - contenir tout schéma ou diagramme nécessaire à la bonne compréhension du code et de son organisation
>   - expliquer les différentes fonctionnalités du programme, et pour chacune, comment y accéder lors de l'utilisation et ou trouver le code correspondant dans le code source
>   - indiquer les difficultés rencontrées, si il y en à eu, et les solutions apportées
>
> Rendu : Livraison du code source et du rapport.


### Sujet choisi
Un client mail avec une GUI (Qt ou curses).
> Tkinter, PyQt/PySide, WxPython, PyGTK, PyGame


## Dépendances
Dépendances embarquées dans le **setup** (ou *requirements*) :
  - [PyQt5](https://www.riverbankcomputing.com/software/pyqt)
  - ...

Dépendances non embarqués (à installer manuellement) :
  - [Python 3](https://www.python.org/downloads/)
  - [Qt5](https://wiki.qt.io/Main) (section *Quick Access* > Qt 5.x.x)
    => Uniquement si en dev, sinon bianires embarqués ;)


## Usage
```python
#todo
```

## Installation
### Depuis PyPi :
```shell
pip install PyMailDev
```
**>> Ne fonctionne pas pour l'instant.**

### En local (copie du Git) :
```shell
python setup.py install
```

### _Développeurs_
Pour installer les dépendances de devel:
```shell
python install -r requirements.txt
```

Pour vérifier la conformité du code (PEP8 entre autre) :
```shell
python setup.py pylint flake8
```
ou simplement `pep8 ./` mais retourne pas toutes les erreurs.

Pour tester le programme (conformité & tests unitaires): 
```shell
python setup.py test
```

Pour packager le programme :
```shell
python setup.py bdist_wheel
```
