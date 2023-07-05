version ?= beta_ca_es

buildx-docker:
	docker buildx build \
		--platform linux/amd64,linux/arm64 \
		-t projecteaina/mt-api:${VERSION} \
		--push \
		.
deploy:
	docker compose up -d
undeploy:
	docker compose down
stop:
	docker compose stop