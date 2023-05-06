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

```
Usage: margatsni [-h] [--version] {public,pub,account,help} ...

Optional Arguments:
  --version                  show program's version number and exit
  -h, --help                 show this help message and exit

Actions:
  {public,pub,account,help}  Action to execute
```

### Public

Corresponds to the commands comming from Minet (https://github.com/medialab/minet).

```
Usage: margatsni public [-h] [-c COOKIE] [--rcfile RCFILE] [--silent] {comments,hashtag,post-infos,user-followers,user-following,user-infos,user-posts} ...

# Margatsni Public Command

Gather public data from Instagram.

Optional Arguments:
  -c, --cookie COOKIE           Authenticated cookie to use or browser from which to extract it (supports "firefox", "chrome", "chromium", "opera" and "edge"). Defaults to `firefox`. Can also be
                                configured in a .minetrc file as "instagram.cookie" or read from the MINET_INSTAGRAM_COOKIE env variable.
  --rcfile RCFILE               Custom path to a minet configuration file. More info about this here: https://github.com/medialab/minet/blob/master/docs/cli.md#minetrc
  --silent                      Whether to suppress all the log and progress bars. Can be useful when piping.
  -h, --help                    show this help message and exit

Subcommands:
  {comments,hashtag,post-infos,user-followers,user-following,user-infos,user-posts}
                                Subcommand to use.
```

To know more about a specific subcommand:

```bash
margatsni pub subcommand_name -h
```

### Account

Commands about account-specific data (for example, recommendation data).

To get posts from explore section:

```bash
margatsni account explore limit -c cookie
```
where `limit` is the number of posts to retrieve and `cookie` is the Instagram cookie which needs to be manually retrieved from web browser (getting it with `margatsni` is currently not working). To get it in a french web browser: clic droit > Inspecter > Réseau > premier lien où un cookie apparaît > entête de la requête > Cookie à copier.
