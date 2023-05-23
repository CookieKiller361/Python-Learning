#classes
class minecraft_blocks:
    def __init__ (self,blockid,blockheight,blocklength,texture):
        self.blockid = blockid
        self.blockheight=blockheight
        self.blocklength=blocklength
        self.texture=texture

#classes with blocked variables
class minecraft_blocks_two:
    def __init__ (self,blockid,blockheight,blocklength,texture):
        self.__blockid = blockid
        self.__blockheight=blockheight
        self.__blocklength=blocklength
        self.__texture=texture
    
    def get_blockid(self):
        return self.__blockid

#object
dirt_block=minecraft_blocks(10,64,64,"Grass_Texture")
wooden_block=minecraft_blocks_two(10,64,64,"Grass_Texture")


print(dirt_block.blockid)
print(wooden_block.get_blockid())

