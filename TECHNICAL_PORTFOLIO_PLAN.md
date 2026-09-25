**Plan de mejora del portfolio para demostrar nivel técnico**

Preparado e implementado el 25 de septiembre de 2026 sobre la versión local de `Portfolio`, rama `improve-portfolio`. La iteración está aplicada a las páginas y al CV descargable. El sitio público todavía no se ha actualizado.

**Estado de implementación**

- Ampliación con las nuevas fuentes: HERO Harness y Horizon Cyber-Vision pasan a ser casos destacados junto con OntoGenix. Biotecnología y neuroingeniería tienen sección propia en portada, con GEERT, MULTI_GEERT, GePHYCAM, BIOSIGNALS y NeuroSorter. ASISVIA conserva su página como caso complementario.
- Horizon Cyber-Vision recoge concepto, hardware, software y diseño experimental, confirmados por el propietario, además de la autoría principal y de correspondencia del artículo. El capítulo completo se localizó en el libro IWINAC 2022 del propietario. La página incorpora ya arquitectura, componentes, procesos paralelos, tasas de procesamiento y el estudio de visión simulada con cinco voluntarios, con sus límites.
- NeuroSorter corregido desde el código: UMAP, Louvain y plantillas en la variante importada por la aplicación; se reconoce la coautoría con Javier Alegre-Cortés. AI-SpikeScope se omite por indicación del propietario.
- Verificación de esta ampliación: 17 páginas, 319 referencias locales y 44 combinaciones de página y ancho de pantalla sin fallos detectados. En HERO pasan 18 pruebas locales de contratos, ejecución y verificación. Esta iteración no modifica el CV. Los puntos siguientes documentan la primera implementación.
- Portada orientada a Research Engineer, Agentic AI & Knowledge Systems; conserva TMC como cargo actual, Crevillente e Inditex como asignación anterior.
- OntoGenix desarrollado con contribución personal, diagrama del flujo, tabla de contexto, dos decisiones, artefactos de Amazon Ratings, gráfico del estudio y reflexión técnica. Evaluación atribuida al equipo; no se ha reproducido el experimento.
- ASISVIA sustituye el caso genérico. El propietario concretó su aportación: concepción del sistema de IA generativa para gestionar entrevistas y analizar resultados. La página se centra en ese alcance y en el razonamiento arquitectónico, sin atribuirle decisiones de implementación no confirmadas.
- BIOSIGNALS ampliado tras inspeccionar el repositorio: control de grabación, marcadores basados en muestras, captura real y distinción entre el componente EDF y la variante de almacenamiento NumPy.
- Capacidades consolidadas en tres áreas y enlazadas con evidencia; las rutas anteriores redirigen al contenido correspondiente.
- CV descargable corregido para reflejar la aportación conceptual; originales conservados. Dos páginas y seis enlaces mantenidos, con revisión visual.
- Verificación: 14 páginas generadas, 242 referencias locales, ocho páginas principales a cuatro anchos de pantalla, navegación móvil, cuatro redirecciones y lectura sin JavaScript. Detalle en `VALIDATION.md`.

Las secciones siguientes conservan los criterios del plan y la procedencia de las decisiones. La ejecución editorial queda completada dentro del alcance respaldado por las fuentes y las aclaraciones del propietario.

Actualización tras la revisión del repositorio: ya están preparados el [borrador técnico de OntoGenix](case-studies/ontogenix.md), su [diagrama editable](case-studies/ontogenix-context.mmd) y la [ficha de ASISVIA](case-studies/asisvia.md), elegido como segundo caso. La motivación histórica de la especialización de agentes está confirmada por el propietario; la mecánica se ha documentado desde el código.

**Objetivo**

Permitir que una persona que evalúe tu perfil pueda comprender un problema que resolviste, identificar tu responsabilidad, seguir una decisión de ingeniería hasta su implementación y valorar la evidencia del resultado. La profundidad debe reflejar lo que realmente hiciste, con claridad sobre el trabajo del equipo.

La orientación recomendada es **Research Engineer — Agentic AI & Knowledge Systems**, con **Senior Research Engineer en IA aplicada** como objetivo profesional prioritario. Para buscar oportunidades también encaja la denominación Senior Applied AI Engineer cuando el puesto incluya investigación, diseño de sistemas e implementación. Es una recomendación basada en tu trayectoria y en las contribuciones que has confirmado, no una equivalencia automática entre títulos de empresas.

La combinación que conviene hacer visible es investigación, diseño conceptual, arquitectura e implementación. OntoGenix permite conectar esas capacidades en un mismo proyecto; tu aportación a otros proyectos puede mostrar capacidad para definir sistemas y orientar su construcción. El trabajo previo en neuroingeniería aporta continuidad experimental y amplitud de problemas abordados.

Texto de posicionamiento propuesto para la portada, pendiente de aplicar: **Research Engineer · Agentic AI & Knowledge Systems**. Frase de apoyo: *I design and build AI systems that connect language models, agents and structured knowledge, drawing on a background in software engineering and experimental research.* El cargo de la experiencia laboral seguirá siendo AI Consultant at TMC; la especialización de la portada y el objetivo profesional son conceptos diferentes.

**Progresión profesional que debe apoyar el portfolio**

| Horizonte | Dirección recomendada | Evidencia que conviene presentar o desarrollar |
|---|---|---|
| Próxima oportunidad | Senior Research Engineer en un equipo de IA aplicada, producto o I+D con responsabilidad de implementación | Capacidad para formular un problema, comparar enfoques, construir una solución y explicar resultados y límites |
| Evolución técnica | Staff Research Engineer / Staff Applied AI Engineer | Decisiones adoptadas por otras personas, contribución a estándares y evaluación, coordinación técnica y mejoras que beneficien a un equipo |
| Mayor alcance | Principal Engineer o responsabilidad de arquitectura de sistemas de IA, según la organización | Criterio aplicado a varios sistemas o equipos, continuidad de las decisiones y resultados de su adopción |

La progresión depende del alcance demostrado, sin fijar plazos ni atribuirte ahora responsabilidades no documentadas. Como referencia, GitLab distingue el nivel Staff por su influencia más allá del propio equipo, estándares técnicos y mentoría, además de la ejecución. [Descripción de roles de ML en GitLab](https://handbook.gitlab.com/job-description-library/engineering/development/data-science/machine-learning/).

Para sostener esa evolución conviene reunir evidencia de tres dimensiones todavía poco visibles en el portfolio: evaluación y diagnóstico; operación y mantenimiento de sistemas; adopción de tus decisiones por otras personas. Son lagunas de documentación, no una afirmación de que carezcas de esa experiencia. Si falta experiencia en alguna, se convertirá en un objetivo de desarrollo profesional. Un experimento futuro pequeño sobre contexto entre agentes podría demostrar diseño de evaluación propio, claramente separado de la validación histórica de OntoGenix.

El formato de los casos también debe ayudarte en entrevistas: problema, aportación personal, alternativas, decisiones y aprendizaje. Monzo pide explícitamente explorar contribuciones, implementación y compromisos de diseño en su proceso Senior Staff+. Se toma como ejemplo de evaluación profesional, no como criterio universal. [Proceso técnico de Monzo](https://monzo.com/blog/demystifying-the-senior-staff-engineering-interview-process).

Se mantienen los datos corregidos: Crevillente; TMC como puesto actual según el contexto disponible; Inditex como asignación anterior, sin una fecha de fin inventada.

**1. Seleccionar qué debe demostrar cada caso**

| Caso | Prioridad | Capacidad que debe demostrar | Material disponible | Información pendiente |
|---|---|---|---|---|
| OntoGenix | Primer caso principal | Idea → arquitectura → implementación → comunicación científica; especialización de agentes y gestión de su contexto | Código y prompts inspeccionados, artefactos guardados, publicación, evaluación del equipo, contribución y motivación confirmadas | No bloquea la redacción. Solo añadir comparaciones históricas o cifras sobre especialización si existe evidencia |
| ASISVIA | Segundo caso principal, elegido por complementariedad | Formulación del problema y diseño arquitectónico de alto nivel | Contexto oficial del hospital, portfolio anterior y aclaración general del propietario sobre su contribución conceptual y arquitectónica | Atribución de decisiones concretas y adopción; no hace falta código para preparar el caso |
| BIOSIGNALS | Caso complementario | Ingeniería de adquisición, sincronización y registros experimentales | Repositorio público y captura real de la aplicación | Contribuciones concretas, problema de sincronización resuelto y ejemplo de uso verificable |
| NeuroSorter y otros | Apoyo en la sección de investigación | Amplitud de experiencia y continuidad del trabajo científico | Referencias de software e investigación | Ampliar solo si aporta una dimensión que no cubren los anteriores |

Si un proyecto reciente propio tiene mejor evidencia y mayor aportación personal que las opciones de agentes, puede ocupar el segundo lugar. No es obligatorio presentar tres casos con la misma extensión.

**2. Construir un inventario de evidencia antes de redactar**

Para cada afirmación relevante, registrar: qué se afirma, tu responsabilidad, fuente concreta, versión o fecha, condiciones y límite de la conclusión. El resultado será una ficha breve por proyecto.

Separar expresamente:

- Comportamiento observado en el código: no prueba por sí solo que funcionara en una ejecución ni quién lo implementó.
- Resultado publicado: atribuido al estudio y a su protocolo, sin convertirlo automáticamente en un resultado individual.
- Experiencia que confirmas: explica responsabilidad y contexto, aunque no haya un repositorio público.
- Ejecución observada: acompañada del entorno, entrada y salida correspondiente.
- Propuesta de mejora actual: presentada como lo que cambiarías hoy, sin adjudicarla retrospectivamente al sistema original.

No es necesario disponer de una métrica numérica para cada contribución. Un ejemplo verificable, una decisión bien explicada y un fallo diagnosticado también aportan evidencia técnica.

**3. Desarrollar primero OntoGenix como caso de referencia**

Contribución confirmada por el propietario el 25 de septiembre de 2026: desarrolló la idea y el diseño conceptual, la arquitectura, la implementación y la redacción del artículo. La validación correspondió a otros miembros del equipo. Se describirá su contribución principal sin convertirla en autoría exclusiva del proyecto o del artículo.

Texto de contribución propuesto: *I developed the concept, designed and implemented the system, and wrote the manuscript. Other members of the research team carried out the validation.* Mantener la referencia bibliográfica con todos sus autores. Los resultados publicados se atribuirán al estudio; no se afirmará que el propietario diseñó o ejecutó la evaluación.

El eje del caso será **cómo dividir una tarea compleja entre agentes conservando el contexto necesario para cada etapa**, identificado por el propietario como la decisión técnica más difícil. Título editorial propuesto: *OntoGenix: decomposing ontology engineering into specialised agents*. El relato debe explicar dónde situaste los límites de responsabilidad y cómo conectaste sus resultados.

Motivación confirmada posteriormente por el propietario: pedir a los agentes varios pasos complejos producía alucinaciones y errores; especializarlos permitía acotar tarea y contexto. La lectura del repositorio documenta ese mecanismo. No hace falta pedirle que reconstruya detalles que están disponibles en el código, y no se necesita una cifra de reducción de errores para explicar la decisión.

La inspección ha seguido el controlador, los agentes, sus plantillas, la preparación de datos, el parseo y la materialización. Se ha leído código, sin ejecutar la aplicación, invocar modelos ni reproducir experimentos. Referencia: commit `3c1693b6f1292920b479027fe889af9861d99555`, coincidente con el HEAD remoto el 25 de septiembre de 2026. Los hallazgos y enlaces exactos se detallan en [el borrador del caso](case-studies/ontogenix.md).

| Tema | Evidencia localizada | Trabajo propuesto |
|---|---|---|
| Contexto construido para cada petición | [LlmBase.py](https://github.com/tecnomod-um/OntoGenix/blob/3c1693b6f1292920b479027fe889af9861d99555/GUI/LLM_base/LlmBase.py) envía rol de sistema y contenido preparado para la llamada; [LLM_planner.py](https://github.com/tecnomod-um/OntoGenix/blob/3c1693b6f1292920b479027fe889af9861d99555/GUI/PlanSage/LLM_planner.py) y [LLM_ontology.py](https://github.com/tecnomod-um/OntoGenix/blob/3c1693b6f1292920b479027fe889af9861d99555/GUI/OntoBuilder/LLM_ontology.py) componen entradas específicas | Explicar qué información se transmite, qué queda en la aplicación y qué necesita reconstruirse. No deducir de esta lectura una estrategia global de memoria ni un ahorro de tokens medido |
| Orquestación restringida por estados | [automata_manager.py](https://github.com/tecnomod-um/OntoGenix/blob/3c1693b6f1292920b479027fe889af9861d99555/GUI/GuiManager/automata_manager.py#L93) define estados y transiciones; [LLM_Genie.py](https://github.com/tecnomod-um/OntoGenix/blob/3c1693b6f1292920b479027fe889af9861d99555/GUI/GuiManager/LLM_Genie.py#L34) incorpora estado y siguientes pasos al flujo del asistente | Dibujar el recorrido real y explicar qué restricciones se buscaban; confirmar contigo por qué se eligió este enfoque |
| Reintentos de generación de ontologías | [GuiBehavior.py:451](https://github.com/tecnomod-um/OntoGenix/blob/3c1693b6f1292920b479027fe889af9861d99555/GUI/GuiManager/GuiBehavior.py#L451) contiene un bucle limitado y tratamiento de errores sintácticos | Elegir una entrada y un error concretos; mostrar cómo se genera el feedback y cuándo se detiene el proceso |
| Corrección de mappings | [LLM_ontomapper.py:29](https://github.com/tecnomod-um/OntoGenix/blob/3c1693b6f1292920b479027fe889af9861d99555/GUI/OntoMapper/LLM_ontomapper.py#L29) acepta feedback; en [GuiBehavior.py:633](https://github.com/tecnomod-um/OntoGenix/blob/3c1693b6f1292920b479027fe889af9861d99555/GUI/GuiManager/GuiBehavior.py#L633) hay partes del bucle de reintentos comentadas | Distinguir corrección asistida y automatización efectivamente activa; no describir una recuperación autónoma completa sin comprobarla |
| Materialización del grafo | [KGEN.py:58](https://github.com/tecnomod-um/OntoGenix/blob/3c1693b6f1292920b479027fe889af9861d99555/GUI/KG_Generator/KGEN.py#L58) conecta con Morph-KGC y serializa el resultado | Mostrar el contrato entre dataset, ontology/mapping y salida, incluyendo un ejemplo de fallo de integración |

La figura principal deberá mostrar las entradas y salidas de cada agente, además de las conexiones. Este es el inventario inicial, obtenido del código; debe contrastarse con el recorrido y la versión elegidos para el caso:

| Componente | Contexto observado en la implementación | Salida o responsabilidad |
|---|---|---|
| PlanSage | Tarea, resumen estadístico JSON, metadatos opcionales; segunda llamada con esquema y resultados de Schema.org | Descripción inicial y respuesta de interoperabilidad. En este código la segunda llamada sustituye `answer`, que será consumido por OntoBuilder |
| OntoBuilder | Datos JSON, descripción de PlanSage y, en el camino de corrección, feedback de error | Generación o revisión de la ontología |
| OntoMapper | Descripción o ontología según el camino, referencia al dataset, formatos y feedback de error cuando se facilita | Mapping, extraído como bloque RML |
| Genie y controlador de la aplicación | Petición, estado actual y siguientes estados posibles; el controlador conserva y pasa los artefactos | Selección de acción y coordinación del flujo |

El código muestra composición explícita de entradas y transferencia de artefactos. El motivo principal ya está confirmado por el propietario. No se presentará como probado que evita toda pérdida de contexto, ni se inventarán alternativas ensayadas o mejoras medidas.

La reflexión sobre qué cambiarías hoy puede partir de tres observaciones verificables del código: conservación separada del esquema durante el enriquecimiento; sustitución de delimitadores textuales frágiles por contratos estructurados; y precisión sobre qué reintentos están activos. La sustitución de `plan_builder.answer` plantea un riesgo de pérdida de parte del esquema inicial. Se documentará como inferencia estática y propuesta futura, no como un fallo histórico reproducido.

Las dos decisiones a desarrollar serán: (1) dónde dividir las responsabilidades entre agentes; (2) qué contexto transmitir en cada frontera y cómo corregir una salida inválida. Comparar con alternativas realmente consideradas. Si una alternativa se propone ahora —por ejemplo, pasar todo el historial a todos los agentes— se etiquetará como comparación retrospectiva, sin inventar que fue ensayada.

La [evaluación pública](https://github.com/tecnomod-um/OntoGenixEvaluation#results-of-the-estimation-of-time-saving) compara seis datasets. Reporta ahorros de tiempo del 8,2 % al 58,3 %, contando generación, revisión y adaptación, y excluyendo el análisis del CSV común a ambos procedimientos. También documenta limitaciones de modelado y resultados de calidad mixtos. Estos datos permiten presentar resultados con sus condiciones; no justifican trasladar porcentajes de otros experimentos a este estudio.

Entregables del caso:

- Un resumen de seis líneas: problema, usuarios, responsabilidad, dificultad, resultado y fuente.
- Un diagrama editable de la arquitectura real, con límites entre UI, orquestación, LLM, comprobaciones de formato y materialización. Distinguir estas comprobaciones en ejecución de la validación científica realizada por el equipo.
- Dos decisiones técnicas: alternativa considerada, elección, motivo, coste asumido y consecuencia. Tus motivos se documentarán a partir de tu explicación, no se deducirán del código.
- Un recorrido concreto de entrada a salida. Preferencia por materiales existentes; si hay que ejecutar algo nuevo, se identificará como una reproducción actual.
- Una visualización compacta de resultados publicados con protocolo y limitaciones junto a los datos.
- Un ejemplo de fallo: qué detectaba el sistema, qué no podía garantizar y cómo se resolvía.
- Dos o tres enlaces al código de la versión analizada, acompañados de una explicación de qué merece la pena observar.
- Un párrafo final: qué mantendrías y qué cambiarías hoy. Debe expresar criterio, sin insinuar que esas mejoras ya existían.

Criterio de cierre: un revisor puede localizar tu aportación y seguir al menos una decisión desde el problema hasta código y evidencia. Queda explícito qué produjo el equipo, qué hiciste tú y qué falta verificar.

**4. Construir un caso de diseño arquitectónico de agentes**

Sustituir la página genérica “Conversational AI & XR” por **ASISVIA**. MindFrameAI puede seguir como contexto profesional. La [ficha de selección y redacción](case-studies/asisvia.md) compara ASISVIA, THOT y CityVerse y documenta la procedencia de cada detalle.

ASISVIA complementa OntoGenix al conectar agentes conversacionales con la experiencia previa en investigación sobre personas. El portfolio anterior ofrece decisiones candidatas sobre flujo prefijado/generativo y separación del contexto por sesión. La fuente oficial respalda el contexto del proyecto, pero no acredita esa implementación ni su autoría individual.

El propietario aclara que su aportación fue principalmente el desarrollo conceptual de las ideas y el diseño arquitectónico del software a alto nivel, y que no dispone de código para mostrar. Ese será el alcance inicial; falta concretar la atribución de decisiones dentro de ASISVIA. No se requiere conseguir un repositorio para construir este caso.

Desarrollar un escenario de uso antes de describir todo el sistema. La evidencia principal serán decisiones justificadas, responsabilidades de componentes, flujos de información y consecuencias de las decisiones adoptadas. Si la adopción no puede acreditarse, describir el diseño y su estado conocido.

El relato cubrirá:

- Problema de los usuarios, objetivo del sistema y restricciones conocidas.
- Componentes que propusiste, sus responsabilidades y la información intercambiada.
- Dos decisiones propias: alternativas, criterio de elección y coste o limitación aceptados.
- Una secuencia de interacción, identificada como flujo diseñado o comportamiento observado según la evidencia.
- Cómo se transmitió el diseño al equipo, qué se adoptó y qué cambió durante el desarrollo, si se conoce.
- Estado alcanzado: diseño, prototipo, piloto o despliegue. Separar el estado del proyecto del alcance de tu contribución.
- Riesgos previstos y método de evaluación propuesto. Incluir fallos o resultados reales solo cuando puedas respaldarlos.

Entregables: ficha de contribución, diagrama de componentes, una secuencia y dos registros breves de decisión. Podemos reconstruir estos materiales a partir de tu explicación; llevarán la indicación de que son una reconstrucción actual del diseño histórico. Si se conserva documentación original, servirá como fuente adicional. Un ejemplo ilustrativo no se presentará como una traza de ejecución.

Texto de rol propuesto, a concretar por proyecto: *My contribution focused on concept development and high-level software architecture.* No sustituirlo por verbos como “implemented”, “deployed” u “optimised” sin atribución específica. La aclaración general del propietario tampoco demuestra que nunca implementara ningún componente.

Criterio de cierre: el lector entiende qué diseñaste, por qué, qué parte se adoptó o quedó como propuesta y hasta dónde llega la evidencia disponible. Este caso demuestra criterio arquitectónico; OntoGenix proporciona la evidencia principal de implementación.

**5. Usar BIOSIGNALS para mostrar otra dimensión de ingeniería**

Conservarlo como caso más breve. Su función será mostrar que tu experiencia incluye sistemas experimentales y la calidad de los datos, además de aplicaciones con LLM.

Revisar el recorrido adquisición → sincronización de eventos → interfaz → almacenamiento. Localizar después un problema concreto de tiempos, concurrencia, pérdida de datos o finalización de grabaciones, si lo hubo. Publicar solo el mecanismo y las condiciones que puedan respaldarse.

Entregables: captura real anotada, diagrama del flujo, una decisión relevante y un ejemplo de salida o uso científico. No añadir cifras de latencia o precisión por estimación.

La información específica para este caso se pedirá después de cerrar el primero, evitando que tengas que reconstruir toda tu carrera de una vez.

**6. Adaptar la web para facilitar dos niveles de lectura**

| Elemento | Cambio | Criterio de aceptación |
|---|---|---|
| Portada | Titular Research Engineer · Agentic AI & Knowledge Systems y frase de apoyo propuesta | En una primera lectura se entiende qué perfil ofreces y dónde ver trabajo relevante; el cargo actual sigue identificado por separado |
| Tarjetas | Una frase sobre el problema, una sobre tu contribución y una evidencia destacada | Cada tarjeta conduce a una prueba o explicación concreta |
| Inicio de cada caso | Resumen, rol, fechas y estado | Un lector no necesita leer toda la página para ubicar el proyecto |
| Profundidad técnica | Índice local; arquitectura, decisiones y límites; ejecución y resultados cuando haya evidencia | Un revisor técnico encuentra rápido los apartados que necesita y distingue diseño de comportamiento observado |
| Visuales | Capturas, trazas y diagramas específicos con leyendas | Cada imagen explica una relación, decisión o resultado; las ilustraciones decorativas quedan en segundo plano |
| Capacidades | Vincular cada capacidad importante a uno de los casos | Se puede pasar de una afirmación de competencia a su evidencia |
| Servicios | Consolidar las páginas repetitivas alrededor de tres áreas | Se mantienen enlaces anteriores mediante rutas compatibles o redirecciones válidas |

Mantener la base visual actual. No hace falta añadir animaciones o rehacer la identidad para completar esta iteración.

Aplicación en archivos:

- `site/home.html`: posicionamiento, tarjetas y relación entre capacidades y casos.
- `site/build.py`: ampliar las definiciones de `CASES` y la plantilla de artículo con bloques de contribución, decisiones y evaluación. Mantener separadas las capacidades generales.
- `images/projects/`: capturas y figuras específicas; conservar los originales y fuentes editables de los diagramas.
- `css/portfolio.css`: composición para diagramas, comparaciones y bloques de evidencia; lectura en móvil.
- `CONTENT_NOTES.md`: fuentes, versiones, atribución y aclaraciones sobre nuevas reproducciones.
- `site/check.py` y `VALIDATION.md`: enlaces, fragmentos y comprobaciones de la presentación final.

No es necesario cambiar de framework ni refactorizar todo el generador para trabajar el contenido.

**7. Orden de ejecución y comprobación final**

1. Completado: orientación recomendada, contribución y motivación de OntoGenix, lectura del repositorio y selección de ASISVIA.
2. Preparado: borrador técnico y diagrama editable de OntoGenix, con entradas por agente, artefactos guardados y límites observados. Convertirlo en artículo de portfolio, separando validación científica y comprobaciones internas.
3. Preparada: ficha de ASISVIA con contexto respaldado y decisiones candidatas. Redactar el caso de arquitectura sin exigir código; concretar atribuciones antes de presentar decisiones como logros personales.
4. Preparar la ficha breve de BIOSIGNALS. Puede iniciarse la inspección del repositorio mientras se redacta el segundo caso.
5. Actualizar la portada, tarjetas y capacidades a partir de la evidencia reunida.
6. Revisar consistencia entre casos, experiencia y CV; comprobar legibilidad de diagramas y tablas en escritorio y móvil.

Para cerrar la iteración, los dos casos principales deben permitir responder: qué problema abordaste, qué hiciste tú, por qué elegiste ese diseño y qué limitaciones quedaron. OntoGenix conectará decisiones con implementación y resultados del estudio. El segundo caso conectará decisiones con arquitectura y adopción conocida, sin exigir resultados de ejecución no disponibles. Al menos una afirmación relevante por caso debe llevar a una fuente o artefacto concreto, identificando las reconstrucciones. Los resultados numéricos deben incluir contexto y procedencia.

La evidencia de un nuevo ensayo debe distinguirse de la de un estudio histórico. No hace falta rehacer experimentos costosos ni ejecutar APIs para redactar un caso sólido si la documentación existente resulta suficiente.

El resultado previsto es una versión local revisable con dos casos principales, un caso complementario y una portada que los represente. La publicación será una acción posterior.

**Decisiones cerradas y revisión pendiente**

Ya incorporado: orientación hacia Research Engineer en IA aplicada; responsabilidad principal en OntoGenix desde la idea hasta la implementación y redacción, con validación del equipo; especialización motivada por alucinaciones y errores en tareas complejas; aportación conceptual y arquitectónica en los otros proyectos; ASISVIA seleccionado como segundo caso.

La lectura del repositorio permite desarrollar OntoGenix sin otra ronda de preguntas generales. Hay materiales concretos para explicar tareas, contexto, coordinación, corrección y límites. No se ha medido de nuevo el efecto de la especialización.

La aclaración final de ASISVIA delimita la contribución a la concepción de IA generativa para entrevistas y análisis de resultados. La página implementada usa ese alcance; los modos prefijado/generativo y el aislamiento por sesión del portfolio anterior no se presentan como decisiones personales confirmadas. No quedan preguntas pendientes para esta iteración.

No hay una nueva petición de elección de proyecto ni de explicación general del repositorio. Los siguientes pasos de edición ya están definidos en este documento.
