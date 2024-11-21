# -*- coding: utf-8 -*-
# Indicamos que el archivo utiliza codificación UTF-8, lo que permite incluir caracteres especiales como tildes o eñes.

# Este archivo fue generado automáticamente al convertir un archivo .ui a código Python con pyuic5.
# Cualquier cambio manual puede ser sobrescrito si se vuelve a ejecutar el comando pyuic5.

# Importamos los módulos necesarios de PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# Definimos una clase para la interfaz gráfica de usuario (GUI)
class Ui_Form(object):
    # Método para configurar la interfaz de usuario
    def setupUi(self, Form):
        # Configuración inicial del formulario principal
        Form.setObjectName("Form")  # Asignamos un nombre interno al formulario
        Form.resize(762, 371)  # Establecemos las dimensiones iniciales del formulario (ancho x alto)

        # Creamos un QLabel para mostrar el título "Sintaxis"
        self.labelSintaxis = QtWidgets.QLabel(Form)  # Añadimos un widget de etiqueta al formulario
        self.labelSintaxis.setGeometry(QtCore.QRect(270, 10, 261, 51))  # Posicionamos y dimensionamos el QLabel (x, y, ancho, alto)
        self.labelSintaxis.setObjectName("labelSintaxis")  # Asignamos un nombre interno al QLabel

        # Creamos un QPushButton para el botón "Árbol sintáctico"
        self.buttonSintactico = QtWidgets.QPushButton(Form)  # Añadimos un botón al formulario
        self.buttonSintactico.setGeometry(QtCore.QRect(50, 230, 151, 31))  # Posicionamos y dimensionamos el botón
        self.buttonSintactico.setObjectName("buttonSintactico")  # Asignamos un nombre interno al botón

        # Creamos otro QLabel para la etiqueta "Ingrese expresión"
        self.labelExpresion = QtWidgets.QLabel(Form)  # Añadimos un QLabel al formulario
        self.labelExpresion.setGeometry(QtCore.QRect(140, 80, 121, 20))  # Posicionamos y dimensionamos la etiqueta
        self.labelExpresion.setObjectName("labelExpresion")  # Asignamos un nombre interno al QLabel

        # Creamos un QTextEdit para que el usuario pueda ingresar texto
        self.textExpresion = QtWidgets.QTextEdit(Form)  # Añadimos un widget de texto al formulario
        self.textExpresion.setGeometry(QtCore.QRect(280, 70, 231, 31))  # Posicionamos y dimensionamos el QTextEdit
        self.textExpresion.setObjectName("textExpresion")  # Asignamos un nombre interno al QTextEdit

        # Creamos un QLabel para la etiqueta "Derivación"
        self.labelDerivacion = QtWidgets.QLabel(Form)  # Añadimos un QLabel al formulario
        self.labelDerivacion.setGeometry(QtCore.QRect(220, 150, 81, 16))  # Posicionamos y dimensionamos la etiqueta
        self.labelDerivacion.setObjectName("labelDerivacion")  # Asignamos un nombre interno al QLabel

        # Creamos un QRadioButton para la opción de derivación "Izquierda"
        self.radioButtonIzq = QtWidgets.QRadioButton(Form)  # Añadimos un botón de opción al formulario
        self.radioButtonIzq.setGeometry(QtCore.QRect(290, 160, 111, 41))  # Posicionamos y dimensionamos el QRadioButton
        self.radioButtonIzq.setObjectName("radioButtonIzq")  # Asignamos un nombre interno al QRadioButton

        # Creamos un QRadioButton para la opción de derivación "Derecha"
        self.radioButtonDer = QtWidgets.QRadioButton(Form)  # Añadimos otro botón de opción al formulario
        self.radioButtonDer.setGeometry(QtCore.QRect(440, 160, 141, 41))  # Posicionamos y dimensionamos el QRadioButton
        self.radioButtonDer.setObjectName("radioButtonDer")  # Asignamos un nombre interno al QRadioButton

        # Creamos un QPushButton para el botón "Árbol abstracto"
        self.buttonSintactico_2 = QtWidgets.QPushButton(Form)  # Añadimos un botón al formulario
        self.buttonSintactico_2.setGeometry(QtCore.QRect(270, 230, 181, 31))  # Posicionamos y dimensionamos el botón
        self.buttonSintactico_2.setObjectName("buttonSintactico_2")  # Asignamos un nombre interno al botón

        # Creamos un QPushButton para el botón "Tabla de derivación"
        self.buttonSintactico_3 = QtWidgets.QPushButton(Form)  # Añadimos un botón al formulario
        self.buttonSintactico_3.setGeometry(QtCore.QRect(530, 230, 181, 31))  # Posicionamos y dimensionamos el botón
        self.buttonSintactico_3.setObjectName("buttonSintactico_3")  # Asignamos un nombre interno al botón

        # Llamamos a la función para configurar el texto de los elementos (traducción)
        self.retranslateUi(Form)
        # Conectamos señales y slots automáticamente por nombre (si existen)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # Método para establecer textos en los elementos de la GUI
    def retranslateUi(self, Form):
        # Obtenemos una referencia para traducir textos
        _translate = QtCore.QCoreApplication.translate
        # Establecemos el título de la ventana
        Form.setWindowTitle(_translate("Form", "Form"))
        # Establecemos el texto del QLabel "Sintaxis" en formato HTML
        self.labelSintaxis.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Sintaxis</span></p></body></html>"))
        # Establecemos el texto del botón "Árbol sintáctico"
        self.buttonSintactico.setText(_translate("Form", "Árbol sintáctico"))
        # Establecemos el texto de la etiqueta "Ingrese expresión"
        self.labelExpresion.setText(_translate("Form", "Ingrese expresión"))
        # Establecemos el texto de la etiqueta "Derivación"
        self.labelDerivacion.setText(_translate("Form", "Derivación"))
        # Establecemos el texto del radioButton "Izquierda"
        self.radioButtonIzq.setText(_translate("Form", "Izquierda"))
        # Establecemos el texto del radioButton "Derecha"
        self.radioButtonDer.setText(_translate("Form", "Derecha"))
        # Establecemos el texto del botón "Árbol abstracto"
        self.buttonSintactico_2.setText(_translate("Form", "Árbol abstracto"))
        # Establecemos el texto del botón "Tabla de derivación"
        self.buttonSintactico_3.setText(_translate("Form", "Tabla de derivación"))

# Bloque principal que se ejecuta al iniciar el programa
if __name__ == "__main__":
    # Importamos el módulo sys para manejar argumentos y la salida del programa
    import sys
    # Creamos una aplicación Qt
    app = QtWidgets.QApplication(sys.argv)
    # Creamos una instancia del formulario principal
    Form = QtWidgets.QWidget()
    # Creamos una instancia de nuestra clase de interfaz y configuramos el formulario
    ui = Ui_Form()
    ui.setupUi(Form)
    # Mostramos el formulario en pantalla
    Form.show()
    # Ejecutamos el ciclo de eventos de la aplicación y salimos cuando se cierre la ventana
    sys.exit(app.exec_())
