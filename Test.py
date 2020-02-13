import improc


path_load = 'data/json/B01_0361_annotations.json'

image = improc.load(path_load)


test = [(100,100,0), (120,143,5), (1000, 300, 200)]

print(image.check(test))
