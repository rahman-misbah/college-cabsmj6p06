server_config = {"timeout": 300, "status": "active"}

# Debug Console
print("Status:", server_config["status"])
print("Admin Email:", server_config.get("admin_email","Not Set"))
print("Setting Count:", len(server_config))
print("Keys:", list(server_config.keys()))
print("Values:", list(server_config.values()))

# Modifications
server_config["timeout"] *= -1
server_config["max_connections"] = 100

# Clean Up
server_config.pop("timeout", None)

# Final Result
print("Keys:", sorted(list(server_config.keys())))