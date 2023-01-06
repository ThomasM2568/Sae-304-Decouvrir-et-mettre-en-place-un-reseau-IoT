import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
playerEntities = mc.getPlayerEntityIds()
print (playerEntities)

mc.postToChat("/gamemode 1")