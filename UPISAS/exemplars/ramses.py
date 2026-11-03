docker_config = {
    "name": "simulation-scenario",
    "image": "giamburrasca/scenario1:arm64",
    "network": "ramses-sas-net",
    "environment": {
        "ADAPT": "0",
        "FAILURE_INJECTION_1_START": "120",
    },
}
