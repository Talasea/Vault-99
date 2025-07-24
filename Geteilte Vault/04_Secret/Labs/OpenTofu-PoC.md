---
created: 2025-01-10T19:34
updated: 2025-01-10T19:35
---
```yml
terraform {
  required_providers {
    proxmox = {
      source  = "telmate/proxmox"
      version = "~> 2.9"
    }
  }
}

provider "proxmox" {
  pm_api_url       = var.pm_api_url
  pm_user          = var.pm_user
  pm_token_id      = var.pm_token_id
  pm_token_secret  = var.pm_token_secret
  pm_tls_insecure  = var.pm_tls_insecure
}
```