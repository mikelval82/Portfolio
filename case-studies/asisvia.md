**ASISVIA: caso seleccionado de diseño conceptual y arquitectura**

Ficha editorial preparada el 25 de septiembre de 2026. Su objetivo es definir un caso defendible para el portfolio a partir del material disponible. No es una descripción verificada de la implementación ni una atribución a Mikel de toda la arquitectura del proyecto.

Actualización de implementación: el propietario concretó su contribución como «la concepción del sistema basado en IA generativa para la gestión de las entrevistas y el análisis de resultados». `project-asisvia.html` está redactado alrededor de ese alcance. El flujo ilustrado es una reconstrucción conceptual; las decisiones de sesión y modos de entrevista mencionadas en esta ficha no se han atribuido a Mikel en la página.

**Por qué elegir este caso**

ASISVIA permite conectar la trayectoria de Mikel en investigación sobre personas con su trabajo en agentes conversacionales. Complementa OntoGenix: el primer caso profundiza en implementación y contexto entre etapas; este segundo permite explicar decisiones de interacción, separación de responsabilidades e integración de un sistema.

| Candidato | Qué aporta al perfil | Decisión editorial |
|---|---|---|
| ASISVIA | Contexto de aplicación definido, interacción por voz y material previo con decisiones arquitectónicas concretas | Segundo caso principal |
| THOT | Agentes y formación inmersiva; aparece en el CV aportado | Mantener en experiencia. El material revisado ofrece menos detalle para desarrollar decisiones propias |
| CityVerse | Flujos estructurados e integración con entornos virtuales, descritos en el portfolio anterior | Caso de apoyo. Su organización por estados se solapa más con lo que ya muestra OntoGenix |

Esta selección prioriza complementariedad y evidencia disponible, sin juzgar la importancia real de cada proyecto.

**Contexto que sí está respaldado**

La página oficial de Hospitales Universitarios San Roque identifica ASISVIA como el proyecto PAIS-20241015, con participación de la UPV/LabLENI. Describe el uso de agentes virtuales e interacción por voz para recoger y analizar la experiencia del paciente. También presenta módulos para satisfacción, estado emocional, realidad virtual y gestión de usuarios. Son objetivos y descripciones de diseño; la página no demuestra resultados clínicos ni la contribución individual de Mikel. [Fuente oficial del hospital](https://hospitalessanroque.com/es/transparencia).

**Atribución personal y procedencia de los detalles**

Mikel ha aclarado que su trabajo en estos proyectos fue principalmente conceptual y de arquitectura de software de alto nivel, y que no dispone de código para mostrar. Para ASISVIA ha confirmado específicamente la concepción del sistema de entrevistas y análisis con IA generativa. Ese es el alcance utilizado en la página.

La versión anterior de `service-llm.html`, conservada en Git, describe un flujo conversacional por estados, contexto por sesión, voz, modos prefijados y generativos, y persistencia. Es material aportado por el propietario, útil para reconstruir el caso, pero no una verificación independiente.

| Afirmación candidata | Fuente disponible | Tratamiento en el futuro caso |
|---|---|---|
| Diseño conceptual y arquitectura de alto nivel como tipo de contribución | Aclaración del propietario sobre estos proyectos | Usar ese alcance; concretar sus componentes antes de atribuir decisiones individuales |
| Separación entre flujo prefijado y respuestas generativas | Portfolio anterior | Decisión candidata para explicar control y flexibilidad; falta confirmar autoría, motivo y adopción |
| Separación del contexto entre sesiones | Portfolio anterior | Decisión candidata sobre límites de estado; no presentar concurrencia o aislamiento como propiedades medidas |
| LiveKit, Whisper, GPT-4o-mini, ElevenLabs, LangGraph y PostgreSQL | Portfolio anterior | Detalles históricos por confirmar; no son necesarios para contar el diseño a alto nivel |
| Despliegue hospitalario, funcionamiento en producción y resultados de satisfacción | Afirmaciones del portfolio anterior y objetivos públicos | No convertirlos en resultados comprobados ni en logros individuales sin evidencia adicional |

**Estructura concreta del caso**

Título propuesto: *ASISVIA: designing a conversational system for patient experience*.

1. **Problema y responsabilidad.** Un párrafo sobre el contexto público y otro sobre la contribución personal delimitada.
2. **Arquitectura.** Un diagrama que permita distinguir interacción, estado conversacional, análisis y resultados. Cada componente debe marcarse como documentado o como reconstrucción del diseño.
3. **Dos decisiones.** Candidatas: dónde fijar el flujo y dónde permitir generación; cómo delimitar el contexto de una sesión. Para cada una, registrar alternativa, razón, consecuencia y estado de adopción.
4. **Una interacción.** Recorrido ilustrativo desde una respuesta por voz hasta su incorporación al proceso. Identificarlo como ejemplo reconstruido, no como grabación o traza histórica.
5. **Alcance y aprendizajes.** Qué se entregó como diseño, qué parte se sabe que se adoptó y qué quedó sin observar. Atribuir la implementación y evaluación a quien corresponda.

El caso puede demostrar razonamiento arquitectónico sin mostrar código. Los artefactos deben hacer comprensible el diseño y sus decisiones; no sustituyen la evidencia de implementación, operación o impacto.

**Siguiente trabajo y límites actuales**

Caso implementado con contexto público, contribución confirmada, flujo conceptual y preguntas arquitectónicas sobre adaptación de la entrevista y trazabilidad de la interpretación. Los detalles de proveedores, concurrencia y despliegue se han omitido. La comparación anterior de decisiones candidatas queda como registro editorial, no como tarea pendiente ni como evidencia de autoría.
