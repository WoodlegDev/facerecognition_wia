from deepface import DeepFace
from pathlib import Path

path = Path('test_images')
path_list = []
for p in path.iterdir():
    path_list.append(str(p.absolute()))


def analyze_face(img_path):
    obj = DeepFace.analyze(img_path=img_path, actions=['age', 'gender', 'race', 'emotion'])
    return obj


analyzed_list = []
for img in path_list:
    face = analyze_face(img)
    dic = {img: face}
    analyzed_list.append(dic)


print(analyzed_list)
