# Team Commands
Set team color `/team modify <team_name> color <teamColor>` 

Add players to a team with a command like `/team join <team_name> <player_name>`

Remove players with `/team leave <player_name>` 

List the players in a team `/team list <team_name>` 

Apply luck to all participants for 20 minutes `/minecraft:effect give @a[distance=..1000] luck 1200` 

Apply glow to the hiders for 5 minutes `/minecraft:effect give @a[team=hider] glowing 300` 

Teleport players to you `/minecraft:tp @a[team=hider] ~ ~ ~` `/minecraft:tp @a[team=seeker] ~ ~ ~` 

Clear items `/minecraft:clear @a[team=hider]` `/minecraft:clear @a[team=seeker]`

# CMI
## Make a kit
`/cmi kiteditor new [kitname]`
> Items containing **{USERNAME} {DISPLAYNAME} {KITNAME} {WORLDNAME} {RANDOMPLAYER}** variables in display name or lore will be replaced automatically to appropriate values when player gets kit.


# LuckPerms
## Make Permission Group
`lp creategroup [name]`
## Add/remove user p to permission group x
`lp user [player] parent add/remove [permissionGroup]
# WorldGuard
## Make a new region
Select a region with worldedit then do `/region define [regionName]`
## Add permissiongroup to region
`/rg addmember -w [regionName] g:[groupName] [optionalAdditionalPlayers]`
## Deny/allow region exit for members
`/region flag [regionName] exit -g members deny/allow`
## Deny/Allow TNT explosions in region
`/region flag [regionName] other-explosion deny/allow`
