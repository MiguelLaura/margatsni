# Margatsni

Margatsni is Minet, but only for Instagram. It adds some commands to get account-specific data. Most of the code comes from, or is strongly inspired by https://github.com/medialab/minet.

## Installation

You need to set up a python environment. Then, in your shell, type:

```bash
git clone git@github.com:MiguelLaura/margatsni.git
cd margatsni
make deps
```

## Usage

```
Usage: margatsni [-h] [--version] {account,public,pub,,help} ...

Optional Arguments:
  --version                  show program's version number and exit
  -h, --help                 show this help message and exit

Actions:
  {account,public,pub,help}  Action to execute
```
### Account

Commands about account-specific data (for example, recommendation data).

!!! WARNING !!! Instagram is able to detect this tool as a bot and block you.

To get posts from explore section:

```bash
margatsni account explore limit
```
where `limit` is the number of posts to retrieve. It will automatically get the authenticated cookie from firefox. To change the browser, use the argument --cookie (or -c) followed by your browser name (it supports "firefox", "chrome", "chromium", "opera" and "edge"), or followed directly by the cookie to use. 

### Public

Corresponds to the commands coming from Minet (https://github.com/medialab/minet).

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
