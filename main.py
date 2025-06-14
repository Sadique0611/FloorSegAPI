from fastapi import FastAPI, UploadFile, File
from dxf_parser.parse_dxf import dxf_to_image
from segmentation.segmentor import segment_image
from utils.ocr import extract_text_labels

import shutil
import os
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from dxf_parser.parse_dxf import dxf_to_image
from segmentation.segmentor import segment_image
from utils.ocr import extract_text_labels
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

@app.post("/segment/")
async def segment(file: UploadFile = File(...)):
    os.makedirs("temp", exist_ok=True)
    input_path = f"temp/{file.filename}"
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    image_path = dxf_to_image(input_path)
    segmented_output = segment_image(image_path)
    room_texts = extract_text_labels(image_path)
    os.remove(input_path)
    return {
        "segmented_rooms": segmented_output,
        "detected_labels": room_texts
    }
