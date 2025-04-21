from flask import Flask, render_template, request
from werkzeug.utils import secure_filename  # ✅ 안전한 파일명 처리
import os
from font_checker import extract_fonts, find_missing_fonts

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ✅ 업로드 허용 확장자
ALLOWED_EXTENSIONS = {'.pptx', '.hwp'}

@app.route('/')
def index():
    return render_template('index.html', fonts=missing_fonts )

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        ext = os.path.splitext(filename)[1].lower()

        # ✅ 여기서 파일 확장자 검사!
        if ext not in ALLOWED_EXTENSIONS:
            return '지원하지 않는 파일 형식입니다. (.pptx, .hwp만 가능해요)'

        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        used_fonts = extract_fonts(filepath)
        missing_fonts = find_missing_fonts(used_fonts)

        return render_template('index.html', fonts=missing_fonts)

    return '파일이 없습니다!'
