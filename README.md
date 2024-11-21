# PROGRAMA PARA ANALISIS DE SINTAXIS Y GRAMÁTICAS LIBRES DE CONTEXTO

## Hecho por:
- Athina Cappelletti
- Daniela Salazar
- Laura Indabur
  
## Descripción
Este programa se basa en un **analizador sintáctico** utilizando la biblioteca **NLTK** y la clase **ChartParser**. El programa está diseñado para analizar expresiones matemáticas o cadenas de texto basadas en una **gramática libre de contexto (CFG)**, y construir un **árbol sintáctico**, **árbol abstracto**  y **tabla de derivación** que muestra cómo la entrada se ajusta a las reglas definidas por la gramática.

El analizador se enfoca en derivar cadenas de símbolos (como expresiones aritméticas o frases en un lenguaje simplificado) y visualizar la estructura gramatical de esas cadenas.

## Lenguaje utilizado
- **Python**: El proyecto está desarrollado en Python, aprovechando la biblioteca NLTK para el análisis sintáctico. (Python 3.12, miniconda)
- **NLTK (Natural Language Toolkit)**: Utilizado para procesar y analizar la entrada según la gramática definida.

## Instalación
Para ejecutar el programa, es necesario instalar la biblioteca **NLTK** y la biblioteca **PyQt5**. Puedes instalarla mediante **pip**:

```bash
pip install nltk
pip install PyQt5
