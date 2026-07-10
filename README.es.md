# AgentOS: El Framework MAS Autónomo

![AgentOS Architecture](assets/CortanaAgentOS.jpg)

Los IDE modernos vienen con potentes agentes LLM base, pero en su estado predeterminado, son esencialmente chatbots sin estado con acceso a la terminal. Sufren de "Negligencia de Idempotencia" (romper el código reintentando malas ediciones), inflado de contexto (agotamiento de memoria), y el síndrome del "Modelo Dios" (intentar resolver problemas de 100k tokens en una ventana de 4k tokens).

Hemos diseñado un **Framework de Contexto AgentOS Personalizado** que se sitúa por encima del agente del IDE. En el momento en que un agente "fresco" despierta en este entorno, se transforma instantáneamente mediante archivos de configuración locales en un **Supervisor Autónomo y Escalado por Riesgo**.

## Características Principales

### 1. Autonomía Escalada por Riesgo
Los agentes frescos tratan todas las tareas por igual. Nuestro AgentOS inyecta un estricto sistema de Autonomía de 4 Niveles:
- **T0**: Lecturas, búsquedas, linting (Auto-Procesar).
- **T1**: Ediciones de un solo archivo (Auto-Procesar. Debe hacer `git commit` de un punto de control primero).
- **T2**: Refactorizaciones de múltiples archivos (Aprobación por Lotes).
- **T3**: Eliminaciones, Inyección Externa, ediciones de Autenticación (Revisión Obligatoria por Equipo Rojo).

### 2. Idempotencia y El Núcleo de Recuperación
Cada mutación debe verificar primero si su efecto ya existe. Si un reemplazo quirúrgico de texto falla, al agente se le permite *un* reintento. En el segundo fallo, debe abortar, previniendo bucles de ejecución infinitos.

### 3. Compresión de Memoria Transaccional
Cuando la memoria de `worklog.md` excede los 4,000 tokens, el agente ejecuta un bucle transaccional de 5 pasos: Destilar → Añadir → Verificar → Truncar → Confirmar (Commit). Esto proporciona una garantía del 100% contra la pérdida de datos de contexto durante caídas del LLM.

### 4. Delegación de Frontera (MAS Supervisor/Trabajador)
Cuando una tarea requiere lógica extrema (40k+ tokens), el SO (Sistema Operativo) activa un paquete de entrega. El agente limpia secretos y claves API, y compila un prompt denso para un Modelo de Frontera externo. Cuando el código regresa, se inyecta literalmente, se analiza estáticamente, y se presenta como un `git diff` para una revisión humana de nivel T3.

### 5. Bloqueo Constitucional y Andamiaje del SO
El agente no puede reescribir sus propios límites de seguridad. Cualquier edición al directorio `.agents/rules/` se clasifica permanentemente como una **acción T3**. Además, si faltan archivos centrales en el inicio, el agente activará automáticamente un cuestionario de selección múltiple para construir la estructura del espacio de trabajo.

## Instalación
¡Simplemente arrastra la carpeta `.agents` a la raíz de tu espacio de trabajo, y tu agente se transformará instantáneamente en el Supervisor V2!
