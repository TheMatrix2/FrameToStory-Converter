from flask import Flask, flash, render_template, request, jsonify, redirect
import tempfile
import cv2
from source.frame_maker import frame_maker, save_video
from source.image_to_story import create_story

app = Flask(__name__,
            static_url_path='/static/',)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/frame', methods=['GET', 'POST'])
def frame():
    if request.method == 'POST':
        video_file = request.files['file']
        if video_file.filename == '':
            flash('No file selected. Choose a video and try again.')
            return redirect('/')

        with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as tmp_video:
            path_to_video = tmp_video.name
            save_video(path_to_video, tmp_video)
        random_frame = frame_maker(path_to_video)
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_frame:
            path_to_frame = tmp_frame.name
            cv2.imwrite(path_to_frame, random_frame)
        return render_template('index.html', path_to_video=path_to_video, path_to_frame=path_to_frame)


@app.route('/frame_re', methods=['GET'])
def frame_re():
    if request.method == 'GET':
        path_to_video = request.args.get('path_to_video')
        random_frame = frame_maker(path_to_video)
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_frame:
            random_frame.save(tmp_frame.name)
            path_to_frame = tmp_frame.name
        return render_template('index.html', path_to_video=path_to_video, path_to_frame=path_to_frame)


# @app.route('/story', methods=['GET'])
# def story():
#     if request.method == 'GET':
#         path_to_frame = request.args.get('path_to_frame')


if __name__ == '__main__':
    app.run(debug=True)
