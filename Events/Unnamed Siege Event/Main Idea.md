# Unnamed Siege Event

A combination of bedwars, capture the flag, and TNT wars.


## Player Roles
Players pick a kit (role) before joining the game. Some players may recieve a "Special Kit" randomly. The kits are as follows:
### Fighters
Fighters fight. They have the best armor and weapons out of all roles and must defend their base and attack the enemies.
#### Items
1. Diamond Sword (Special: Netherite Sword)
	1. `/give @p diamond_sword{display:{Name:'[{"text":"Fighter\'s Sword","italic":false}]',Lore:['[{"text":"Thou shall not use outside of event.","italic":false}]']},CanDestroy:[blue_wall_banner,red_wall_banner]} 1`
2. Diamond Armor
3. Colored Shield
	1. Blue: `/give @p minecraft:shield{BlockEntityTag:{Base:11,Patterns:[{Color:8,Pattern:"bo"}]}, display:{Name:'[{"text":"Fighter\'s Shield","italic":false}]',Lore:['[{"text":"Strong and sturdy.","italic":false}]']}} 1`
	2. Red: `/give @p minecraft:shield{BlockEntityTag:{Base:14,Patterns:[{Color:8,Pattern:"bo"}]}, display:{Name:'[{"text":"Fighter\'s Shield","italic":false}]',Lore:['[{"text":"Strong and sturdy.","italic":false}]']}} 1`
4. 64 Steak
5. 16 Ender Pearls
6. 1 Strength 2 Potion
7. 1 Swiftness 2 Potion
8. Special: 10 Golden Apples

### Archers
Archers go pew pew. They are supporting the fighters by being spotters and snipers. They have ok armor and weapons, but rather retreat when confronted.
#### Items
1. Bow (Special: Power 5, Punch 2)
	1. `/give @p minecraft:bow{display:{Name:'[{"text":"Archer\'s Bow","italic":false}]',Lore:['[{"text":"Pew pew.","italic":false}]']},CanDestroy:["minecraft:blue_wall_banner","minecraft:red_wall_banner"]} 1`
2. 32 Arrows (Special: Instant Damage Tipped Arrows)
3. 32 Spectral Arrows
5. Iron Pickaxe (Pressure plates only)
6. Iron Armor
7. 64 Steak
8. 16 Ender Pearls
9. 1 Swiftness 3 Potion
10. 1 Jump Boost (for 2 block jump) Potion

### Engineers
Engineers fortify the home base and breach the enemy base. They have minimal armor, and only has a knockback stick. Unlike others, they can build and destroy freely. Retreating is a must when encountring an enemy.
#### Items
1. Knockback 1 Stick
2. Iron Pickaxe (Special: Diamond Pickaxe)
3. Iron Shovel (Special: Diamond Shovel)
4. Colored Leather armor
5. Shears
6. Redstone Toolbox (Redstone, Repeaters, Comparators, Prefilled Dispensers, Buttons, Levers, Pressure Plates, TNT Minecarts (Yes, Landmines.) and maybe even some skulk sensors when server is 1.19 updated?)
7. Special: Crossbow (Multishot, Unbreaking 3)
8. Special: 32 Fireworks (4 stars, Flight Duration 3)

## Role System Goals
The goal with this system is that a team cannot rush the enemy by only choosing fighters, as (in 1.19 especially) landmines can shoot them up into the sky and deal heavy damage. To counter this, a part of their team will need to be archers, so that they can either: Intentionally detonate the landmine by shooting arrows at the pressure plate or making enough noise to trigger the skulk sensor. However, Fighters and Archers cannot beat the game on its own. They would need the engineers to break through the walls of the fort and let everyone in. You can't have engineers rush the fort because they have bad armor and can easily be killed by either Landmines, TNT cannons, or good ol' fireworks.

To keep the game interesting, a random player will be given special versions of their chosen kits. These are meant to give a little more life (and maybe some scuff) to the battlefield.


## Player Teams
A team must be roughly equal in size, adjusting accordingly. (E.g., If there is a PvP warlord in 1 team, that team gets less players).

## Arena
For now, I'll be picking a random spot on the res server. I'll make a proper map soon :tm:.
The flag will be placed in a place where there are natural bottlenecks. (E.g A Peninsula, a long island, etc) Every location must be Staff/Event Team approved so that players don't go in caves looking for it. It must clearly be in a man-made structure, and a player must be able to walk (not crawl) to the flag without difficulties.

Players are given 15-30 minutes to prepare all defenses. The defences may include landmines, walls, chokepoints, TNT cannons, lava walls. There will be a reasonable limit to the placing limits. During this time, all players can help build.
## Game Rules
1. No items must go out, or in. All players are expected to stash their belongings in a chest before joining.
2. Players cannot drop items. (Command block based method is nice, but I'd rather make a dedicated plugin for all my events. Not sure why, but it seems easier.)
3. Unlimited respawns until all flags are down, spawn on the home fort.


## Technical Stuff
Plugin used: PvP Arena, CMI, WorldGuard, LuckPerms
	Mode: PhysicalFlag
## Procedures
1. Scout/paste suitable arena
2. Define regions and permissions
	1. Make regions
		1. `/region define arena`
		2. `/region define blueBase`
		3. `/region define redBase`
	2. Configure regions
		1. `/region define arena SpaceNerden`
		2. `/region define blueBase SpaceNerden`
		3. `/region define redBase SpaceNerden`
		4. `/region flag arena exit -g members deny`
		5.  `/region flag arena exit-via-teleport -g members deny`
		6. `/region flag arena entry -g members deny`
		7. `/region flag arena other-explosion deny`
		8. `/region flag blueBase exit -g members deny`
		9. `/region flag redBase exit -g members deny`
3. Configure PvP Arena 
	1. Create arena and configure goals
		1. `/pa create siegeArena`
		2. `/pa siegeArena goal TeamLives`
		3. `/pa siegeArena goal PhysicalFlags`
		4. `/pa reload`
		5. `/pa siegeArena set flagType WHITE_BANNER`
		6. `/pa siegeArena set effect GLOWING`
	2. Set spawn points
		1. `/pa siegeArena spawn blueSpawn`
		2. `/pa siegeArena spawn redSpawn`
		3. `/pa siegeArena spawn spectator`
		4. `/pa siegeArena spawn exit`
4. Make kits
	1. `/cmi kiteditor new [kitname]`
5. Send announcement
6. Make teams for easy crowd control
	1. `/team add redteam`
	2. `/team add blueTeam`
7. Add players to WG regions
	1. `/region addmember -w arena [players]
	2. `/region addmember -w redBase [players]
	3. `/region addmember -w blueBase [players]
8. Register players to arena, add to team, and give kits
	1. `/pa siegeArena playerjoin [player] [team]`
	2. `/cmi kit [kitName] [player] 
	3. `/team join [teamName] [player]`
9. Start event
	1. `/pa siegeArena start`
10. After ~10 minutes, add fighters and archers to adventure mode. Release players.
	1. `/gamemode adventure [players]`
	2.  `/region flag blueBase exit -g members allow`
	3. `/region flag redBase exit -g members allow`
11. Cleanup
	1. Clear all inventories
	2. Delete WG regions
		1. `/region remove redBase`
		2. `/region remove blueBase`
		3. `/region remove arena`
	4. Delete PvP Arena arenas
		1. `/pa siegeArena delete`
		2. `/pa siegeArena delete` (Confirmation)
	5. Delete permission groups
		1. `/lp deletegroup redTeam`
		2. `/lp deletegroup blueTeam`
	6. Delete teams
		1. `/team remove redTeam`
		2. `/team remove blueTeam`

## TODO:
- [ ] Revoke `pvparena.user` for players 
- [ ] **Rehearse.**
## Maybe?
- Make custom plugin for ultimate flexibility