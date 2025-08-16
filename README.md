# udacity-azure-ci-cd

![CI](https://github.com/JanaAlharbi3/udacity-azure-ci-cd/actions/workflows/pythonapp.yml/badge.svg)

A tiny ML web API deployed to **Azure App Service** with **CI (GitHub Actions)** and **CD (Azure Pipelines)**.

## Live app

- **URL:** https://flaskml-jana-151905.azurewebsites.net  
  - Health: `GET /` → `ML API is up 🟢`  
  - Features schema: `GET /features`  
  - Predict: `POST /predict` (JSON)

## Project Planning Links

- **Trello Board (To Do / In Progress / Done):**  
  https://trello.com/invite/b/689f402b57e48c9a6e8511d7/ATTI946a399131637955cd0654d305bb1fd02822C96B/udacity-azure-ci-cd
- **Project Plan (Excel):** `udacity_azure_ci_cd_plan.xlsx`

## Architecture

```mermaid
flowchart LR
  A[GitHub Repo] -- push --> B[GitHub Actions (CI)]
  B -->|lint + tests pass| C[Azure Pipelines (CD)]
  C -->|zip artifact & deploy| D[Azure App Service (Linux, Py 3.10)]
  D -->|HTTP| E[User/Client]
