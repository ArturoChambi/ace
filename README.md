## Requerimientos implementados

### 1. Ruta principal `/`
Muestra "Bienvenido al Portal Académico." o "Bienvenido nuevamente, [usuario]."
según exista la cookie `usuario_preferido`.

### 2. Ruta `/login`
Formulario que solicita usuario y contraseña. Valida contra el diccionario
de usuarios y guarda el nombre en la sesión.

### 3. Ruta `/cursos`
Lista dinámica con Jinja2. Usa `{% for %}` y `{% if %}` para mostrar
"Curso disponible" o "Curso lleno" según los cupos.

### 4. Ruta `/perfil` (protegida)
Si no hay sesión, redirige a `/login`.

### 5. Cookie `usuario_preferido`
Se crea al iniciar sesión. Se puede eliminar desde la página principal.

### 6. Ruta `/logout`
Elimina la sesión, redirige al inicio y muestra "Sesión cerrada correctamente."