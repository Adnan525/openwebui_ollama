# Run OpenWebUI and Ollama from Docker containers

This setup provides a containerized deployment of OpenWebUI with Ollama for running AI models locally.

## Prerequisites
- Docker and Docker Compose installed
- NVIDIA drivers installed (if using GPU acceleration)
- NVIDIA Container Toolkit (if using GPU acceleration)

## Quick Start
Run the included `docker-compose.yml` file with:

```bash
docker-compose up -d
```

The `-d` flag runs containers in detached mode (background). Remove this flag if you want to see the console output.

Once started, access OpenWebUI at: http://localhost:3000

## Compatibility Notes
The docker-compose file was tested with:
```bash
docker-compose version 1.25.0, build unknown
```
nvidia-smi:
```bash
NVIDIA-SMI 535.183.01             Driver Version: 535.183.01   CUDA Version: 12.2  
```

### For newer Docker Compose versions
Newer versions of Docker Compose (V2+) may require modifications to the file:

1. You need to use `docker compose` instead of `docker-compose` (no hyphen)
2. The `version` field in the YAML might need updating
3. GPU access syntax may differ between versions

## Configuration
- OpenWebUI data is persisted in `./open-webui-local/`
- Ollama models are stored in `./ollama-local/`
- Edit the docker-compose.yml file to modify ports or environment variables

## Stopping the Service
To stop the running containers:
```bash
docker-compose down
```

## Troubleshooting
- If OpenWebUI cannot connect to Ollama, both containers must be on the same network. The default network created by Docker Compose handles this automatically.
- For GPU support, make sure your system has the NVIDIA Container Toolkit properly installed.

>Note: Docker Compose automatically creates a default network with DNS resolution, allowing OpenWebUI to connect to Ollama using the service name as hostname (via OLLAMA_BASE_URL=http://ollama:11434).