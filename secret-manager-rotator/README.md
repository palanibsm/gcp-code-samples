## Testing

{
    "project_id": "sen-host-project",
    "secret_id": "secret-02",
    "payload": "Chaindavi"
}

Below is for some experiment commands. Kindly ignore
Sample Commands for ref
### Command-01: gcloud secrets create secret-02 --topics projects/sen-host-project/topics/secret-rotator-pubsub
### Command-02: export SM_SERVICE_ACCOUNT="service-77430368358@gcp-sa-secretmanager.iam.gserviceaccount.com"
### Command-03: gcloud pubsub topics add-iam-policy-binding projects/sen-host-project/topics/secret-rotator-pubsub     --member "serviceAccount:${SM_SERVICE_ACCOUNT}"     --role "roles/pubsub.publisher"
### Command-04: gcloud functions add-iam-policy-binding secret-manager --member="serviceAccount:${SM_SERVICE_ACCOUNT}" --role="roles/secretmanager.admin"

#gcloud functions add-iam-policy-binding secret-manager --member="service-77430368358@gcf-admin-robot.iam.gserviceaccount.com " --role="roles/secretmanager.admin"
