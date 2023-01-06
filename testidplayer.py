import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()
playerEntities = mc.getPlayerEntityIds()
print (playerEntities)
mc.player.setting("autojump", True)
while True:
    time.sleep(3)
    pos=mc.entity.getPos(playerEntities[0])
    mc.postToChat("x="+str(pos.x)+"y="+str(pos.y)+"z="+str(pos.z))