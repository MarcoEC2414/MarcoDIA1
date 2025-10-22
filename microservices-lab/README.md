# Laboratorio de Microservicios (FastAPI + React)

## Arquitectura inicial
- auth-service/      → Autenticación y tokens JWT
- blog-service/      → Publicaciones, autores y categorías
- email-service/     → Notificaciones y formularios
- frontend/          → Interfaz React
- reverse-proxy/     → Balanceo / Gateway local

Servicios base:
- PostgreSQL (5432)
- Redis (6379)

## Checklist Día 1
- [x] Estructura de carpetas creada
- [x] README en cada servicio
- [x] Docker Compose con PostgreSQL y Redis funcionando
- [x] Variables de entorno en `.env.example`
- [x] Test de conexión a PostgreSQL y Redis realizado (opcional, recomendado)
