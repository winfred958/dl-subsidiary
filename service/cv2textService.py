import cv2
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

from entity.cv2nlp.CV2NLPEntity import CV2NLPEntity


class CV2NLPService:

    def __init__(self):
        # 通用文本识别
        self.recognition_general = pipeline(Tasks.ocr_recognition,
                                            model='damo/cv_convnextTiny_ocr-recognition-general_damo')

        # 手写文本
        self.recognition_handwritten = pipeline(Tasks.ocr_recognition,
                                                model='damo/cv_convnextTiny_ocr-recognition-handwritten_damo')

        # 读光-文字识别-CRNN模型-中英-通用领域
        self.crnn_ocr_recognition_general = pipeline(Tasks.ocr_recognition,
                                                     model='damo/cv_crnn_ocr-recognition-general_damo')

        # 印刷体 (识别验证码一绝)
        self.recognition_document = pipeline(Tasks.ocr_recognition,
                                             model='damo/cv_convnextTiny_ocr-recognition-document_damo')

    def image2Text(self, imagePath: str):
        list = []
        imread = cv2.imread(imagePath)
        generalResult: dict = self.recognition_general(imread)
        handWrittenResult: dict = self.recognition_handwritten(imread)
        crnnResult: dict = self.crnn_ocr_recognition_general(imread)
        documentResult: dict = self.recognition_document(imread)

        # FIXME: 多线程并行处理
        list.append(CV2NLPEntity(key="general", value=self.arr2str(generalResult), description="通用文本识别"))
        list.append(CV2NLPEntity(key="handWritten", value=self.arr2str(handWrittenResult), description="手写文本识别"))
        list.append(CV2NLPEntity(key="cnn", value=self.arr2str(crnnResult), description="cnn文本识别"))
        list.append(CV2NLPEntity(key="document", value=self.arr2str(documentResult), description="印刷体文本识别"))

        return list

    def arr2str(self, textDict):
        list = textDict.get("text")
        return "".join(list)
