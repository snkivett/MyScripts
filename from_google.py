from flask import Flask, jsonify
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = Flask(__name__)

@app.route('/')
def index():
    credentials = service_account.Credentials.from_service_account_file(
        'service-account-file.json',
        scopes=["https://www.googleapis.com/auth/presentations.readonly"]
    )
    service = build('slides', 'v1', credentials=credentials)

    presentation_id = '1r3fKM74E17GbxNwom_Fb0QmbxhidwBPespOkUk_yUrA'
    presentation = service.presentations().get(presentationId=presentation_id).execute()
    slides = presentation.get('slides')

    slides_info = [{'slide_number': i + 1, 'elements': len(slide.get('pageElements', []))} for i, slide in enumerate(slides)]

    return jsonify(slides_info)

if __name__ == '__main__':
    app.run(debug=True)
