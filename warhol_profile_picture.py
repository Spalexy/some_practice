from PIL import Image


original_image = Image.open("original.jpg")
red_channel, green_channel, blue_channel = original_image.split()

offset_step = 42

coordinates_red_channel_1 = (offset_step * 2,
                             0,
                             original_image.width,
                             original_image.height)
coordinates_red_channel_2 = (offset_step,
                             0,
                             original_image.width - offset_step,
                             original_image.height)
red_channel_1 = red_channel.crop(coordinates_red_channel_1)
red_channel_2 = red_channel.crop(coordinates_red_channel_2)
blended_red_image = Image.blend(red_channel_1, red_channel_2, 0.3)

coordinates_blue_channel_2 = (0,
                              0,
                              original_image.width - offset_step * 2,
                              original_image.height)
coordinates_blue_channel_1 = (offset_step,
                              0,
                              original_image.width - offset_step,
                              original_image.height)
blue_channel_1 = blue_channel.crop(coordinates_blue_channel_1)
blue_channel_2 = blue_channel.crop(coordinates_blue_channel_2)
blended_blue_image = Image.blend(blue_channel_1, blue_channel_2, 0.7)

cropping_coordinates = (offset_step,
                        0,
                        original_image.width - offset_step,
                        original_image.height)
cropped_green_image = green_channel.crop(cropping_coordinates)

warhol_image = Image.merge("RGB", (blended_red_image, cropped_green_image, blended_blue_image))
warhol_image.thumbnail((80, 80))
warhol_image.save('Warhol_image.jpg', format='JPEG')
