# Floorplan Segmentation API

This project parses DWG/DXF architectural floorplans and uses deep learning to segment rooms and identify labels.

## Features
- Convert .dxf to .png
- Segment rooms with pretrained model
- Extract room names using OCR
- FastAPI-based REST API

## Usage
1. Run `uvicorn main:app --reload`
2. Visit `http://localhost:8000/docs`
3. Upload a `.dxf` floorplan to `/segment/`

## Folder Structure
```
floorplan-segmentation-api/
├── main.py
├── model/
│   └── unet_model.pth
├── dxf_parser/
│   └── parse_dxf.py
├── segmentation/
│   └── segmentor.py
├── utils/
│   └── ocr.py
├── test_data/
│   ├── example.dxf
│   └── example.png
├── requirements.txt
└── README.md
```
