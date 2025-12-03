SecurityLogAnalyzer

Sistema de análisis de logs y detección de intentos de fuerza bruta

SecurityLogAnalyzer es una herramienta diseñada para analizar registros de autenticación, identificar patrones de fallos y detectar posibles ataques de fuerza bruta mediante un análisis automático de eventos.

Su objetivo es apoyar a empresas, estudiantes y equipos de TI a comprender mejor el comportamiento de acceso en sus sistemas, reforzar la seguridad y anticiparse a actividades sospechosas.

Características principales

✔ Análisis automático de logs (.csv)

Conteo total de eventos.

Identificación de intentos fallidos.

Agrupación de fallos por dirección IP.

✔ Detección de fuerza bruta

Incluye un módulo especializado (BruteForceDetector) configurable para alertar cuando una IP o usuario supera cierto umbral de intentos fallidos.

✔ Modular y fácil de expandir

El proyecto está organizado por módulos independientes:

utils → lectura y manejo de archivos

analytics → análisis de información

brute_force_detector → detección de ataques

main.py → punto de ejecución

La estructura facilita agregar futuras funciones como: reportes automáticos, visualización de datos, backend API, o integración con SIEM.

Requisitos

Python 3.10 o superior

No requiere librerías externas (todo es estándar)

Cómo ejecutar el programa:

Coloca un archivo logs.csv válido en la carpeta data/.

Abre una terminal en la carpeta principal del proyecto.

Ejecuta:

python main.py


El sistema mostrará:

Estadísticas generales

Fallos por IP

IPs y usuarios sospechosos de fuerza bruta

Licencia

Este proyecto está protegido bajo una licencia propietaria, creada por el autor.
No se permite copiar, modificar, distribuir ni utilizar este software sin autorización escrita.

Para más detalles, revise el archivo: LICENSE

Autor

Desarrollado por Félix Damián Cerna Carrasco (2025).
Estudiante de Ingeniería en Ciberseguridad.
