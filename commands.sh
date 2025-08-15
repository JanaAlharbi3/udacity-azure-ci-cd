
set -euo pipefail

RESOURCE_GROUP="udacity-rg"
LOCATION="eastus"
PLAN_NAME="udacity-asp-$RANDOM"
APP_NAME="flaskml-jana-$(date +%H%M%S)" 
RUNTIME="PYTHON:3.10"
SKU="B1"   
TAG_VALUE="udacity-azure-ci-cd"   
echo "Creating/Updating RG with tag..."
az group create -n "$RESOURCE_GROUP" -l "$LOCATION" --tags project="$TAG_VALUE"

echo "Creating App Service plan (Linux) with tag..."
az appservice plan create \
  -g "$RESOURCE_GROUP" -n "$PLAN_NAME" \
  --is-linux --sku "$SKU" \
  --tags project="$TAG_VALUE"

echo "Creating Web App with tag..."
az webapp create \
  -g "$RESOURCE_GROUP" -p "$PLAN_NAME" -n "$APP_NAME" \
  --runtime "$RUNTIME" \
  --tags project="$TAG_VALUE"

echo "Building ZIP package..."
zip -r app.zip . -x '*.git*' 'screenshots/*' '__pycache__/*' '*.pyc' '.venv/*' 'venv/*' '.env' >/dev/null

echo "Deploying ZIP to Web App..."
az webapp deployment source config-zip \
  -g "$RESOURCE_GROUP" -n "$APP_NAME" \
  --src app.zip

echo "Enabling logs..."
az webapp log config -n "$APP_NAME" -g "$RESOURCE_GROUP" --application-logging true

echo "Deployed URL: https://$APP_NAME.azurewebsites.net"
