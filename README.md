SecurityLogAnalyzer
Plataforma de análisis de registros orientada a la identificación de actividad potencialmente maliciosa

SecurityLogAnalyzer es una solución desarrollada en Python para el procesamiento y análisis de registros de autenticación. Su propósito es proporcionar una revisión clara y estructurada del comportamiento registrado en sistemas, permitiendo identificar fallos recurrentes, patrones irregulares y actividades compatibles con intentos de acceso no autorizados.

El proyecto está diseñado bajo principios de modularidad, claridad y mantenibilidad, facilitando su adopción en entornos académicos, de laboratorio o en pequeñas organizaciones que requieren visibilidad sobre la actividad en sus sistemas.

Objetivos del sistema

Analizar registros de autenticación de forma automatizada.

Identificar intentos fallidos y frecuencia de eventos asociados a direcciones IP específicas.

Detectar comportamientos compatibles con ataques de fuerza bruta.

Proveer resultados interpretables para la toma de decisiones en materia de seguridad.

Servir como base para futuras implementaciones o integraciones en sistemas más amplios.

Componentes principales

El sistema está construido mediante módulos independientes que permiten escalar y modificar la herramienta con facilidad:

Módulo de lectura: procesamiento de archivos CSV y conversión de datos en estructuras manipulables.

Módulo analítico: generación de métricas clave sobre la actividad registrada.

Módulo de detección: identificación de IPs y usuarios cuyo comportamiento excede umbrales definidos.

Archivo principal: coordinación central del proceso de lectura, análisis y reporte.

Ejecución

Requisitos mínimos: Python 3.10 o superior.

Para ejecutar el sistema:

python main.py


El programa procesará automáticamente el archivo de registros ubicado en la carpeta correspondiente y mostrará los resultados del análisis.

Licencia

Este proyecto está protegido por una licencia de uso privado.
No se permite copiar, modificar, distribuir ni utilizar este software sin autorización explícita y por escrito del autor.

Autor

Félix Damián Cerna Carrasco
Estudiante de Ingeniería en Ciberseguridad
