from PIL import Image

image=Image.open('your image.jpg')
new_image=image.resize((300,300))
new_image.save('ur_image.jpg')

