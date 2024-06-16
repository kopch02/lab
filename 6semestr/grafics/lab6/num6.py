#фото в схему вышивки она максимум 300 на 300
#палитра dmc
#в эвклидовой
from PIL import Image
import numpy as np
from sklearn.neighbors import NearestNeighbors


def verify_pixel(image_path: str) -> None:
    with Image.open(image_path) as img:
        img_data = list(img.getdata())
        for i, color in enumerate(img_data):
            if not all(0 <= c <= 255 for c in color):
                print(
                    f"Pixel at position {divmod(i, img.width)} is out of range"
                )


def mosaic_image(target_path: str, mosaic_size: int, image_path: str) -> None:
    with Image.open(image_path) as img:
        new_img = Image.new('RGB', img.size)
        for x in range(0, img.size[0], mosaic_size):
            for y in range(0, img.size[1], mosaic_size):
                colors = []
                for x1 in range(x, x + mosaic_size):
                    for y1 in range(y, y + mosaic_size):
                        if x1 >= img.size[0] or y1 >= img.size[1]:
                            continue
                        colors.append(img.getpixel((x1, y1)))

                avg_color = tuple(
                    int(sum([c[i] for c in colors]) / len(colors))
                    for i in range(3))

                for x1 in range(x, x + mosaic_size):
                    for y1 in range(y, y + mosaic_size):
                        if x1 >= img.size[0] or y1 >= img.size[1]:
                            continue
                        new_img.putpixel((x1, y1), avg_color)

        new_img.save(target_path)


# Example usage
verify_pixel("lab6.jpg")
mosaic_image("canvas.png", 8, "big_img.jpg")

dmc_palette = [
    [0, 0, 0], [208, 208, 208], [255, 255, 255], [45, 59, 59],
    [52, 74, 75], [147, 145, 141], [155, 153, 138], [167, 169, 173],
    [160, 160, 160], [46, 110, 137], [34, 87, 119], [70, 157, 159],
    [39, 106, 112], [111, 112, 110], [71, 56, 41], [181, 163, 126],
    [182, 180, 162], [103, 78, 60], [61, 52, 47], [141, 108, 67],
    [168, 103, 50], [223, 207, 185], [166, 67, 49], [196, 89, 17],
    [226, 184, 45], [252, 253, 182], [174, 148, 106], [194, 172, 133],
    [222, 193, 146], [80, 91, 99], [112, 88, 74], [223, 137, 61],
    [240, 217, 189], [238, 186, 133], [228, 65, 45], [69, 65, 78],
    [184, 133, 113], [233, 214, 208], [121, 70, 49], [195, 136, 91],
    [255, 244, 221], [147, 112, 87], [225, 183, 163], [165, 40, 65],
    [203, 58, 74], [247, 184, 198], [240, 218, 218], [253, 228, 223],
    [156, 48, 54], [187, 63, 68], [240, 139, 139], [253, 200, 201],
    [125, 77, 73], [189, 154, 145], [211, 183, 177], [252, 225, 206],
    [184, 46, 82], [188, 75, 97], [244, 149, 164], [216, 107, 123],
    [251, 212, 220], [255, 238, 244], [98, 109, 191], [118, 131, 195],
    [154, 167, 212], [186, 200, 227], [211, 220, 239], [68, 109, 182],
    [49, 85, 149], [84, 119, 181], [122, 152, 204], [169, 204, 227],
    [184, 204, 228], [206, 222, 239], [69, 95, 116], [116, 132, 150],
    [153, 168, 193], [196, 198, 204], [54, 69, 79], [89, 75, 79],
]


with Image.open("canvas.png") as img:
    dmc_palette = np.array(dmc_palette)
    nbrs = NearestNeighbors(n_neighbors=1, algorithm='kd_tree').fit(
        dmc_palette)  #ближайшие соседи

    img_array = np.array(img)
    h, w, _ = img_array.shape
    img_array = img_array.reshape(h * w, 3)  #вытянул в одну строчку
    dist, indices = nbrs.kneighbors(
        X=img_array)  #нашёл по 1 мближайшему соседу

    img_array = dmc_palette[indices].reshape(h, w, 3)  #записал новые цвета
    Image.fromarray(np.uint8(img_array)).save('new_image.png')
