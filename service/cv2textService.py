import cv2
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

from entity.cv2nlp.CV2NLPEntity import CV2NLPEntity


class CV2NLPService:
    # 读光-文字识别-行识别模型-中英-通用领域
    ocr_recognition_general = pipeline(Tasks.ocr_recognition,
                                       model='damo/cv_convnextTiny_ocr-recognition-general_damo')

    # 读光-文字识别-行识别模型-中英-自然场景文本领域
    ocr_recognition_scene = pipeline(Tasks.ocr_recognition,
                                     model='damo/cv_convnextTiny_ocr-recognition-scene_damo')

    # 读光-文字识别-行识别模型-中英-手写文本领域

    ocr_recognition_handwritten = pipeline(Tasks.ocr_recognition,
                                           model='damo/cv_convnextTiny_ocr-recognition-handwritten_damo')

    # 读光-文字识别-CRNN模型-中英-通用领域
    ocr_crnn_recognition_general = pipeline(Tasks.ocr_recognition,
                                            model='damo/cv_crnn_ocr-recognition-general_damo')

    # 读光-文字识别-行识别模型-中英-文档印刷体文本领域 (识别某些验证码一绝)
    ocr_recognition_document = pipeline(Tasks.ocr_recognition,
                                        model='damo/cv_convnextTiny_ocr-recognition-document_damo')

    def __init__(self):
        pass

    def image2Text(self, imagePath: str):
        list = []
        imread = cv2.imread(imagePath)
        generalResult: dict = self.ocr_recognition_general(imread)
        recognition_scene: dict = self.ocr_recognition_scene(imread)
        handWrittenResult: dict = self.ocr_recognition_handwritten(imread)
        crnnResult: dict = self.ocr_crnn_recognition_general(imread)
        documentResult: dict = self.ocr_recognition_document(imread)

        # FIXME: 多线程并行处理
        list.append(CV2NLPEntity(key="general", value=self.arr2str(generalResult),
                                 description="读光-文字识别-行识别模型-中英-通用领域"))
        list.append(CV2NLPEntity(key="scene", value=self.arr2str(recognition_scene),
                                 description="读光-文字识别-行识别模型-中英-自然场景文本领域"))
        list.append(CV2NLPEntity(key="handWritten", value=self.arr2str(handWrittenResult),
                                 description="读光-文字识别-行识别模型-中英-手写文本领域"))
        list.append(
            CV2NLPEntity(key="crnn", value=self.arr2str(crnnResult), description="读光-文字识别-CRNN模型-中英-通用领域"))
        list.append(CV2NLPEntity(key="document", value=self.arr2str(documentResult),
                                 description="读光-文字识别-行识别模型-中英-文档印刷体文本领域"))

        return list

    def arr2str(self, textDict):
        list = textDict.get("text")
        return "".join(list)
