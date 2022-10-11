az ad sp create-for-rbac \
    --name "ghActionAzureVote" \
    --scope /subscriptions/25a35ae0-f4ba-4b7a-b070-b584e0ab078c/resourceGroups/rg-aks-jitm \
    --role Contributor \
    --sdk-auth