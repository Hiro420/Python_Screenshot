from PIL import Image

layer2 = Image.open(".\\images\\output-onlinepngtools.png")
layer1 = Image.open(".\\images\\pictures\\screen.png")

final1 = Image.new("RGBA", layer1.size)
final1.paste(layer1, (0,0), layer1)
final1.paste(layer2, (0,0), layer2)
final1.save("CockPS_Screenshot.png")