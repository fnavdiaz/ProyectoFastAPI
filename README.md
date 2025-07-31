# ProyectoFastAPI para el registro de series.
Sistema para registrar las series de televisión, y poder saber que ha visto una persona y cuando, asi como el posible personal de la pelicula (Actores u actrices, Directores, Guionistas, etc..). Utiliza MongoDB, FastAPI y Docker.

## Funcionalidades Principales

- **Registrar** usuario, series que ha visto este en la plataforma y cuándo las ha visto.
- **Registrar** series con sus detalles tales como episodios temporadas, personal...
- **Registrar** personal y detalles.
- **Consultar** cada uno de estos registros.

# Requisitos previos

Antes de comenzar, asegúrate de tener instalado en tu equipo:  
- Docker  
- Git

# Instrucciones para ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/fnavdiaz/ProyectoFastAPI.git
   cd ProyectoFastAPI
   ```

2. Levantar los contenedores con Docker:
   ```bash
   docker-compose up --build
   ```

3. Acceder al swagger donde tendras todos los métodos disponibles en http://localhost:8000/docs
