 
##  🛠 Installation des outils

Installer Python3 (qui est installer sur ubuntu 20.04)
Sous windows , il faut le telecharger sus sa page officiel
```bash
 $ sudo apt-get update && sudo apt-get -y upgrade
 $ python3 -V


 python --version
 Python 3.8.10
```
**Étape 1- installation pip**
```bash
 $ sudo apt-get install -y python3-pip
 $ pip3 -V

     **Output**
 pip 22.0.4 
```



**Étape 2-Installer virtualenv**

```bash
 $ pip3 install virtualenv
 $ virtualenv --version

 **Output**
virtualenv 20.13.3 from /home/sammy/.local/lib/python3.5/site-packages/virtualenv/__init__.py
```

**Étape 3 - Installer Django**



Installation  des autres outils comme:

- PyCharm ou Visual code
- chrome ou Edge ou FireFox

# Installation Django

Creation d'un dossier du Projet

```bash 
 mkdir foru
 cd forum 
```

Alors qu'à l'intérieur du django-appsrépertoire, créez votre environnement virtuel. Appelons-leenv.

```bash
virtualenv env
```
Maintenant, activez l'environnement virtuel avec la commande suivante :
```bash
. env/bin/activate
```
Vous saurez qu'il est activé une fois le préfixe remplacé par(env), qui ressemblera à ce qui suit selon le répertoire dans lequel vous vous trouvez :


Dans l'environnement, installez le package Django à l'aide de pip. L'installation de Django nous permet de créer et d'exécuter des applications Django. Pour en savoir plus sur Django, lisez notre série de tutoriels sur Django Development .
```bash
pip install django
```
Une fois installé, vérifiez votre installation Django en exécutant une vérification de version :
```bash
django-admin --version
```
Ceci, ou quelque chose de similaire, sera la sortie résultante :
```bash
Output
4.0.3

```
# Création d'un projet de test Django

Démarrage du projet
Nous pouvons maintenant générer une application en utilisant ```django-admin,```

Dans le django-appsrépertoire, exécutez la commande suivante :
```bash
django-admin startproject forum
```