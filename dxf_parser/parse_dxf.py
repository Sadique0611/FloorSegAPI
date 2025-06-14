import ezdxf
import matplotlib.pyplot as plt
import os

def dxf_to_image(dxf_path):
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()

    fig, ax = plt.subplots()
    for entity in msp:
        if entity.dxftype() == 'LINE':
            start, end = entity.dxf.start, entity.dxf.end
            ax.plot([start.x, end.x], [start.y, end.y], color='black')

    plt.axis('equal')
    image_path = dxf_path.replace(".dxf", ".png")
    plt.savefig(image_path)
    plt.close()
    return image_path
