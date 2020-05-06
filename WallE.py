from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
from numpy import *


def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
#--------------------------------
#Backgroun Circle
    glBegin(GL_POLYGON)
    r = 0.55
    glColor3f(0.9843137255, 0.831372549, 0.5764705882)
    for theta in arange(0, 2 * pi, 0.01):
        x1 = r * cos(theta) -0.009
        y1 = r * sin(theta) -0.13
        glVertex2d(x1, y1)
    glEnd()
#---------------------------------------
    #Red Greeting
    glColor3f(0.929412, 0.109804, 0.141176)
    glBegin(GL_POLYGON)
    glVertex2d(-0.463688, 0.476562)
    glVertex2d(-0.472922, 0.470703)
    glVertex2d(-0.493234, 0.544922)
    glVertex2d(-0.479688, 0.550781)
    glEnd()
    glColor3f(0.929412, 0.109804, 0.141176)
    glBegin(GL_POLYGON)
    glVertex2d(-0.490109, 0.458984)
    glVertex2d(-0.505734, 0.439453)
    glVertex2d(-0.583859, 0.527344)
    glVertex2d(-0.557297, 0.548828)
    glEnd()
    glColor3f(0.929412, 0.109804, 0.141176)
    glBegin(GL_POLYGON)
    glVertex2d(-0.515109, 0.417969)
    glVertex2d(-0.519797, 0.400391)
    glVertex2d(-0.579172, 0.433594)
    glVertex2d(-0.572922, 0.449219)
    glEnd()
#----------------------------------------
#LEFT LEG
    glColor3f(0.1490196078,0.1098039216,0.08235294118)
    glBegin(GL_POLYGON)
    glVertex2d(-0.4140625, -0.2246093)
    glVertex2d(-0.2843750, -0.2265625)
    glVertex2d(-0.3921875, -0.7128906)
    glVertex2d(-0.5437500, -0.6484375)
    glEnd()
    glColor3f(0.09411764706,0.07058823529,0.05098039216)
    glBegin(GL_POLYGON)
    glVertex2d(-0.284375, -0.226562500)
    glVertex2d(-0.392187, -0.712890625)
    glVertex2d(-0.203125, -0.591796875)
    glEnd()
#-----------------------------------
#LEFT HAND
    #BASIC BONE
    glColor3f(0.8, 0.784314, 0.788235)
    glBegin(GL_POLYGON)
    glVertex2d(-0.4, 0.357422)
    glVertex2d(-0.423438, 0.304688)
    glVertex2d(-0.384375, 0.253906)
    glVertex2d(-0.348437, 0.261719)
    glEnd()
    glColor3f(0.67451, 0.658824, 0.662745)
    glBegin(GL_POLYGON)
    glVertex2d(-0.362, 0.289109)
    glVertex2d(-0.348437, 0.261719)
    glVertex2d(-0.384375, 0.253906)
    glVertex2d(-0.398438, 0.273438)
    glEnd()
    #LEFT FINGER
    glColor3f(0.8, 0.784314, 0.788235)
    glBegin(GL_POLYGON)
    glVertex2d(-0.351562, 0.388672)
    glVertex2d(-0.382812, 0.314453)
    glVertex2d(-0.41, 0.326172)
    glVertex2d(-0.3829, 0.408203)
    glEnd()
    glColor3f(0.67451, 0.658824, 0.662745)
    glBegin(GL_POLYGON)
    glVertex2d(-0.351562, 0.388672)
    glVertex2d(-0.359375, 0.373047)
    glVertex2d(-0.388, 0.388672)
    glVertex2d(-0.3829, 0.408203)
    glEnd()
    #RIGHT FINGER
    glColor3f(0.8, 0.784314, 0.788235)
    glBegin(GL_POLYGON)
    glVertex2d(-0.429688, 0.443359)
    glVertex2d(-0.401563, 0.394531)
    glVertex2d(-0.426562, 0.373047)
    glVertex2d(-0.45625, 0.417969)
    glEnd()
    glColor3f(0.67451, 0.658824, 0.662745)
    glBegin(GL_POLYGON)
    glVertex2d(-0.401563, 0.394531)
    glVertex2d(-0.426562, 0.373047)
    glVertex2d(-0.396875, 0.326172)
    glVertex2d(-0.376563, 0.349609)
    glEnd()
    #MID FINGER
    glColor3f(0.67451, 0.658824, 0.662745)
    glBegin(GL_POLYGON)
    glVertex2d(-.432813, 0.367188)
    glVertex2d(-0.396875, 0.322266)
    glVertex2d(-0.420, 0.289062)
    glVertex2d(-0.457812, 0.339844)
    glEnd()
    glColor3f(0.8, 0.784314, 0.788235)
    glBegin(GL_POLYGON)
    glVertex2d(-0.464063, 0.40625)
    glVertex2d(-0.432813, 0.367188)
    glVertex2d(-0.457812, 0.339844)
    glVertex2d(-0.489062, 0.382812)
    glEnd()
    #ARM
    glColor3f(0.7568627450980392,0.4980392156862745,0.2196078431372549)
    glBegin(GL_POLYGON)
    glVertex2d(-0.3375, 0.28418)
    glVertex2d(-0.248437, 0.0400391)
    glVertex2d(-0.284375, 0.00878906)
    glVertex2d(-0.371875, 0.24707)
    glEnd()
    glColor3f(0.8666666666666667,0.592156862745098,0.2470588235294118)
    glBegin(GL_POLYGON)
    glVertex2d(-0.371875, 0.24707)
    glVertex2d(-0.284375, 0.00878906)
    glVertex2d(-0.321875, 0.00292969)
    glVertex2d(-0.414062, 0.25)
    glEnd()
    glColor3f(0.9529411764705882,0.6313725490196078,0.2784313725490196)
    glBegin(GL_POLYGON)
    glVertex2d(-0.3375, 0.28418)
    glVertex2d(-0.371875, 0.24707)
    glVertex2d(-0.414062, 0.25)
    glEnd()
#--------------------------------------------------
#BODY
    #SIDE SIDE
    glColor3f(0.7568627451, 0.4980392157, 0.2196078431)
    glBegin(GL_POLYGON)
    glVertex2d(0, 0)
    glVertex2d(0, -0.689453125)
    glVertex2d(0.34375, -0.505859375)
    glVertex2d(0.34375, 0.083984375)
    glEnd()
    #ELEVATION VIEW
    glColor3f(0.866667, 0.592156862745098, 0.2470588235294118)
    glBegin(GL_POLYGON)
    glVertex2d(0, 0)
    glVertex2d(0, -0.689453125)
    glVertex2d(-0.35, -0.603515625)
    glVertex2d(-0.35, 0.083984375)
    glEnd()
    #TOP VIEW
    glColor3f(0.9568627451, 0.631372549, 0.2784313725)
    glBegin(GL_POLYGON)
    glVertex2d(0, 0)
    glVertex2d(-0.35, 0.083984375)
    glVertex2d(0, 0.185546875)
    glVertex2d(0.34375, 0.083984375)
    glEnd()
#------------------------------------------
#RIGHT ARM
    #SIDE VIEW
    glColor3f(0.866667, 0.592156862745098, 0.2470588235294118)
    glBegin(GL_POLYGON)
    glVertex2d(0.2125,-0.157227)
    glVertex2d(-0.053125,-0.245117)
    glVertex2d(-0.06875,-0.297852)
    glVertex2d(0.2125,-0.188477)
    glEnd()
    #ELEVATION VIEW
    glColor3f(0.9882352941176471, 0.6666666666666667, 0.3490196078431373)
    glBegin(GL_POLYGON)
    glVertex2d(-0.078125, -0.1962889)
    glVertex2d(-0.06875, -0.297852)
    glVertex2d(-0.053125, -0.245117)
    glEnd()
    #TOP VIEW
    glColor3f(0.8,0.5215686274509804,0.2431372549019608)
    glBegin(GL_POLYGON)
    glVertex2d(0.2125,-0.131836)
    glVertex2d(-0.078125,-0.196289)
    glVertex2d(-0.053125,-0.245117)
    glVertex2d(0.2125,-0.157227)
    glEnd()
#-------------------------------------------
#RIGHT HAND
    #BASIC HAND BONE
    glColor3f(0.2980392156862745,0.2470588235294118,0.1882352941176471)
    glBegin(GL_POLYGON)
    glVertex2d(0.2125,-0.131836)
    glVertex2d(0.167187,-0.141602)
    glVertex2d(0.173438,-0.170898)
    glVertex2d(0.212500,-0.157227)
    glEnd()
    # BASIC HAND BONE 2
    glColor3f(0.4392156862745098,0.3647058823529412,0.2745098039215686)
    glBegin(GL_POLYGON)
    glVertex2d(0.212500,-0.157227)
    glVertex2d(0.212500,-0.188477)
    glVertex2d(0.178125,-0.202148)
    glVertex2d(0.173438,-0.170898)
    glEnd()
    #BOTTOM FINGER
    glColor3f(0.576471, 0.576471, 0.576471)
    glBegin(GL_POLYGON)
    glVertex2d(-0.103125, -0.279297)
    glVertex2d(-0.117188, -0.300781)
    glVertex2d(-0.134375, -0.289062)
    glVertex2d(-0.121875, -0.273438)
    glEnd()
    glColor3f(0.792157, 0.780392, 0.788235)
    glBegin(GL_POLYGON)
    glVertex2d(-0.134375, -0.289062)
    glVertex2d(-0.117188, -0.300781)
    glVertex2d(-0.134375, -0.326172)
    glVertex2d(-0.154687, -0.314453)
    glEnd()
    #BASIC BONE
    glColor3f(0.8,0.7843137254901961,0.7882352941176471)
    glBegin(GL_POLYGON)
    glVertex2d(-0.0640625,-.2333980)
    glVertex2d(-0.0625000,-0.262695)
    glVertex2d(-0.1156250,-0.280273)
    glVertex2d(-0.1328120,-0.241211)
    glEnd()
    glColor3f(0.6745098039215686,0.6588235294117647,0.6627450980392157)
    glBegin(GL_POLYGON)
    glVertex2d(-0.0640625,-.2333980)
    glVertex2d(-0.0625000,-0.262695)
    glVertex2d(-0.0828125,-0.270508)
    glVertex2d(-0.0921875,-0.236328)
    glEnd()
    #UPPER FINGER
    glColor3f(0.67451, 0.658824, 0.662745)
    glBegin(GL_POLYGON)
    glVertex2d(-0.0859375, -0.227539)
    glVertex2d(-0.101562, -0.248047)
    glVertex2d(-0.176563, -0.250977)
    glVertex2d(-0.189063, -0.220703)
    glEnd()
    glColor3f(0.792157, 0.780392, 0.788235)
    glBegin(GL_POLYGON)
    glVertex2d(-0.189063, -0.220703)
    glVertex2d(-0.176563, -0.250977)
    glVertex2d(-0.204688, -0.276367)
    glVertex2d(-0.220313, -0.25293)
    glEnd()
    #MID FINGER
    glColor3f(0.67451, 0.658824, 0.662745)
    glBegin(GL_POLYGON)
    glVertex2d(-0.0859375, -0.264648)
    glVertex2d(-0.0984375, -0.282227)
    glVertex2d(-0.157813, -0.292969)
    glVertex2d(-0.171875, -0.265625)
    glEnd()
    glColor3f(0.792157, 0.776471, 0.780392)
    glBegin(GL_POLYGON)
    glVertex2d(-0.171875, -0.265625)
    glVertex2d(-0.157813, -0.292969)
    glVertex2d(-0.179688, -0.335938)
    glVertex2d(-0.19375, -0.316406)
    glEnd()
#-------------------------------------------
#RIGHT LEG
    glColor3f(0.1490196078, 0.1098039216, 0.08235294118)
    glBegin(GL_POLYGON)
    glVertex2d(0.190625, -0.357421875)
    glVertex2d(0.321875, -0.376953125)
    glVertex2d(0.1828125, -0.84375)
    glVertex2d(0.0359375, -0.767578125)
    glEnd()
    glColor3f(0.09411764706,0.07058823529,0.05098039216)
    glBegin(GL_POLYGON)
    glVertex2d(0.3218750, -0.376953125)
    glVertex2d(0.3671875, -0.74609375)
    glVertex2d(0.1828125, -0.84375)
    glEnd()
#-------------------------------------------
#LEFT EYE
    #EYE SHAPE
    glColor3f(0.4392156863,0.3647058824,0.2745098039)
    glBegin(GL_POLYGON)
    glVertex2d(-0.05781250, 0.298828125)
    glVertex2d(-0.20156250, 0.238281250)
    glVertex2d(-0.26718750, 0.373046875)
    glVertex2d(-0.05156250, 0.486328125)
    glEnd()
    #EYE CIRCLE
    glBegin(GL_POLYGON)
    r = 0.05625
    glColor3f(1,1,1)
    for theta in arange(0, 2 * pi, 0.01):
        x1 = r * cos(theta) - 0.147578125
        y1 = r * sin(theta) + 0.347656250
        glVertex2d(x1, y1)
    glEnd()
    #PUPIL CIRCLE
    glBegin(GL_POLYGON)
    r = 0.03984375
    glColor3f(0, 0, 0)
    for theta in arange(0, 2 * pi, 0.01):
        x1 = r * cos(theta) - 0.147578125
        y1 = r * sin(theta) + 0.347656250
        glVertex2d(x1, y1)
    glEnd()
    #SMALLER WHITE CIRCLE
    glBegin(GL_POLYGON)
    r = 0.01953125
    glColor3f(1,1,1)
    for theta in arange(0, 2 * pi, 0.01):
        x1 = r * cos(theta) - 0.16640625
        y1 = r * sin(theta) + 0.365234375
        glVertex2d(x1, y1)
    glEnd()
#--------------------------------------------
#RIGHT EYE
    #EYE SHAPE
    glColor3f(0.4392156863,0.3647058824,0.2745098039)
    glBegin(GL_POLYGON)
    glVertex2d(0.06406250, 0.26171875)
    glVertex2d(-0.0406250, 0.30859375)
    glVertex2d(-0.0296875, 0.482421875)
    glVertex2d(+0.1703125, 0.376953125)
    glEnd()
    #EYE CIRCLE
    glBegin(GL_POLYGON)
    r = 0.05625
    glColor3f(1,1,1)
    for theta in arange(0, 2 * pi, 0.01):
        x1 = r * cos(theta) + 0.0375
        y1 = r * sin(theta) + 0.359375
        glVertex2d(x1, y1)
    glEnd()
    #EYE PUPIL
    glBegin(GL_POLYGON)
    r = 0.03984375
    glColor3f(0, 0, 0)
    for theta in arange(0, 2 * pi, 0.01):
        x1 = r * cos(theta) + 0.0375
        y1 = r * sin(theta) + 0.359375
        glVertex2d(x1, y1)
    glEnd()
    #SMALLER WHITE CIRCLE
    glBegin(GL_POLYGON)
    r = 0.01953125
    glColor3f(1,1,1)
    for theta in arange(0, 2 * pi, 0.01):
        x1 = r * cos(theta) + 0.01484
        y1 = r * sin(theta) + 0.37890625
        glVertex2d(x1, y1)
    glEnd()
# -------------------------------------------
# Add-On
    #BLACK SQUARE
    glColor3f(0.129412, 0.129412, 0.129412)
    glBegin(GL_POLYGON)
    glVertex2d(-0.29, 0.00390625)
    glVertex2d(-0.29, -0.0332031)
    glVertex2d(-0.3529, -0.0175781)
    glVertex2d(-0.3529, 0.0195312)
    glEnd()
    #BLACK SQUARE 2
    glColor3f(0.129412, 0.129412, 0.129412)
    glBegin(GL_POLYGON)
    glVertex2d(-0.0197969, -0.625469)
    glVertex2d(-0.0197969, -0.662578)
    glVertex2d(-0.0525937, -0.654766)
    glVertex2d(-0.0510469, -0.619609)
    glEnd()
    #WHITE SQUARE
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2d(-0.284469, -0.508047)
    glVertex2d(-0.284469, -0.592031)
    glVertex2d(-0.332906, -0.582266)
    glVertex2d(-0.332906, -0.498281)
    glEnd()
    #SMALLER WHITE SQUARE
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2d(-0.279781, -0.554922)
    glVertex2d(-0.248531, -0.560781)
    glVertex2d(-0.248531, -0.597891)
    glVertex2d(-0.279781, -0.592031)
    glEnd()
#----------------------------------
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Wall-E Project")
glutInitWindowSize(1024 , 1024)
glutDisplayFunc(draw)
glutMainLoop()
