

set -euo pipefail

RESOURCE_GROUP="udacity-rg"
LOCATION="eastus"
APP_NAME="flaskml-jana-$(date +%H%M%S)"
PY_RUNTIME="PYTHON:3.10"
SKU="F1"
echo "Creating/Updating RG: $RESOURCE_GROUP ($LOCATION)"
az group create -n "$RESOURCE_GROUP" -l "$LOCATION"

echo "Deploying Web App from current folder..."
az webapp up \
  -n "$APP_NAME" \
  -g "$RESOURCE_GROUP" \
  -l "$LOCATION" \
  --runtime "$PY_RUNTIME" \
  --sku "$SKU"

echo "Enabling logs..."
az webapp log config -n "$APP_NAME" -g "$RESOURCE_GROUP" --application-logging true

echo "Deployed URL: https://$APP_NAME.azurewebsites.net"
