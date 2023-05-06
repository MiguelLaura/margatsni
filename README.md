# Margatsni

Margatsni is Minet, but only for Instagram. It adds some commands to get account-specific data.

## Installation

You need to set up a python environment. Then, in your shell, type:

```bash
git clone git@github.com:MiguelLaura/margatsni.git
cd margatsni
make deps
```

## Usage

Pour récupérer les posts dans Découvrir:

```bash
margatsni account explore limit -c cookie
```
où `limit` est le nombre de posts à récupérer et `cookie` est le cookie d'Instagram à récupérer dans le navigateur (clic droit > Inspecter > Réseau > premier lien où un cookie apparaît > entête de la requête > Cookie à copier)

IGNOREZ LES AIDES ASSOCIÉES AUX COMMANDES DE ACCOUNT DANS LE TERMINAL !!
