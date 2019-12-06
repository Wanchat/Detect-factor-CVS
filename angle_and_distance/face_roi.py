import dlib

class Extract_eyes:
    
    def __init__(self):

        # Dlib Function Call Model
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(
            r'../res/shape_predictor_68_face_landmarks.dat')

    def inde(self,shape, x1, y1):
        return shape.part(x1).x, shape.part(y1).y

    def inde2(self,shape, idx1, idx2, axe): # << finds center point eye
        if axe == 0:
            point = abs(shape.part(idx1).x + int((shape.part(idx2).x - shape.part(idx1).x) / 2))
        else:
            point = abs(shape.part(idx1).y + int((shape.part(idx2).y - shape.part(idx1).y) / 2))
        return point

    def find_both(self, p1, p2): # fix point center x or y
        if p1 > p2:
            p = p2 + int(abs(p1 - p2) / 2)
        else:
            p = p1 + int(abs(p1 - p2) / 2)
        return p

    # Extract From Dlib Point
    def extract(self, image_gray):

        self.detect_from_model = self.detector(image_gray, 0)

        for self.rect in self.detect_from_model:
            self.shape = self.predictor(image_gray, self.rect)

            rightX = self.inde2(self.shape, 36, 39, 0)
            rightY = self.inde2(self.shape, 37, 41, 1)
            leftX = self.inde2(self.shape, 42, 45, 0)
            leftY = self.inde2(self.shape, 43, 47, 1)

            centerX = self.find_both(rightX, leftX)
            centerY = self.find_both(rightY, leftY)

            return {
                    "eye_right" : (rightX, rightY),
                    "eye_left"  : (leftX, leftY),
                    "eye_center": (centerX, centerY),
                    "face" : (self.rect.left(), self.rect.top(),
                                self.rect.right(), self.rect.bottom())
                    }