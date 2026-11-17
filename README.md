# Network Stack Lab

This teaching project uses Docker Compose to run a loopback-only HTTP counter and a Redis service with a named volume. See the course lab tutorial for the complete GitHub and deployment workflow.

From this directory in PowerShell, use a fresh clone:

```powershell
Copy-Item .env.example .env
docker compose config --quiet
docker compose up -d --build --wait
docker compose ps
curl.exe -fsS http://127.0.0.1:8080/
```

Set WEB_PORT in .env if port 8080 is occupied. Use the same port in the browser or curl. Run docker compose down to remove the containers and keep the named volume. Run docker compose down -v only when you intend to erase this lab's counter data.
