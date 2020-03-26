import image, machine,gc

img_1 = image.Image('/1.bmp')
img_2 = image.Image('/2.bmp')
b_and = img_1.b_and(img_2).save('/b_and.bmp')
b_and_inv = b_and.invert().save('/b_and_inv.bmp')
del img_1,img_2,b_and,b_and_inv
gc.collect()

img_1 = image.Image('/1.bmp')
img_2 = image.Image('/2.bmp')
b_inv_1 = img_1.invert().save('/b_inv_1.bmp')
b_inv_2 = img_2.invert().save('/b_inv_2.bmp')
del img_1,img_2,b_inv_1,b_inv_2
gc.collect()

# b_and_inv_1 is equal with b_nand_21
img_1 = image.Image('/1.bmp')
img_2 = image.Image('/2.bmp')
b_and_inv_1 = img_1.invert().b_and(img_2).save('/b_and_inv_1.bmp')
del img_1,img_2,b_and_inv_1
gc.collect()

img_1 = image.Image('/1.bmp')
img_2 = image.Image('/2.bmp')
b_nand_21= img_2.b_nand(img_1).save('/b_nand_21.bmp')
del img_1,img_2,b_nand_21
gc.collect()

# b_and_inv_2 is equal with b_nand_12
img_1 = image.Image('/1.bmp')
img_2 = image.Image('/2.bmp')
b_and_inv_2 = img_1.b_and(img_2.invert()).save('/b_and_inv_2.bmp')
del img_1,img_2,b_and_inv_2
gc.collect()

img_1 = image.Image('/1.bmp')
img_2 = image.Image('/2.bmp')
b_nand_12= img_1.b_nand(img_2).save('/b_nand_12.bmp')
del img_1,img_2,b_nand_12
gc.collect()

img_1 = image.Image('/1.bmp')
img_2 = image.Image('/2.bmp')
b_or  = img_1.b_or(img_2).save('/b_or.bmp')
b_or_inv = b_or.invert().save('/b_or_inv.bmp')
del img_1,img_2,b_or,b_or_inv
gc.collect()

img_1 = image.Image('/1.bmp')
img_2 = image.Image('/2.bmp')
b_nor_12 = img_1.b_nor(img_2).save('/b_nor_12.bmp')
del img_1,img_2,b_nor_12
gc.collect()

img_1 = image.Image('/1.bmp')
img_2 = image.Image('/2.bmp')
b_nor_21 = img_1.b_nor(img_2).save('/b_nor_21.bmp')
del img_1,img_2,b_nor_21
gc.collect()

img_1 = image.Image('/1.bmp')
img_2 = image.Image('/2.bmp')
b_xor = img_1.b_xor(img_2).save('/b_xor.bmp')
del img_1,img_2,b_xor
gc.collect()

img_1 = image.Image('/1.bmp')
img_2 = image.Image('/2.bmp')
b_xnor= img_1.b_xnor(img_2).save('b_xnor.bmp')
del img_1,img_2,b_xnor
gc.collect()

machine.reset()
