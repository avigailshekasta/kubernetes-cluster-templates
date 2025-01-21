provider "azurerm" {
  features {}
  subscription_id ="d5e75b17-cf3b-4fd3-a5d1-566475905e83"
}

# יצירת קבוצת משאבים
resource "azurerm_resource_group" "example" {
  name     = "ResourceGroup"
  location = "East US"
}

# יצירת אשכול AKS
resource "azurerm_kubernetes_cluster" "example" {
  name                = "Cluster"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  dns_prefix          = "myk8scluster"

  default_node_pool {
    name       = "default"
    node_count = 2
    vm_size    = "Standard_DS2_v2"
  }

  identity {
    type = "SystemAssigned"  # מזהה שנוצר אוטומטית
  }

  # לא נדרשים הגדרות נוספות עבור RBAC
}
