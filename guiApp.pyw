# Importamos las bibliotecas necesarias
import sys  # Proporciona funciones y variables para interactuar con el intérprete de Python
import nltk  # Librería de procesamiento de lenguaje natural, se usa aquí para análisis sintáctico
from guiApp_ui import Ui_Form  # Importa la clase generada para la interfaz gráfica (creada con PyQt Designer)
from PyQt5.QtWidgets import QApplication, QWidget  # Componentes básicos para aplicaciones gráficas en PyQt
from nltk import CFG, ChartParser  # Para definir y analizar gramáticas libres de contexto (CFG)
from nltk.tree import Tree  # Representación de árboles sintácticos

# **Definición de la gramática libre de contexto (CFG)**
# Se define la estructura válida para las expresiones. 
# La gramática se compone de:
# - `E` para expresiones generales, que pueden ser sumas o restas de términos.
# - `T` para términos, que pueden ser multiplicaciones o divisiones de factores.
# - `F` para factores, que son los elementos básicos como números o variables.
gramatica = CFG.fromstring("""
    E -> E '+' T | E '-' T | T  # Una expresión puede ser una suma/resta de otra expresión y un término, o simplemente un término.
    T -> T '*' F | T '/' F | F  # Un término puede ser una multiplicación/división de otro término y un factor, o simplemente un factor.
    F -> '(' E ')' | 'a' | 'b' | 'c' | ... | '9'  
    # Un factor puede ser una expresión encerrada en paréntesis o una letra/número individual.
""")

# **Crea un analizador sintáctico con la gramática definida**
# Este analizador utiliza el algoritmo de chart parsing para procesar y analizar sintácticamente las entradas.
parser = ChartParser(gramatica)

# **Función para derivación paso a paso**
# Dado un árbol sintáctico, muestra las derivaciones paso a paso en el orden especificado.
def derivacion_ordenada(gramatica, expresion_objetivo, orden="izquierda"):
    # Itera sobre todas las posibles derivaciones del analizador sintáctico
    for tree in parser.parse(expresion_objetivo):
        print(f"Derivación paso a paso ({orden}):")  # Indica el orden de derivación
        derivaciones = tree.productions()  # Obtiene las reglas de producción usadas para derivar la expresión
        
        # Si se elige derivación por la derecha, se ordenan las producciones en orden inverso
        if orden == "derecha":
            derivaciones = sorted(derivaciones, key=lambda x: str(x.lhs()), reverse=True)

        # Muestra cada paso de la derivación
        for paso, produccion in enumerate(derivaciones, start=1):
            print(f"Paso {paso}: {produccion}")
        return tree  # Devuelve el árbol derivado

# **Genera un árbol abstracto simplificado**
# Convierte un árbol completo en una representación abstracta que solo incluye operadores y operandos.
def generar_arbol_abstracto(arbol):
    if arbol.height() == 2:  # Si el nodo actual es terminal (altura 2 significa no tiene hijos)
        return arbol[0]  # Devuelve el valor terminal
    elif len(arbol) == 3 and arbol[1] in ['+', '-', '*', '/']:
        # Si el nodo es un operador binario, crea una lista [izquierda, operador, derecha]
        return [generar_arbol_abstracto(arbol[0]), arbol[1], generar_arbol_abstracto(arbol[2])]
    else:
        # Si el nodo tiene otros elementos, procesa cada hijo recursivamente
        return [generar_arbol_abstracto(hijo) for hijo in arbol if isinstance(hijo, nltk.Tree)]

# **Convierte una estructura simplificada a un objeto Tree de NLTK**
def estructura_a_tree(estructura):
    if isinstance(estructura, str):  # Si es un nodo terminal, lo devuelve directamente
        return estructura
    if isinstance(estructura, list) and len(estructura) == 3:
        # Si es una lista de tamaño 3 (operador binario), crea un árbol con el operador como raíz
        operador = estructura[1]
        return Tree(operador, [estructura_a_tree(estructura[0]), estructura_a_tree(estructura[2])])
    elif isinstance(estructura, list) and len(estructura) == 1:
        # Si es una lista de un solo elemento, procesa el único hijo
        return estructura_a_tree(estructura[0])
    else:
        # Si es otro tipo de lista, crea un árbol vacío con los hijos procesados
        return Tree('', [estructura_a_tree(hijo) for hijo in estructura])

# **Construye y muestra un árbol sintáctico completo**
def construir_arbol(tree):
    print("\nÁrbol de derivación completo:")  # Indica que se mostrará el árbol
    tree.pretty_print()  # Muestra el árbol en formato texto en la consola
    tree.draw()  # Abre una ventana gráfica con el árbol visualizado

# **Clase para la ventana gráfica principal**
# Gestiona la interfaz gráfica y conecta botones con sus funciones correspondientes.
class Ventana(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)  # Inicializa el widget base
        self.ui = Ui_Form()  # Carga la interfaz generada automáticamente
        self.ui.setupUi(self)  # Configura los elementos de la interfaz

        # Conecta los botones a las funciones que ejecutan
        self.ui.buttonSintactico.clicked.connect(self.mostrar_arbol_sintactico)
        self.ui.buttonSintactico_2.clicked.connect(self.mostrar_arbol_abstracto)
        self.ui.buttonSintactico_3.clicked.connect(self.mostrar_tabla_derivacion)

    def obtener_expresion(self):
        # Obtiene la expresión ingresada en el cuadro de texto y la separa en tokens
        return self.ui.textExpresion.toPlainText().split()

    def mostrar_arbol_sintactico(self):
        expresion_objetivo = self.obtener_expresion()  # Obtiene la expresión ingresada

        if self.ui.radioButtonIzq.isChecked():  # Derivación por la izquierda
            arbol_izq = derivacion_ordenada(gramatica, expresion_objetivo, orden="izquierda")
            construir_arbol(arbol_izq)
        elif self.ui.radioButtonDer.isChecked():  # Derivación por la derecha
            arbol_der = derivacion_ordenada(gramatica, expresion_objetivo, orden="derecha")
            construir_arbol(arbol_der)

    def mostrar_arbol_abstracto(self):
        expresion_objetivo = self.obtener_expresion()

        # Itera sobre derivaciones posibles y genera árboles abstractos
        for tree in parser.parse(expresion_objetivo):
            arbol_abstracto = generar_arbol_abstracto(tree)
            arbol_nltk = estructura_a_tree(arbol_abstracto)

            print("Árbol visualizable con operadores:")
            arbol_nltk.pretty_print()  # Muestra el árbol abstracto
            arbol_nltk.draw()  # Visualiza el árbol en una ventana gráfica

    def mostrar_tabla_derivacion(self):
        expresion_objetivo = self.obtener_expresion()

        # Muestra la derivación en el orden especificado por el usuario
        if self.ui.radioButtonIzq.isChecked():
            derivacion_ordenada(gramatica, expresion_objetivo, orden="izquierda")
        elif self.ui.radioButtonDer.isChecked():
            derivacion_ordenada(gramatica, expresion_objetivo, orden="derecha")

# **Ejecución del programa**
if __name__ == "__main__":
    mi_applicacion = QApplication(sys.argv)  # Crea la aplicación Qt
    mi_app = Ventana()  # Instancia la ventana principal
    mi_app.show()  # Muestra la ventana
    sys.exit(mi_applicacion.exec_())  # Inicia el bucle de eventos de Qt y termina el programa al cerrarlo
