# udacity-azure-ci-cd

![CI](https://github.com/JanaAlharbi3/udacity-azure-ci-cd/actions/workflows/pythonapp.yml/badge.svg)

A tiny ML web API deployed to **Azure App Service** with **CI (GitHub Actions)** and **CD (Azure Pipelines)**.

## Live app

- **URL:** https://flaskml-jana-151905.azurewebsites.net  
  - Health: `GET /` → `ML API is up 🟢`  
  - Features schema: `GET /features`  
  - Predict: `POST /predict` (JSON)

---

## Project Planning Links

- **Trello Board (To Do / In Progress / Done):**  
  https://trello.com/invite/b/689f402b57e48c9a6e8511d7/ATTI946a399131637955cd0654d305bb1fd02822C96B/udacity-azure-ci-cd
- **Project Plan (Excel):** `https://studentksuedu-my.sharepoint.com/:x:/g/personal/442202214_student_ksu_edu_sa/EZ4NjJuwRcBOmTfpWsTmEwQBmcX618o72bql2TCaw4Oiag?e=f2WJye`
- **Demo Video:** https://youtu.be/F8mm-3J5bFY

---

## Architecture     



├── app.py                    # Flask API (loads model/model.joblib)
├── model/
│   └── model.joblib          # trained scikit-learn model
├── requirements.txt
├── Makefile                  # install / lint / test / all
├── commands.sh               # Azure CLI provisioning + deploy (rubric item)
├── azure-pipelines.yml       # Azure Pipelines (CD)
├── .github/workflows/
│   └── pythonapp.yml         # GitHub Actions (CI)
└── screenshots/              # rubric evidence
    ├── 01_trello_board.png
    ├── 02_spreadsheet.png
    ├── 03_cloud_shell.png
    ├── 04_make_all_pass.png
    ├── 05_green_actions.png
    ├── 06_readme_badge.png
    ├── 07_app_service_portal.png
    ├── 08_pipeline_creation.png
    ├── 09_pipeline_success.png
    └── 10_predict_response.png
# optional venv
python -m venv .venv && source .venv/bin/activate

# install & run checks
make all

# run the API
python app.py    # http://127.0.0.1:8000
curl -s http://127.0.0.1:8000/features | jq

curl -sS -H "Content-Type: application/json" -d '{
  "CHAS": 0, "RM": 6.575, "TAX": 296.0, "PTRATIO": 15.3, "B": 396.9, "LSTAT": 4.98
}' http://127.0.0.1:8000/predict
az webapp config appsettings set \
  -g udacity-rg-centralus -n flaskml-jana-151905 \
  --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true

az webapp config set \
  -g udacity-rg-centralus -n flaskml-jana-151905 \
  --startup-file "gunicorn --bind 0.0.0.0:8000 app:app"
# health
curl -s https://flaskml-jana-151905.azurewebsites.net/

# features
curl -s https://flaskml-jana-151905.azurewebsites.net/features | jq

# prediction
curl -sS -H "Content-Type: application/json" -d '{
  "CHAS": 0, "RM": 6.575, "TAX": 296.0, "PTRATIO": 15.3, "B": 396.9, "LSTAT": 4.98
}' https://flaskml-jana-151905.azurewebsites.net/predict
az webapp log tail -g udacity-rg-centralus -n flaskml-jana-151905
